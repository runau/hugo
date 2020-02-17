#!/bin/sh

dir_path="content/posts/*"
dirs=`find $dir_path -maxdepth 0 -type f -name 20200217*.md`

for dir in $dirs;
do
    echo $dir
    python create_meta_image.py $dir
done

hugo -t zzo_custom
