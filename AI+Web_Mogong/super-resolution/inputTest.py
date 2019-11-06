import urllib.request
import cv2, os, glob
import numpy as np
from keras.models import load_model
from Subpixel import Subpixel
from skimage.transform import pyramid_reduce
import matplotlib.pyplot as plt
from Modimg import ModImg

import sys
from skimage import io

import pyimgur


url = sys.argv[1]
# url = "aaa"
# print(sys.argv)
img_sample = io.imread(url)

model = load_model('super-resolution/models/model_256.h5', custom_objects={'Subpixel':Subpixel})


x1_test = img_sample
# x1_test = cv2.imread('celeba-dataset\\train_f\\train_f\\f352743cdf535690.jpg')
img = ModImg(x1_test, 512, 2)
padded = img.getPadImg()
x1_test_resized = pyramid_reduce(padded, 2)

y_pred = model.predict(x1_test_resized.reshape((1, 256, 256, 3)))
y_pred = y_pred.reshape((512, 512, 3))
y_pred = (y_pred * 255).astype('uint8')
# y_pred = img.cutPadImg(y_pred)
y_pred = cv2.cvtColor(y_pred, cv2.COLOR_BGR2RGB)

cv2.imwrite('processed.jpg', y_pred)


print(url)

CLIENT_ID = "acd50197869043a"
PATH = './processed.jpg'

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH)

print(uploaded_image.link)



