import cv2, os, glob
import numpy as np
from keras.models import load_model
from Subpixel import Subpixel

base_path = 'celeba-dataset/processed'

x_test_list = sorted(glob.glob(os.path.join(base_path, 'x_test', '*.npy')))
y_test_list = sorted(glob.glob(os.path.join(base_path, 'y_test', '*.npy')))

model = load_model('models/model.h5', custom_objects={'Subpixel':Subpixel})

test_idx = 22

x1_test = np.load(x_test_list[test_idx])
y_pred = model.predict(x1_test.reshape((1, 44, 44, 3)))


x1_test = (x1_test * 255).astype(np.uint8)
y_pred = np.clip(y_pred.reshape((176, 176, 3)), 0, 1)

x1_test = cv2.cvtColor(x1_test, cv2.COLOR_BGR2RGB)
y_pred = cv2.cvtColor(y_pred, cv2.COLOR_BGR2RGB)
y_pred = (y_pred * 255).astype('uint8')

cv2.imwrite('test.jpg', y_pred)
