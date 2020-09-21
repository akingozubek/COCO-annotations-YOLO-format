#import packages
import argparse
import os

import collect_coco_images
import convert_yolo

ap = argparse.ArgumentParser()

ap.add_argument("-t", "--type", required=True,
                help="""
                Select for using image 
                type for validation or train.
                Use 'valid' or 'train' arguments.
                """)

ap.add_argument("-c", "--classes", required=True,
                help="""
                Select for using image categories files.
                Use a class file path.
                """)

args = vars(ap.parse_args())


def run() -> None:
    try:
        with open(args["classes"], "r") as f:
            categories = f.read().splitlines()

        annotation_file = collect_coco_images.annotations_type(
            args["type"], categories)

        if annotation_file:

            data = convert_yolo.annotation_data(annotation_file)

            convert_yolo.write_labels(categories, data)

    except FileNotFoundError:
        print("Classes File Not Exists.")


if __name__ == "__main__":
    run()
