import os
import json


# Convert bbox to yolo type annotations.
def convertYOLO(size, box):
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

def annotation_data(annot_file):
    with open(annot_file, 'r') as f:
        data = json.load(f)
    return data


def write_labels(classes, data):
    # all your images list in images directory
    images = os.listdir("Images")
    categories = [i for i in data["categories"] if i["name"] in classes]

    classes = [i["name"] for i in categories]

    coco_images = [i for i in data["images"]]

    matching_images = [i for i in coco_images if i["file_name"] in images]

    for img in matching_images:
        image_id = img['id']
        file_name = img['file_name']
        width = img['width']
        height = img['height']

        annoted_obj = filter(
            lambda x: x['image_id'] == image_id, data['annotations'])

        # labels Path
        try:
            os.mkdir("Labels")
        except FileExistsError:
            pass

        with open(f'Labels/{file_name[:-4]}.txt', 'w') as f:
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
                        f'{class_id} {" ".join([str(a) for a in annot])}\n')

    with open("Labels/classes.txt", "w") as f:
        f.write("\n".join(classes))
