import argparse
from zipfile import ZipFile
import os

import collect_coco_images
import convert_yolo


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--download", type=str, default=False,
                help="for download annotations, if you don't have annotations files use 'yes' arguments.")

ap.add_argument("-t", "--type", required=True,
                help="select for using image type for validation, train. use 'valid' or 'train' arguments.")

ap.add_argument("-c", "--category", required=True, nargs="+",
                help="select for using image categories. For Example: person or car dog cat")

args = vars(ap.parse_args())


def run():
    if args["download"] == "yes":
        collect_coco_images.download_annotation()

    annotation_file = collect_coco_images.annotations_type(
        args["type"], args["category"])
    data = convert_yolo.annotation_data(annotation_file)

    convert_yolo.write_labels(args["category"], data)


if __name__ == "__main__":
    run()
