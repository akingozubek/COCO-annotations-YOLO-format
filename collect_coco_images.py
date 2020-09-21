import os
from zipfile import ZipFile

import requests
from pycocotools.coco import COCO


def collect_images(coco: object, categories: list) -> None:

    for category in categories:
        category_ids = coco.getCatIds(catNms=[category])
        if not category_ids:
            print(f'{category} is not in COCO dataset categories.')
            break

        image_ids = coco.getImgIds(catIds=category_ids)
        images = coco.loadImgs(image_ids)

        answer = input(
            f"Your selected category {category} has {len(images)} images."
            f"Do you want download those images?(y/n)")

        if answer.lower() == "y":

            try:
                os.mkdir("Images")
            except FileExistsError:
                print("Images Directory Exists.")

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
            print("Please select y/n")
            break


def annotations_type(annot_type: str, categories: list) -> str:

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

    else:
        return None
