## Media Converter

### Usage

#### 1. Prepare video files

#### 2. Install pillow and ffmpeg

```shell
$ pip install Pillow
$ brew install ffmpeg
```

#### 3. Configure your path and run scripts

##### 3.1 Wrap each video with new folder

```shell
$ python enclose_video.py
```

##### 3.2 Convert video to images

```
$ python split_video_to_images.py
```

##### 3.3 Create `annotation.json` which is COCO format json

```
$ python make_annotation_json.py
```

And then you can annotate and export by using [KeypointAnnotation](https://github.com/motlabs/KeypointAnnotation) on iOS device!

### Components

#### enclose_video.py

특정 폴더 안에 들어있는 비디오(`.mov`)를 찾고, 비디오 파일 이름으로 폴더를 만든 뒤, 해당 폴더 안에 각각의 비디오 파일을 이동시킨다.

from

```
dataset
 ├ video_001.mov
 ├ video_002.mov
 ├ video_003.mov
```

to

```
dataset
 ├ video_001
   ├ video_001.mov
 ├ video_002
   ├ video_002.mov
 ├ video_003
   ├ video_003.mov
```

#### split_video_to_images.py

각각 비디오 폴더 안에 있는 비디오를 이미지로 쪼게어서 images 폴더 안에 저장. 비디오는 삭제(optional)

from

```
dataset
 ├ video_001
   ├ video_001.mov
 ├ video_002
   ├ video_002.mov
 ├ video_003
   ├ video_003.mov
```

to

```
dataset
 ├ video_001
   ├ images
     ├ video_001_00001.jpeg
     ├ video_001_00002.jpeg
     ├ video_001_00003.jpeg
 ├ video_002
   ├ images
     ├ video_002_00001.jpeg
     ├ video_002_00002.jpeg
     ├ video_002_00003.jpeg
 ├ video_003
   ├ images
     ├ video_003_00001.jpeg
     ├ video_003_00002.jpeg
     ├ video_003_00003.jpeg
     ├ video_003_00004.jpeg
     ├ video_003_00005.jpeg
```

#### make_annotation_json.py

images 폴더 안에 있는 이미지들로 annotation.json 파일을 만듦.

frome

```
dataset
 ├ video_001
   ├ images
     ├ video_001_00001.jpeg
 ├ video_002
   ├ images
     ├ video_002_00001.jpeg
 ├ video_003
   ├ images
     ├ video_003_00001.jpeg
```

to

```
dataset
 ├ video_001
   ├ annotation.json
   ├ images
     ├ video_001_00001.jpeg
 ├ video_002
   ├ annotation.json
   ├ images
     ├ video_002_00001.jpeg
 ├ video_003
   ├ annotation.json
   ├ images
     ├ video_003_00001.jpeg
```

`annotation.json` 포맷

```
{
    "images": [{
    	"file_name": image_name,
		"height": img_height,
		"width": img_width,
		"id": image_id
    }, {
    	"file_name": image_name,
		"height": img_height,
		"width": img_width,
		"id": image_id
    }],
    "annotations": [],
    "categories": [{
    	'supercategory': 'hand',
        'name': 'fingertip',
        'id': 1,
        'keypoints': ["index", "index DIP", "index PIP", "index MP"],
        'skeleton': [[1, 2], [2, 3], [3, 4]]
     }]
}
```

