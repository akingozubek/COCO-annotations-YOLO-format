# COCO-annotations-YOLO-format

Collect COCO datasets for selected classes and convert Json annotations to YOLO format, write to txt files.

You must have annotations files especially instances annotations and it must be in Annotations directory.

If you have images, it must be in Images directory.
When finished processing, txt files in Labels directory.
when processing is done, you can find the txt files in the Labels folder.

file system:

````├──MAIN
    ├──Images
        images
    ├──Annotations
        annotations
    ├──Labels
        labels```



Commands
```-t or --type -> you must use this command for train or valid dataset.
-c or --classes -> you must use this command for select specify classes. it is your classes file.```

Using Commands:

```-t train``` or ```-t valid```
or

```--type train``` or ```--type valid```


```-c classes.txt```
or
```--classes classes.txt```


FOR EXAMPLE USES:

use train annotations and images, collect images and annotations for inside classes.txt
```Shell
python main.py -t train -c classes.txt```

use valid annotations and images, collect images and annotations for inside Labels/classes.names
```Shell
python main.py -t valid -c Labels/classes.names ```



```NOTES```

You can control with any annotation tools.

I controlled with labelImg.
https://github.com/tzutalin/labelImg

Also you can use
https://github.com/AlexeyAB/Yolo_mark

or another annotation tools.


```code work with instances_ annotations.```

```I use 2017 annotations in code, if you want use another annotations you must be change variable in collect_coco_images.py```


process is done, you can train YOLO models with images and labels files.

if you have any suggestion or question you can ask me.
I can answer your question as far as I know.
````
