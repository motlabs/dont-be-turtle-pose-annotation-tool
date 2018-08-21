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
import random

from subprocess import check_output
import argparse


PROJ_HOME_DIR   = getcwd()
DEFAULT_IMAGE_INPUT_DIR     = '/image_for_annotation'
DEFAULT_LABEL_OUTPUT_DIR    = '/label_annotated'


'''
    1) get $IMAGE_DIR
    2) mkdir $LABEL_DIR
    3) generate image file list
    4) run pose_annotation tool
    5) add image remove function to pose_anntation tool
'''

def create_label_folder(imagedir):

    imagedir_split_list = imagedir.split('/')

    if imagedir_split_list[-1] == 'images':
        labeldir = '/'.join(imagedir_split_list[2:-1]) + '/labels'

    else:
        labeldir = '/'.join(imagedir_split_list[2:])


    labeldir =  DEFAULT_LABEL_OUTPUT_DIR + '/' + labeldir
    # print 'labeldir = %s' % labeldir

    if not os.path.exists(PROJ_HOME_DIR + labeldir):
        check_output('mkdir ' + PROJ_HOME_DIR + labeldir,shell=True)

    return labeldir





def gen_image_filelist(imagedir,samplenum=None):

    filelist = listdir(imagedir)
    filelist.sort()

    try:
        filelist.remove('.DS_Store')
    except:
        print('No .DS_Store')

    if samplenum == None:
        samplenum = len(filelist)


    print('[gen_image_filelist] Dataset path: %s' % imagedir)
    if int(samplenum) < len(filelist):
        picked_filelist = random.sample(set(filelist),int(samplenum))
        print('[gen_image_filelist] Randomly sample %s samples from set' % samplenum)
    else:
        picked_filelist = filelist
        print('[gen_image_filelist] Randomly sample %s samples from set' % len(filelist))

    filename = '/'.join(imagedir.split('/')[:-1]) + '/images_filelist.txt'

    with open(filename,'w') as fp:
        for i in range(0,len(picked_filelist)):
            fp.write(picked_filelist[i] + '\n')

    return filename



def run_pose_anno_tool(imagedir,labeldir,image_filelistname):


    imagedir = imagedir + '/'
    labeldir = labeldir + '/'

    print ('[run_pose_anno_tool] imagedir = %s' % imagedir)
    print ('[run_pose_anno_tool] labeldir = %s' % labeldir)
    print ('[run_pose_anno_tool] image_filelistname = %s' % image_filelistname)

    cmd = './pose_annotation_tool ' + image_filelistname + ' ' \
                                    + imagedir           + ' ' \
                                    + labeldir
    proc_list = check_output(cmd, shell=True)

    print proc_list




if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--imagedir',
        default=DEFAULT_IMAGE_INPUT_DIR,
        help='dir path for input image data',
        nargs='+',
        required=False
    )

    args= parser.parse_args()
    imagedir = '/' + '/'.join(args.imagedir[0].split('/')[1:-1])

    labeldir            = create_label_folder(imagedir=imagedir)
    image_globaldir     = PROJ_HOME_DIR + imagedir

    imagestxt_filename = gen_image_filelist(imagedir=image_globaldir)
    run_pose_anno_tool(imagedir=imagedir,
                       labeldir=labeldir,
                       image_filelistname = imagestxt_filename)





