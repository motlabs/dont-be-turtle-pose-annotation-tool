# Copyright 2018 Jaewook Kang (jwkang10@gmail.com)
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===================================================================================
# -*- coding: utf-8 -*-

import os
from os import getcwd
from os import listdir
from subprocess import check_output

import argparse
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sp
import json
from PIL import Image

'''
    objective: 
        1) generation of json files corresponding to each img files
        2) generation of imagefile_list.txt

'''

HOME                    = getcwd() +'/'
DATASET_PATH            = 'images_for_annotation/'
DATASET_TYPE            = 'dontbeturtle/'
IMAGE_FILE_FOLDER_NAME  = 'youtubepose/'
LABEL_FILE_NAME         = 'youtube_joints.mat'

ANNOTATION_PATH         = 'label_annotated/'

# body part index of youtube pose
'''
0 Head, 
1 Right wrist, 
2 Left wrist, 
3 Right elbow, 
4 Left elbow, 
5 Right shoulder 
6 Left shoulder
'''
NOVALUE = -1.0
FILENUM_IN_FOLDER   = 100
FOLDER_NUM          = 50
IMAGE_MAX_VALUE     = 255

# keypoint index
HEAD        = 0
NOSE        = 1
R_SHOULDER  = 5
L_SHOULDER  = 6

is_image_plot = True


def main():
    # get image file path
    imag_data_path  = HOME + DATASET_PATH \
                           + DATASET_TYPE \
                           + IMAGE_FILE_FOLDER_NAME

    # loading label data
    label_data_path =   HOME + DATASET_PATH \
                             + DATASET_TYPE \
                             + LABEL_FILE_NAME

    json_label_path     = HOME + ANNOTATION_PATH \
                               + DATASET_TYPE

    if not os.path.exists(json_label_path):
        check_output('mkdir ' + json_label_path, shell=True)


    joints = sp.loadmat(label_data_path)
    img_file_list = listdir(imag_data_path)

    # sorting is very important!!
    img_file_list.sort()

    try:
        img_file_list.remove('.DS_Store')
    except:
        print('There are no .DS_Store')

    filecnt = 0
    for folder_cnt in range(0,FOLDER_NUM):
        print ('folder_cnt = %s' % folder_cnt)
        print ('----------------------------------')
        for file_index in range(0,FILENUM_IN_FOLDER):
            img_filename        = img_file_list[filecnt]
            img_filename_split  = img_filename.split('.')

            img_filename_split_split = img_filename_split[0].split('_')
            folder_index         = int(img_filename_split_split[1])

            print ('filecnt = %s' % filecnt)
            print ('file_index = %s' % file_index)
            print ('folder_index = %s' % folder_index)

            # extract (x,y)
            label_coord_x_head = joints['data'][0][folder_index][2][0][HEAD][file_index]
            label_coord_y_head = joints['data'][0][folder_index][2][1][HEAD][file_index]

            label_coord_x_nose = NOVALUE
            label_coord_y_nose = NOVALUE

            label_coord_x_rshoulder = joints['data'][0][folder_index][2][0][R_SHOULDER][file_index]
            label_coord_y_rshoulder = joints['data'][0][folder_index][2][1][R_SHOULDER][file_index]

            label_coord_x_lshoulder = joints['data'][0][folder_index][2][0][L_SHOULDER][file_index]
            label_coord_y_lshoulder = joints['data'][0][folder_index][2][1][L_SHOULDER][file_index]



            # append (x,y) data
            img_coor_head = []
            img_coor_head.append(label_coord_x_head)
            img_coor_head.append(label_coord_y_head)

            img_coor_nose = []
            img_coor_nose.append(label_coord_x_nose)
            img_coor_nose.append(label_coord_y_nose)


            img_coor_rshoulder = []
            img_coor_rshoulder.append(label_coord_x_rshoulder)
            img_coor_rshoulder.append(label_coord_y_rshoulder)

            img_coor_lshoulder = []
            img_coor_lshoulder.append(label_coord_x_lshoulder)
            img_coor_lshoulder.append(label_coord_y_lshoulder)


            dict_for_json ={}
            dict_for_json['image_path']   = imag_data_path + img_filename
            dict_for_json['head']       = img_coor_head
            dict_for_json['nose']       = img_coor_nose
            dict_for_json['Rshoulder']  = img_coor_rshoulder
            dict_for_json['Lshoulder']  = img_coor_lshoulder

            if is_image_plot == True:

                print ('image path = %s' % imag_data_path)
                print ('head = %s' % img_coor_head)
                print ('neck = %s' % img_coor_nose)
                print ('Rshoulder = %s' % img_coor_rshoulder)
                print ('Lshouder = %s' % img_coor_lshoulder)

                image = Image.open(imag_data_path+ img_filename)
                image = np.array(image).astype(np.uint8)

                image[int(label_coord_y_head),int(label_coord_x_head),0]= IMAGE_MAX_VALUE
                image[int(label_coord_y_head),int(label_coord_x_head),1]= IMAGE_MAX_VALUE
                image[int(label_coord_y_head),int(label_coord_x_head),2]= IMAGE_MAX_VALUE

                image[int(label_coord_y_lshoulder),int(label_coord_x_lshoulder),0]= IMAGE_MAX_VALUE
                image[int(label_coord_y_lshoulder),int(label_coord_x_lshoulder),1]= IMAGE_MAX_VALUE
                image[int(label_coord_y_lshoulder),int(label_coord_x_lshoulder),2]= IMAGE_MAX_VALUE


                image[int(label_coord_y_rshoulder),int(label_coord_x_rshoulder),0]= IMAGE_MAX_VALUE
                image[int(label_coord_y_rshoulder),int(label_coord_x_rshoulder),1]= IMAGE_MAX_VALUE
                image[int(label_coord_y_rshoulder),int(label_coord_x_rshoulder),2]= IMAGE_MAX_VALUE

                plt.imshow(image)
                plt.title(img_filename)
                plt.show()

            json_filename = json_label_path + \
                  IMAGE_FILE_FOLDER_NAME + \
                  img_filename + '.json'

            print ('json filename = %s' % json_filename)
            filecnt += 1

            with open(json_filename,'w') as fp:
                json.dump(dict_for_json,fp)


if __name__ == "__main__":
    main()
