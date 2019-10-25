import tensorflow as tf

# TFrecord reading
filename_queue = tf.train.string_input_producer(tf.train.match_filenames_once("./output2/training_images/*.tfrecords"))

reader = tf.TFRecordReader()
_, serialized = reader.read(filename_queue)
features = tf.parse_single_example(serialized,
    features={
    'label': tf.FixedLenFeature([], tf.string),
    'image': tf.FixedLenFeature([], tf.string),
    })
record_image = tf.decode_raw(features['image'], tf.uint8)
# Changing the image into this shape helps train and visualize the output by
# converting it to be organized like an image.
image = tf.reshape(record_image, [250, 250, 1])
label = tf.cast(features['label'], tf.string)
min_after_dequeue = 10
batch_size = 100
capacity = min_after_dequeue + 3 * batch_size
image_batch, label_batch = tf.train.shuffle_batch([image, label], batch_size=batch_size, capacity=capacity, min_after_dequeue=min_after_dequeue)

# Converting the images to a float of [0,1) to match the expected input to convolution2d
float_image_batch = tf.image.convert_image_dtype(image_batch, tf.float32)

conv2d_layer_one = tf.contrib.layers.convolution2d(
    float_image_batch,
    num_outputs=32,     # The number of filters to generate
    kernel_size=(2,2),          # It's only the filter height and width.
    activation_fn=tf.nn.relu,
    #weights_initializer=tf.random_normal,
    stride=(2, 2),
    trainable=True)
pool_layer_one = tf.nn.max_pool(conv2d_layer_one,
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding='SAME')

conv2d_layer_two = tf.contrib.layers.convolution2d(
    pool_layer_one,
    num_outputs=64,        # More output channels means an increase in the number of filters
    kernel_size=(2,2),
    activation_fn=tf.nn.relu,
    #weights_initializer=tf.random_normal,
    stride=(1, 1),
    trainable=True)
pool_layer_two = tf.nn.max_pool(conv2d_layer_two,
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding='SAME')

flattened_layer_two = tf.reshape(
    pool_layer_two,
    [
        batch_size,  # Each image in the image_batch
        -1           # Every other dimension of the input
    ])

# The weight_init parameter can also accept a callable, a lambda is used here  returning a truncated normal
# with a stddev specified.
hidden_layer_three = tf.contrib.layers.fully_connected(
    flattened_layer_two,
    512,
    #weights_initializer=lambda i, dtype: tf.truncated_normal([38912, 512], stddev=0.1),
    activation_fn=tf.nn.relu
)

# Dropout some of the neurons, reducing their importance in the model
hidden_layer_three = tf.nn.dropout(hidden_layer_three, 0.5)

# The output of this are all the connections between the previous layers and the 120 different dog breeds
# available to train on.
final_fully_connected = tf.contrib.layers.fully_connected(
    hidden_layer_three,
    6,  # Number of dog breeds in the ImageNet Dogs dataset
    #weights_initializer=lambda i, dtype: tf.truncated_normal([512, 3], stddev=0.1)
)

#학습시킬 차례
import glob

# Find every directory name in the imagenet-dogs directory (n02085620-Chihuahua, ...)
labels = list(map(lambda c: c.split("\\")[-1], glob.glob("./input/*")))

# Match every label from label_batch and return the index where they exist in the list of classes
train_labels = tf.map_fn(lambda l: tf.where(tf.equal(labels, l))[0,0:1][0], label_batch, dtype=tf.int64)

loss = tf.reduce_mean(
    tf.nn.sparse_softmax_cross_entropy_with_logits(
        logits=final_fully_connected, labels=train_labels))

batch = tf.Variable(0)
#increment_batch=batch.assign_add(1)
learning_rate = tf.train.exponential_decay(
    0.01,
    batch * 3,
    120,
    0.95,
    staircase=True)

optimizer = tf.train.AdamOptimizer(
    learning_rate, 0.9).minimize(
    loss, global_step=batch)

train_prediction = tf.nn.softmax(final_fully_connected)

saver=tf.train.Saver()
sess = tf.Session()
sess.run(tf.global_variables_initializer())
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

# actual training steps
training_steps = 200
for step in range(training_steps):
#  sess.run([increment_batch, optimizer])
  sess.run(optimizer)
  if step%10 ==0:
      print("loss=", sess.run(loss))

saver.save(sess, './my-model/', global_step=training_steps)
coord.request_stop()
coord.join(threads)
sess.close()

