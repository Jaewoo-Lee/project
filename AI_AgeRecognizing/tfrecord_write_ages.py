import tensorflow as tf
import glob
image_filenames = glob.glob("./input/*/*.jpg")

from itertools import groupby
from collections import defaultdict
training_dataset = defaultdict(list)
testing_dataset = defaultdict(list)

# Split up the filename into its breed and corresponding filename. The breed is found by taking the directory name
image_filename_with_breed = list(map(lambda filename: (filename.split("\\")[1], filename), image_filenames))
# Group each image by the breed which is the 0th element in the tuple returned above
for dog_breed, breed_images in groupby(image_filename_with_breed, lambda x: x[0]):
    # Enumerate each breed’s image and send ~20% of the images to a testing set
    for i, breed_image in enumerate(breed_images):
        if i % 5 == 0:
            testing_dataset[dog_breed].append(breed_image[1])
        else:
            training_dataset[dog_breed].append(breed_image[1])
    # Check that each breed includes at least 18% of the images for testing
    breed_training_count = len(training_dataset[dog_breed])
    breed_testing_count = len(testing_dataset[dog_breed])
    assert round(breed_testing_count / (breed_training_count +
                                        breed_testing_count), 2) > 0.18, "Not enough testing images."

def write_records_file(dataset, record_location):
    sess=tf.Session()
    writer = None
    # Enumerating the dataset because the current index is used to breakup the files
    # if they get over 100 images to avoid a slowdown in writing.
    current_index = 0
    for breed, images_filenames in dataset.items():
        print(breed)
        for image_filename in images_filenames:
            if current_index % 100 == 0:
                if writer:
                  writer.close()
                record_filename = "{record_location}-{current_index}.tfrecords".format(record_location=record_location, current_index=current_index)
                writer = tf.python_io.TFRecordWriter(record_filename)
            current_index += 1
            print(image_filename)
            image_file = tf.read_file(image_filename)
            image = tf.image.decode_jpeg(image_file)
            # Converting to grayscale saves processing and memory but isn't required.
            grayscale_image = tf.image.rgb_to_grayscale(image)
            resized_image = tf.image.resize_images(grayscale_image, [250, 250])
            # tf.cast is used here because the resized images are floats but
            # havent been converted into image floats where an RGB value is between [0,1).
            image_bytes = sess.run(tf.cast(resized_image, tf.uint8)).tobytes()
            # Instead of using the label as a string, it'd be more efficient to
            # turn it into either an integer index or a one-hot encoded rank one tensor.
            image_label = breed.encode("utf-8")
            example = tf.train.Example(features=tf.train.Features(feature=
                {'label': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_label])),
                 'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_bytes]))}
                ))
            writer.write(example.SerializeToString())
    print('DONE')
    writer.close()

write_records_file(testing_dataset, "./output2/testing_images/testing_image")
write_records_file(training_dataset, "./output2/training_images/training_image")