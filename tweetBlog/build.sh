#!/bin/sh

dir_path="content/posts/*"
dirs=`find $dir_path -maxdepth 0 -type f -name 20200307*.md`

for dir in $dirs;
do
    echo $dir
    python create_meta_image.py $dir
done

hugo -t zzo_custom
cp ./content/posts/meta_image/* ./public/posts/meta_image/ -p
cp ./content/posts/img/* ./public/posts/img/ -p