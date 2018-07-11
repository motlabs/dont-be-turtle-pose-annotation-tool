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

import cv2


HOME                    =  getcwd()
DATASET_PATH            = '/images_for_annotation/'
# DATASET_TYPE            = '/test_set_collected/'
# RESIED_DATASET_TYPE     = '/test_set_collected_resized/'
DATASET_TYPE            = '/train_set_croudworks5/'
RESIED_DATASET_TYPE     = '/train_set_croudworks5/'


RESIZE_HEIGHT = 640
RESIZE_WIDTH  = 480

# RESIZE_HEIGHT = 256
# RESIZE_WIDTH  = 256

def main():

    datapath            =  HOME + DATASET_PATH + DATASET_TYPE
    resized_datapath    =  HOME + DATASET_PATH + RESIED_DATASET_TYPE

    if not os.path.exists(resized_datapath):
        check_output('mkdir ' + resized_datapath, shell=True)

    filelist = listdir(datapath)
    try:
        filelist.remove('.DS_Store')
    except:
        print('No .DS_Store')

    for i in range(0,len(filelist)):

        filename = filelist[i]

        # read image
        img = cv2.imread(datapath + filename)
        # height, width = img.shape[:2]

        # resize
        resize_img = cv2.resize(img,(RESIZE_WIDTH,RESIZE_HEIGHT), interpolation=cv2.INTER_CUBIC)

        # write image
        cv2.imwrite(resized_datapath + filename, resize_img)

        # cv2.imshow('Original',img)
        # cv2.imshow('Resized',resize_img)
        # print ('filename = %s' % filename)
        # print('(height,width) = (%d,%d)' %(height, width))



if __name__ == "__main__":
    main()