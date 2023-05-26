#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import glob
# from sklearn.model_selection import train_test_split

img_list = glob('/home/kobot/alpha_project/yolov5/dataset/images/*.jpg')

# print(img_list)
for file_name in img_list:
    # print(file_name)
    file_name = file_name.split('/')[7] # 경로 삭제 후 파일명 추출

    file_labels = file_name.split('_') # age, gender split
    age = int(file_labels[0]) 
    gender = int(file_labels[1])

    age_div_ten = age//10
    if (age_div_ten == 0 or age_div_ten == 1 or age_div_ten == 2 or age_div_ten == 3): # 00-39
        age_div_ten = 0
    elif (age_div_ten == 4 or age_div_ten == 5): # 40-59
        age_div_ten = 1
    elif (age_div_ten == 6 or age_div_ten == 7 or age_div_ten == 8 or age_div_ten == 9): # 60-100
        age_div_ten = 2

    if gender == 0:
        content = str(age_div_ten) + " 0.5 0.5 1 1"
    elif gender == 1:
        content = str(age_div_ten+3) + " 0.5 0.5 1 1"

    file_name = file_name[:-4] # .jpg 삭제
    with open('/home/kobot/alpha_project/yolov5/dataset/labels/' + file_name + '.txt', 'w') as f:
        print(content)
        f.write(content)