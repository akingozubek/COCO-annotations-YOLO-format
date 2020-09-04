import os
from zipfile import ZipFile

import requests
from pycocotools.coco import COCO


def download_annotation():
    print("Annotations Downloaded Start")

    req = requests.get(
        "http://images.cocodataset.org/annotations/annotations_trainval2017.zip")

    try:
        os.mkdir("Annotations")
    except:
        pass
    with open("Annotations/annotations.zip", "wb") as f:
        f.write(req.content)

    print("Download Complete")

    with ZipFile("Annotations/annotations.zip", "r") as f:
        f.extractall()
    print("Extract Zip")


def collect_images(coco, categories):

    for category in categories:
        category_ids = coco.getCatIds(catNms=[category])
        if not category_ids:
            print(f'{category} is not in COCO dataset categories.')
            continue
        image_ids = coco.getImgIds(catIds=category_ids)
        images = coco.loadImgs(image_ids)

        answer = input(
            f"Your selected category {category} has {len(images)} images Do you want download those images?(y/n)")

        if answer.lower() == "y":

            try:
                os.mkdir("Images")
            except FileExistsError:
                pass

            for img in images:
                img_name = img['file_name']

                if not os.path.exists(f'Images/{img_name}'):

                    img_data = requests.get(img['coco_url']).content

                    with open(f'Images/{img_name}', 'wb') as f:
                        print(f"{img_name} Downloaded")
                        f.write(img_data)

                else:
                    print(f"{img_name} is exists")

        elif answer.lower() == "n":
            continue

        else:
            break


def annotations_type(annot_type, categories):

    if annot_type == "train":

        annot = "Annotations/instances_train2017.json"
        coco = COCO(annot)
        collect_images(coco, categories)

        return annot

    elif annot_type == "valid":

        annot = "Annotations/instances_val2017.json"
        coco = COCO(annot)
        collect_images(coco, categories)

        return annot
