## dont-be-turtle format to COCO format converter

This scripts convert dont-be-turtle format(created from [dont-be-turtle-pose-annotation-tool](https://github.com/motlabs/dont-be-turtle-pose-annotation-tool)) to [COCO format](http://cocodataset.org/#format-data).

### Usage

#### 1. Install Pillow module 

```shell
pip install Pillow
```

#### 2. Set source dataset path and destination dataset path in `converter_cocoformat.py`

```python
source_path = "{source_path}"
destination_path = "{destination_path}"
```

#### 3. Run scripts

##### 3.1 Convert dont-be-turtle format to coco format

```shell
$ python converter_cocoformat.py
```

##### 3.2 Update image path on `ai_challenger_train.json` for prefix 

```shell
$ python image_path_prefix.py
```

### dont-be-turtle format(source format)

#### folder structure

```
dataset
  ├ images
    ├ front_normal_10629.jpg
    ├ front_normal_10630.jpg
  ├ labels
    ├ front_normal_10629.jpg.json
    ├ front_normal_10630.jpg.json
```

#### json format

```json
{
	 "image_path": "/Users/jwkangmacpro2/SourceCodes/dont-be-turtle-pose-annotation-tool/images_for_annotation/train_set_croudworks_640x480/train_set_croudworks1_640x480/front_normal_10629.jpg",
	 "head": [ 222 ,97, 0 ],
	 "nose": [ 227 ,429, 0 ],
	 "Rshoulder": [ 125 ,429, 0 ],
	 "Lshoulder": [ 320 ,433, 0 ]
}
```

### COCO format(destination format)

#### folder structure

```
dataset2
  ├ ai_challenger_train.json
  ├ train
    ├ front_normal_10629.jpg
    ├ front_normal_10630.jpg
```

#### COCO json format

```json
{
    "images": [
        {"file_name": "front_normal_192217.jpg", 
         "height": 640, 
         "width": 480, 
         "id": 192217}, 
        {"file_name": "left_sleep_192128.jpg", 
         "height": 640, 
         "width": 480, 
         "id": 192128}, 
        {"file_name": "front_turtle_220248.jpg", 
         "height": 640, 
         "width": 480, 
         "id": 220248}, 
        ...
    ],
    "annotations": [
        {"keypoints": [
        	230, 244, 2, 
        	234, 395, 2, 
        	125, 401, 2, 
        	328, 394, 2, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0], 
    	"area": 500000, 
    	"id": 192217, 
    	"image_id": 192217, 
    	"category_id": 1, 
    	"num_keypoints": 4
	}, {"keypoints": [
        	126, 352, 2, 
        	288, 347, 2, 
        	161, 365, 2, 
        	378, 298, 2, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0, 
        	0, 0, 0], 
        "area": 500000, 
        "id": 192128, 
        "image_id": 192128, 
        "category_id": 1, 
        "num_keypoints": 4
     }, {"keypoints": [
         	235, 382, 2, 
         	233, 430, 2, 
         	139, 427, 2, 
         	317, 429, 2, 
         	0, 0, 0, 
         	0, 0, 0, 
         	0, 0, 0, 
         	0, 0, 0, 
         	0, 0, 0, 
         	0, 0, 0, 
         	0, 0, 0, 
         	0, 0, 0, 
         	0, 0, 0, 
         	0, 0, 0], 
         "area": 500000, 
         "id": 220248, 
         "image_id": 220248, 
         "category_id": 1, 
         "num_keypoints": 4},
        ...
	]
    "categories": [{
        'supercategory': 'body',
        'name': 'up pose',
        'id': 1,
        'keypoints': ["head", "nose", "Rshoulder", "Lshoulder"],
        'skeleton': [[1, 2], [2, 3], [2, 4]]
    }]
}
```

## Components

#### converter_format.py

Convert dont-be-turtle format to COCO format.

#### image_path_prefix.py

```
"file_name": "front_turtle_14606.png"
```

to

```
"file_name": "prefix_somepath/front_turtle_14606.png"
```

on `ai_challenger_train.json`

### See also

- [motlabs/dont-be-turtle-pose-annotation-tool](https://github.com/motlabs/dont-be-turtle-pose-annotation-tool)
- [COCO dataset format](http://cocodataset.org/#format-data)