# COCO-annotations-YOLO-format

Collect COCO datasets for specific classes and Convert Json annotations to YOLO format in txt.

if you have annotations,it must be Annotations directory.
if you have images,it must be Images directory.


Commands
-t or --type-> you must use this command for train or valid dataset.
-c or --classes->you must use this command for select specify classes.
-d or --download->you can use download annotations.



Commands Using: 
-d yes
or
--download yes

this command use like it download annotations, 
it is optional if you not need download annotations, you can not use this command.

if you do not have Coco Annotations Files and you don't use -d command.
you can download this address annotations:
https://cocodataset.org/#download


I use 2017 annotations in code, if you want use another annotations you must be change variable in collect_coco_images.py




-t train or -t valid
or
--type train or --type valid

this command select use train dataset or valid dataset.


-c classes.txt
or
--classes classes.txt

this command, your classes files path.


FOR EXAMPLE USES:

python main.py -t train -c classes.txt -d yes

this commands:
download annotations, use train annotations and images, collect images and annotations for inside classes.txt



python main.py -t valid -c Labels/classes.txt 

this commands:
use valid annotations and images, collect images and annotations for inside classes.txt



You can control any annotation tools.
I controlled with labelImg.
https://github.com/tzutalin/labelImg

Also you can use
https://github.com/AlexeyAB/Yolo_mark

or another annotation tools.


if any suggestion or any question you can create issues.