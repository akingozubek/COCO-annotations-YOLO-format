# COCO-annotations-YOLO-format

Collect COCO datasets for specific classes and Convert Json annotations to YOLO format in txt.

if you have annotations,it must be Annotations directory.
if you have images,it must be Images directory.

file system:
```Shell
├──MAIN
    ├──Images
        images
    ├──Annotations
        annotations
    ├──Labels
        labels
```



Commands
```
-t or --type-> you must use this command for train or valid dataset.
-c or --classes->you must use this command for select specify classes.
-d or --download->you can use download annotations.
```


Commands Using: 

-d/--download command use for download annotations, 
it is optional.
if you not need download annotations, you maybe not use this command.

```Shell
-d yes
```
or
```Shell
--download yes
```

if you do not have Coco Annotations files and you don't use -d command.
you can download this address annotations:
https://cocodataset.org/#download


code work with instances_ annotations.

I use 2017 annotations in code, if you want use another annotations you must be change variable in collect_coco_images.py


-t/--type command select use train dataset or valid dataset.

```Shell
-t train or -t valid
```
or
```Shell
--type train or --type valid
```


-c/--classes your classes files path.
```Shell
-c classes.txt
```
or
```Shell
--classes classes.txt
```

FOR EXAMPLE USES:

download annotations, use train annotations and images, collect images and annotations for inside classes.txt
```Shell
python main.py -t train -c classes.txt -d yes
```


use valid annotations and images, collect images and annotations for inside Labels/classes.txt
```Shell
python main.py -t valid -c Labels/classes.txt 
```


You can control with any annotation tools.

I controlled with labelImg.
https://github.com/tzutalin/labelImg

Also you can use
https://github.com/AlexeyAB/Yolo_mark

or another annotation tools.


 process is done, you can train YOLO models with images and labels files.

if you have any suggestion or question you can create issues.