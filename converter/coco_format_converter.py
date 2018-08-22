import os, json
import shutil
from PIL import Image


source_path = "/Users/canapio/Project/machine learning/MoT Labs/dataset/dontbeturtle_custom_180820"
destination_path = "/Users/canapio/Project/machine learning/MoT Labs/dataset/converted/dontbeturtle_custom_180820"

""" Source Dataset 
dataset
  ├ images
    ├ front_normal_10629.jpg
    ├ front_normal_10630.jpg
  ├ labels
    ├ front_normal_10629.jpg.json
    ├ front_normal_10630.jpg.json
"""
""" Source Dataset JSON Format
{
	 "image_path": "/Users/jwkangmacpro2/SourceCodes/dont-be-turtle-pose-annotation-tool/images_for_annotation/train_set_croudworks_640x480/train_set_croudworks1_640x480/front_normal_10629.jpg",
	 "head": [ 222 ,97, 0 ],
	 "nose": [ 227 ,429, 0 ],
	 "Rshoulder": [ 125 ,429, 0 ],
	 "Lshoulder": [ 320 ,433, 0 ]
}
"""

""" Destination Dataset
dataset2
  ├ ai_challenger_train.json
  ├ train
    ├ front_normal_10629.jpg
    ├ front_normal_10630.jpg
"""
""" Destination Dataset JSON Format
{
    "images": [
        {"file_name": "front_normal_192217.jpg", "height": 640, "width": 480, "id": 192217}, 
        {"file_name": "left_sleep_192128.jpg", "height": 640, "width": 480, "id": 192128}, 
        {"file_name": "front_turtle_220248.jpg", "height": 640, "width": 480, "id": 220248}, 
        ...
    ],
    "annotations": [
        {"keypoints": [230, 244, 2, 234, 395, 2, 125, 401, 2, 328, 394, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "area": 500000, "id": 192217, "image_id": 192217, "category_id": 1, "num_keypoints": 4}, 
        {"keypoints": [126, 352, 2, 288, 347, 2, 161, 365, 2, 378, 298, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "area": 500000, "id": 192128, "image_id": 192128, "category_id": 1, "num_keypoints": 4}, 
        {"keypoints": [235, 382, 2, 233, 430, 2, 139, 427, 2, 317, 429, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "area": 500000, "id": 220248, "image_id": 220248, "category_id": 1, "num_keypoints": 4}],
        ...
    "categories": [{
        'supercategory': 'body',
        'name': 'up pose',
        'id': 1,
        'keypoints': ["head", "nose", "Rshoulder", "Lshoulder"],
        'skeleton': [[1, 2], [2, 3], [2, 4]]
    }]
}
"""

source_images_path = os.path.join(source_path, "images")
source_labels_path = os.path.join(source_path, "labels")

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def convert(source_labels_path, source_images_path, images_destination_path, annotation_json_path):
    annotation_dict = {
        "images": [],
        "annotations": [],
        "categories": [{
            'supercategory': 'body',
            'name': 'up pose',
            'id': 1,
            'keypoints': ["head", "nose", "Rshoulder", "Lshoulder"],
            'skeleton': [[1, 2], [2, 3], [2, 4]]
        }]
    }

    for filename in os.listdir(source_labels_path):
        label_path = os.path.join(source_labels_path, filename)

        # source_json_path = os.path.join(source_path, "annotation.json")
        if os.path.splitext(label_path.split("/")[-1])[1] != '.json':
            continue;

        with open(label_path) as f:
            label_dict = json.load(f)

        # label_dict.keys() : ['image_path', 'head', 'nose', 'Rshoulder', 'Lshoulder']
        image_filename = label_dict["image_path"].split("/")[-1]
        # img_id = int(os.path.splitext(image_filename)[0][2:])
        img_id = int(os.path.splitext(image_filename)[0].split("_")[-1])


        image_path = os.path.join(source_images_path, image_filename)


        if not os.path.exists(image_path):
            continue;

        im = Image.open(image_path)
        img_width, img_height = im.size  # (640, 480)#

        image_info = {
            "file_name": image_filename,
            "height": img_height,
            "width": img_width,
            "id": img_id
        }
        # print(image_info)


        # 'keypoints': [1205, 1611, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # 'area': 500000, 'id': 23, 'image_id': 23, 'category_id': 1, 'num_keypoints': 0, 'bbox': [0, 0, 0, 0]}
        keypoints = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]

        # 'head', 'nose', 'Rshoulder', 'Lshoulder'
        keypoints[3 * 0 + 0] = label_dict["head"][0]
        keypoints[3 * 0 + 1] = label_dict["head"][1]
        keypoints[3 * 0 + 2] = 2

        keypoints[3 * 1 + 0] = label_dict["nose"][0]
        keypoints[3 * 1 + 1] = label_dict["nose"][1]
        keypoints[3 * 1 + 2] = 2

        keypoints[3 * 2 + 0] = label_dict["Rshoulder"][0]
        keypoints[3 * 2 + 1] = label_dict["Rshoulder"][1]
        keypoints[3 * 2 + 2] = 2

        keypoints[3 * 3 + 0] = label_dict["Lshoulder"][0]
        keypoints[3 * 3 + 1] = label_dict["Lshoulder"][1]
        keypoints[3 * 3 + 2] = 2


        anno_info = {
            'keypoints': keypoints,
            'area': 500000,
            'bbox':[0,0,0,0],
            'id': img_id,
            'image_id': img_id,
            'category_id': 1,
            'num_keypoints': 4
        }

        annotation_dict['images'].append(image_info)
        annotation_dict['annotations'].append(anno_info)

        # copy image
        source_image_path = image_path
        destination_image_path = os.path.join(images_destination_path, image_filename)
        print(source_image_path)
        print(destination_image_path)
        shutil.copyfile(source_image_path, destination_image_path)

    with open(annotation_json_path, 'w') as f:
        json.dump(annotation_dict, f)

    print("convert success")
    print("images count     :", len(annotation_dict["images"]))
    print("annotations count:", len(annotation_dict["annotations"]))




make_dir(destination_path)

train_images_destination_path = os.path.join(destination_path, "images")

make_dir(train_images_destination_path)

train_annotation_json_path = os.path.join(destination_path, "annotation.json")


convert(source_labels_path,
        source_images_path,
        train_images_destination_path,
        train_annotation_json_path)
