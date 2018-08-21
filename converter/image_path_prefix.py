import os, json
import shutil

source_path = "merged/dontbeturtle_dataset"
destination_path = "result/dontbeturtle_dataset"

img_prefix_path = "dontbeturtle_dataset/train"



source_anno_json_path = os.path.join(source_path, "ai_challenger_train.json")
destin_anno_json_path = os.path.join(destination_path, "ai_challenger_train.json")

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

if not os.path.exists(source_path):
    print("There is no path:", source_path)
make_dir(destination_path)


with open(source_anno_json_path) as f:
    anno_dict = json.load(f)


# json
new_images = []
for image_info in anno_dict["images"]:
    image_info["file_name"] = os.path.join(img_prefix_path, image_info["file_name"])
    new_images.append(image_info)

anno_dict["images"] = new_images

with open(destin_anno_json_path, 'w') as f:
    json.dump(anno_dict, f)


# images
with open(source_anno_json_path) as f:
    anno_dict = json.load(f)

source_images_path = os.path.join(source_path, "train")
destin_images_path = os.path.join(destination_path, "train")
make_dir(destin_images_path)
for img_info in anno_dict["images"]:
    img_filename = img_info["file_name"]

    source_img_path = os.path.join(source_images_path, img_filename)
    destin_img_path = os.path.join(destin_images_path, img_filename)

    shutil.copyfile(source_img_path, destin_img_path)

print(len(os.listdir(destin_images_path)))