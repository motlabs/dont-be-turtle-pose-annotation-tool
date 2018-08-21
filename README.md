# pose-annotation-tool for dont be turtle proj

## About
This is an annotation tool for [the dont be turtle proj](https://github.com/motlabs/dont-be-turtle). 


## Installation

### Compiling
```bash
$ git clone https://github.com/motlabs/dont-be-turtle-pose-annotation-tool 
$ cmake CMakeLists.txt
```

### How to Use 

#### 1) Placing your dataset
Placing your dataset at `./images_for_annoation`.
For example, when we have the LSP dataset, the images are located at
```bash
$IMAGE_DIR=images_for_annotation/lsp_dataset/images
```

#### 2) Running the program
```bash
$ python run_annotation.py $IMAGE_DIR
```


#### 3) Starting Annotation
When running this program, two windows are popped up: 
- One shows the images that is currently annotating. 
- Another shows which keypoint is currently pointed.  

We can have three choices before starting the annotation:
```
- Press ENTER to annotate the current image
- Press SPACE to skip the current image
- Press D to remote the current image from the dataset.
```

Then the annotation is manipulated by the following:  
```
- Left Click: Visible joint
- Right Click: Occluded joint
- TAB: Current joint is not applicable for current image
- Any key: register the annotation and move to next joint
```

#### 4) Getting Results
The annotation results are formatted by a `JSON` format. 
For example,
```bash
{
	 "image_path": "./images_for_annotation/lsp_dataset/images/front_normal_10754.jpg",
	 "head": [ 248 ,127, 0 ],
	 "nose": [ 251 ,284, 0 ],
	 "Rshoulder": [ 87 ,406, 0 ],
	 "Lshoulder": [ 412 ,399, 0 ]
}

``` 

And, being recorded at
```bash
$LABEL_DIR=label_annotated/lsp_dataset/labels
```
> Note that one label json file is generated for one input image (one to one corresponding relation for the image and label).

## Code Reference
- [ https://github.com/suriyasingh/pose-annotation-tool]( https://github.com/suriyasingh/pose-annotation-tool )

## Feedback
- Jaewook Kang (jwkang@gmail.com)
