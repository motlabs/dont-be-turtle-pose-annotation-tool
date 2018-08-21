/* Copyright 2018 Jaewook Kang (jwkang10@gmail.com)
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
# code reference :  https://github.com/suriyasingh/pose-annotation-tool
*/


#include <stdio.h>
#include <iostream>
#include <fstream>
#include <opencv2/opencv.hpp>
#include <string.h>


#ifdef WINDOWS
#include <direct.h>
#define GetCurrentDir _getcwd
#else
#include <unistd.h>
#define GetCurrentDir getcwd
#endif

using namespace cv;
using namespace std;

#define JOINTS 4
#define NUM_USED_KEY 4



/* keyboard number */
int ESC     = 27;
int ENTER   = 13;
int SPACE   = 32;
int TAB     = 9;

int used_key[3] = {ESC, ENTER, SPACE};

/*
joint_points[][] =
{
    {x,y,occluded_flag},...
}
*/

int joint_points[JOINTS][3] = {-1};
int current_joint = -1;
int r[2], g[2], b[2];

char joints[JOINTS][20] =
{
    "head",
    "nose",
    "Rshoulder",
    "Lshoulder"
};


void CallBackFunc(int event, int x, int y, int flags, void* param)
{
	if (event == CV_EVENT_LBUTTONUP)
	{
		joint_points[current_joint][0] = x;
		joint_points[current_joint][1] = y;
		joint_points[current_joint][2] = 0;

		int occlusion = 0;
		Mat &img = *((Mat*)(param)); 
		circle(img, Point(joint_points[current_joint][0], joint_points[current_joint][1]), 10, Scalar(b[occlusion], g[occlusion], r[occlusion]), 3);
		imshow("image", img);
	}
	else if (event == CV_EVENT_RBUTTONUP)
	{
		joint_points[current_joint][0] = x;
		joint_points[current_joint][1] = y;
		joint_points[current_joint][2] = 1;

		int occlusion = 1;
		Mat &img = *((Mat*)(param));
		circle(img, Point(joint_points[current_joint][0], joint_points[current_joint][1]), 10, Scalar(b[occlusion], g[occlusion], r[occlusion]), 3);
		imshow("image", img);
	}

}

void init()
{
	r[0] = 0;
	g[0] = 255;
	b[0] = 255;

	r[1] = 255;
	g[1] = 0;
	b[1] = 255;
}

int main(int argc, char **argv)
{
	init();

	char cCurrentPath[FILENAME_MAX];
    char* image_subdir = (char*)argv[2];
    char* label_subdir = (char*)argv[3];

    // find absolute path  for  file read//
    GetCurrentDir(cCurrentPath, sizeof(cCurrentPath));
    cCurrentPath[sizeof(cCurrentPath) - 1] = '\0';
    printf("CurrentPath = %s\n",cCurrentPath);
    printf("Image import dirpath=%s\n",image_subdir);
    printf("Lable export dirpath=%s\n",label_subdir);
    printf("-----------------------------------\n");

	if(argc < 1)
	    printf("1:\tpath to list of images\n");

	Mat img;

	namedWindow("image",WINDOW_NORMAL);
	namedWindow("Progress",WINDOW_NORMAL);
	setMouseCallback("image", CallBackFunc, &img);

	FILE *fp_list = fopen(argv[1], "r");
	int key_pressed = 0;



	while(!feof(fp_list))
	{
	    char filename[100];
		fscanf(fp_list, "%s", filename);

        /* image import dir path */
        char path[FILENAME_MAX];
        strcpy(path, cCurrentPath);
        strcat(path, image_subdir);
        strcat(path, filename);


        printf("path = %s",path);

		img = imread(path);
		Mat progress = Mat::zeros(400, 150, CV_8UC3);

		current_joint = -1;
		for(int j = 0; j < JOINTS; j++)
		{
			joint_points[JOINTS][0] = -1;
			joint_points[JOINTS][1] = -1;
			joint_points[JOINTS][2] = -1;
		}

		imshow("image", img);
		imshow("Progress", progress);

        key_pressed =waitKey(0);
		if(key_pressed == SPACE)
		{
			fprintf(stderr, "\nSkipping : %s", path);
			printf("\n[SPACE] Skipping : %s", path);
			continue;
		}
		else if(key_pressed == ESC)
		{
			fprintf(stderr, "\nEXITING at %s\n", path);
			printf("\n[ESC] EXITING at %s\n", path);
			break;
		}
//		else if(key_pressed == ENTER)
        else
		{
			fprintf(stderr, "\nProcessing : %s", path);
			printf("\n[Enter] Processing : %s", path);
			//printf("\n[TAB] skip current annotation by your mouse click");
			//printf("\n[The other keys] save current annotation");


			for(int j=0; j<JOINTS; )
			{
				current_joint = j;
				putText(progress, joints[j], Point(10, 20+j*20), 1, 1, Scalar(255, 255, 255));

				imshow("image", img);
				imshow("Progress", progress);
				key_pressed = waitKey(0);

				int occlusion = joint_points[current_joint][2];

				if(key_pressed == TAB)
				{
				    fprintf(stderr, "\nSkip this part, set its value to -1 ");
			        printf("\nSkip this part, set its value to -1 ");

					joint_points[current_joint][0] = -1;
					joint_points[current_joint][1] = -1;
					joint_points[current_joint][2] = -1;

					putText(progress, "***********", Point(10, 20+j*20), 1, 1, Scalar(255, 255, 255));
					j++;
					imshow("Progress", progress);
				}
				else
				{
					circle(img, Point(joint_points[current_joint][0], joint_points[current_joint][1]), 10, Scalar(b[occlusion], g[occlusion], r[occlusion]), -1);
					j++;
				}
			}


            /* json file saving */

            /* label export dir path */
            char annotation_file_name[FILENAME_MAX];
            strcpy(annotation_file_name,cCurrentPath);
            strcat(annotation_file_name,label_subdir);
            strcat(annotation_file_name,filename);
            strcat(annotation_file_name,".json");

			fprintf(stderr, "\nSaving : %s", annotation_file_name);

			FILE *fp_annotation = fopen(annotation_file_name, "w");

            /* json format writting */
            fprintf(fp_annotation, "{\n");
            fprintf(fp_annotation, "\t \"image_path\": \"%s\",\n",path);
			for(int j=0; j<JOINTS; j++)
			{
			    if (j == JOINTS - 1)
                    fprintf(fp_annotation, "\t \"%s\": [ %d ,%d, %d ]\n",joints[j],joint_points[j][0], joint_points[j][1], joint_points[j][2]);
                else
                    fprintf(fp_annotation, "\t \"%s\": [ %d ,%d, %d ],\n",joints[j],joint_points[j][0], joint_points[j][1], joint_points[j][2]);

            }
            fprintf(fp_annotation, "}\n");
			fclose(fp_annotation);
			/* json writting end */
		}
//		else
//		{
//		    printf("\nkey pressed : %d", key_pressed);
//		    continue;
//		}
	}

	fclose(fp_list);
	return 0;
}