import tensorflow as tf

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
image = tf.reshape(record_image, [250, 151, 1])
label = tf.cast(features['label'], tf.string)
min_after_dequeue = 10
batch_size = 10
capacity = min_after_dequeue + 3 * batch_size
image_batch, label_batch = tf.train.shuffle_batch([image, label], batch_size=batch_size, capacity=capacity, min_after_dequeue=min_after_dequeue)


sess = tf.Session()
sess.run(tf.global_variables_initializer())
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord=coord)

for i in range(200):
  print(sess.run(label_batch))

coord.request_stop()
coord.join(threads)
sess.close()

