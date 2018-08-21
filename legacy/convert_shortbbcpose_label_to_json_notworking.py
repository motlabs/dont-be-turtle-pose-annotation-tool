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
DATASET_TYPE            = 'YouTube_Pose_dataset_1.0/'
IMAGE_FILE_FOLDER_NAME  = 'images/'
LABEL_FILE_NAME         = 'joints.mat'

ANNOTATION_PATH         = 'label_annotated/'

# body part index
'''
0 Right ankle
1 Right knee
2 Right hip
3 Left hip
4 Left knee
5 Left ankle
6 Right wrist
7 Right elbow
8 Right shoulder
9 Left shoulder
10 Left elbow
11 Left wrist
12 Neck (actually we annotatge neck instead of neck)
13 Head top
'''

HEAD        = 13
NECK        = 12 # actually nose
R_SHOULDER  = 8
L_SHOULDER  = 9

is_image_plot = False

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

    # (x,y,v)

    label_coord_x_head  =   joints['data'][0][0][0][HEAD]
    label_coord_x_head  =   joints['data'][0][0][1][HEAD]


    label_coord_x_neck  =   joints['joints'][0][NECK]
    label_coord_y_neck  =   joints['joints'][1][NECK]

    label_coord_x_rshoulder  =   joints['joints'][0][R_SHOULDER]
    label_coord_y_rshoulder  =   joints['joints'][1][R_SHOULDER]

    label_coord_x_lshoulder  =   joints['joints'][0][L_SHOULDER]
    label_coord_y_lshoulder  =   joints['joints'][1][L_SHOULDER]


    try:
        img_file_list.remove('.DS_Store')
    except:
        print('There are no .DS_Store')

    for i in range(0,len(img_file_list)):
        img_filename = img_file_list[i]
        img_filename_split = img_filename.split('.')

        img_index = int(img_filename_split[0][2:6])
        print('img_index = %s' % img_index)

        img_coor_head = []
        img_coor_head.append(label_coord_x_head[img_index-1])
        img_coor_head.append(label_coord_y_head[img_index-1])
        img_coor_head.append(label_coord_v_head[img_index-1])

        img_coor_neck = []
        img_coor_neck.append(label_coord_x_neck[img_index-1])
        img_coor_neck.append(label_coord_y_neck[img_index-1])
        img_coor_neck.append(label_coord_v_neck[img_index-1])


        img_coor_rshoulder = []
        img_coor_rshoulder.append(label_coord_x_rshoulder[img_index-1])
        img_coor_rshoulder.append(label_coord_y_rshoulder[img_index-1])
        img_coor_rshoulder.append(label_coord_v_rshoulder[img_index-1])

        img_coor_lshoulder = []
        img_coor_lshoulder.append(label_coord_x_lshoulder[img_index-1])
        img_coor_lshoulder.append(label_coord_y_lshoulder[img_index-1])
        img_coor_lshoulder.append(label_coord_v_lshoulder[img_index-1])


        dict_for_json ={}
        dict_for_json['image_path']   = imag_data_path + img_filename
        dict_for_json['head']       = img_coor_head
        dict_for_json['neck']       = img_coor_neck
        dict_for_json['Rshoulder']  = img_coor_rshoulder
        dict_for_json['Lshoulder']  = img_coor_lshoulder

        if is_image_plot == True:

            print ('image path = %s' % imag_data_path)
            print ('head = %s' % img_coor_head)
            print ('neck = %s' % img_coor_neck)
            print ('Rshoulder = %s' % img_coor_rshoulder)
            print ('Lshouder = %s' % img_coor_lshoulder)

            image = Image.open(imag_data_path+ img_filename)
            image = np.array(image).astype(np.uint8)

            plt.imshow(image)
            plt.title(img_filename)
            plt.show()





        with open(json_label_path + img_filename + '.json','w') as fp:
            json.dump(dict_for_json,fp)

if __name__ == "__main__":
    main()
