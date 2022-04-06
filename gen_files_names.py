from email.mime import image
import os
import math

"""
This program reads the filenames in the given image directory, 
and writes three txt files (train, test, val) with the image filenames (without extension),
the porcentage defined goes to train file, and the rest is divided by two for test and validation.
These files are required for YOLOv3 retraining, 
they are the input for changing the labels files 
from pascal voc XML to the format required by YOLO v3
"""

filenames = os.listdir("VOCdevkit/VOC2022/JPEGImages/")
porcentage = 80

num_files = len(filenames)

num_files_in_1st_dir = (float(porcentage) / 100) * num_files
num_files_in_1st_dir = int(math.floor(num_files_in_1st_dir))
print("Total number of images: " + str(int(num_files)))
print("Number of files in train directory: " + str(num_files_in_1st_dir))


#img_files = []
#with open('2022_train.txt', 'a') as f:
#with open('2022_test.txt', 'a') as f:
#with open('2022_test.txt', 'a') as f:
f1 = open("train.txt", "a")
f2 = open("test.txt", "a")
f3 = open("val.txt", "a")

second_limit = num_files_in_1st_dir + int((num_files - num_files_in_1st_dir)/2)
print("second limit ", second_limit)
for count, img_filename in enumerate(filenames):
    img_file = img_filename.replace(".png", '')
    #img_files.append(img_file)
    if count < num_files_in_1st_dir:
        f1.write(img_file)
        f1.write('\n')
    elif count < second_limit:
        f2.write(img_file)
        f2.write('\n')
    else:
        f3.write(img_file)
        f3.write('\n')

#print(img_filename)
