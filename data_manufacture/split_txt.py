#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob
from sklearn.model_selection import train_test_split

img_list = glob('/home/kobot/alpha_project/yolov5/dataset/images/*.jpg')

train_img_list, test_img_list = train_test_split(img_list,
                                                 test_size=0.1,
                                                 random_state=2000)

test_img_list, val_img_list = train_test_split(test_img_list,
                                               test_size=0.1,
                                               random_state=2001)

with open('/home/kobot/alpha_project/yolov5/dataset/train.txt', 'w') as f:
  f.write('\n'.join(train_img_list) + '\n')

with open('/home/kobot/alpha_project/yolov5/dataset/val.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')

with open('/home/kobot/alpha_project/yolov5/dataset/test.txt', 'w') as f:
  f.write('\n'.join(test_img_list) + '\n')
