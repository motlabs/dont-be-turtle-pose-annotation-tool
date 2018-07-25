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
from subprocess import check_output
from glob import glob


HOME                    =  getcwd() + '/'
DATASET_PATH            = 'images_for_annotation/'
DATASET_TYPE            = 'YouTube_Pose_dataset_1.0/GT_frames'


def main():

    filelist_jpeg = glob(DATASET_PATH + DATASET_TYPE +'/*/*.jpeg')
    filelist_jpg  = glob(DATASET_PATH + DATASET_TYPE +'/*/*.jpg')
    filelist_png  = glob(DATASET_PATH + DATASET_TYPE +'/*/*.png')

    filelist = filelist_jpeg + filelist_jpg + filelist_png
    filepath = HOME + DATASET_PATH + DATASET_TYPE
    filelist.sort()

    for i in range(0,len(filelist)):
        filename =  filelist[i]
        filename_split = filename.split('/')

        filename_label= str(filename_split[-2])

        filename_split_split    = filename_split[-1].split('.')
        filename_extension      = filename_split_split[-1]
        temp                    = filename_split_split[-2].split('_')
        filename_num            = temp[-1]
        prefix                  = temp[-2]


        filerename = prefix + '_' + filename_label + '_' + str(filename_num) + '.' + filename_extension

        check_output('mv ' + HOME  + filename + ' ' + filepath +'/'+ filerename,shell=True)





if __name__ == "__main__":
    main()