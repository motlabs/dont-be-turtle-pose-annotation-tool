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
DATASET_TYPE            = 'train_set_croudworks/'


def main():

    filelist_jpeg = glob('**/**/**/*.jpeg')
    filelist_jpg  = glob('**/**/**/*.jpg')
    filelist_png  = glob('**/**/**/*.png')

    filelist = filelist_jpeg + filelist_jpg + filelist_png

    filepath = HOME + DATASET_PATH + DATASET_TYPE

    for i in range(0,len(filelist)):
        filename =  filelist[i]
        filename_split = filename.split('/')

        filename_num = int(filename_split[-2]) + i

        filename_split_split    = filename_split[-1].split('.')
        filename_extension      = filename_split_split[-1]
        filename_name_tmp       = filename_split_split[0]
        filename_name_temp_split= filename_name_tmp.split('_')
        filename_name           = filename_name_temp_split[0] + '_' +\
                                  filename_name_temp_split[1]

        filerename = filename_name + '_' + str(filename_num) + '.' + filename_extension

        check_output('mv ' + HOME  + filename + ' ' + filepath + filerename,shell=True)





if __name__ == "__main__":
    main()