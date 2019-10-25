import tensorflow as tf
import cv2
import glob
image_filenames = glob.glob("./face_age/*/*.jpg")

from collections import defaultdict
faces_list = defaultdict(list)

face_cascade = cv2.CascadeClassifier('./frontalFace10/haarcascade_frontalface_default.xml')

from itertools import groupby

# Split up the filename into its breed and corresponding filename. The breed is found by taking the directory name
image_filename_with_age = list(map(lambda filename: (filename.split("\\")[1], filename), image_filenames))
# Group each image by the breed which is the 0th element in the tuple returned above
for age, faces in groupby(image_filename_with_age, lambda x: x[0]):
    # Enumerate each breed’s image and send ~20% of the images to a testing set
    for i, faces in enumerate(faces):
        faces_list[age].append(faces[1])

def save_cropped_face(dataset, lacation):
    imgNum = 0
    for age, face_names in dataset.items():
        print(age)
        for face_names in face_names:
            print(face_names)
            image_file = tf.read_file(face_names)
            img2 = tf.image.decode_jpeg(image_file)

            img = tf.image.convert_image_dtype(img2, dtype=tf.uint8)
            with tf.Session() as sess:
                image = sess.run(img)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)


            for (x, y, w, h) in faces:
                col_image = cv2.imread(face_names)
                cropped = col_image[y - int(h / 100):y + h + int(h / 100), x - int(w / 100):x + w + int(w / 100)]
                resized_image = cv2.resize(cropped, (250, 250))

                # 이미지를 저장
                cv2.imwrite("output/img" + str(imgNum) + ".jpg", resized_image)
                imgNum += 1


    print('Done')

save_cropped_face(faces_list, "./output")







