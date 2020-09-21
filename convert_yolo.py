# Import packages
import json
import os


# Convert bbox to yolo type annotations.
def convertYOLO(size: tuple, box: list) -> tuple:
    # Image height, width
    dw = 1./size[0]
    dh = 1./size[1]

    xmin = box[0]
    ymin = box[1]
    xmax = box[2] + box[0]
    ymax = box[3] + box[1]

    x = (xmin+xmax)*dw/2
    y = (ymin+ymax)*dh/2
    w = (xmax-xmin)*dw
    h = (ymax-ymin)*dh

    return (round(x, 3), round(y, 3), round(w, 3), round(h, 3))


# Coco annotations path
# https://cocodataset.org/#download

# Load json file
def annotation_data(annot_file: str) -> dict:

    with open(annot_file, 'r') as f:
        data = json.load(f)

    return data


def write_labels(classes: list, data: dict) -> None:
    # All your images list in images directory
    images = os.listdir("Images")

    # Required categories
    categories = [cat for cat in data["categories"]
                  if cat["name"] in classes]

    # Categories name
    classes = [class_["name"] for class_ in categories]

    # All COCO dataset images
    coco_images = [coco_img for coco_img in data["images"]]

    # Images matching the COCO dataset images
    matching_images = [
        match for match in coco_images if match["file_name"] in images]

    # Labels Path
    try:
        os.mkdir("Labels")
    except FileExistsError:
        print("Labels Directory Exists.")

    for img in matching_images:

        # Image features
        image_id = img['id']
        file_name = img['file_name']
        width = img['width']
        height = img['height']

        annoted_obj = filter(
            lambda x: x['image_id'] == image_id, data['annotations'])

        # Drop .jpg
        file_name = file_name.split(".")[0]

        # Create txt file and write annotations in it.
        with open(f'Labels/{file_name}.txt', 'w') as f:

            for img2 in annoted_obj:
                category_id = img2['category_id']

                obj_class = filter(
                    lambda x: x['id'] == category_id, categories)

                for item in obj_class:
                    name = item["name"]
                    class_id = classes.index(name)
                    bbox = img2['bbox']

                    annot = convertYOLO((width, height), bbox)

                    f.write(
                        f'{class_id} '
                        f'{" ".join([str(a) for a in annot])}\n')
