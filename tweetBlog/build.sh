#!/bin/sh

cp ./public/* ./public_bk/ -rp

dir_path="content/posts/*"
dirs=`find $dir_path -maxdepth 0 -type f -name $1*.md`

for dir in $dirs;
do
    echo $dir
    python create_meta_image.py $dir
done

hugo -t zzo_custom
cp ./content/posts/meta_image/* ./public/posts/meta_image/ -p
cp ./content/posts/img/* ./public/posts/img/ -p

rm ./public/*/*/index.json
rm ./public/*/index.json
rm ./public/index.json
python diff.py

aws s3 sync public s3://linebot-runauna/blog/
aws cloudfront create-invalidation --distribution-id E4NBTPF3DAIQ2 --paths "/blog/*"

d1=`date -d"$1" +%s`
d2=`date -d20200211 +%s`
date=`expr \( $d1 - $d2 \) / 86400`
echo 日数：$date
posts=`find public/posts -type f | grep .html | grep 2020 | wc -l`
echo 記事数：$posts

sed -e s/..日、..記事目/$date日、$posts記事目/ "content/_index_base.md" > "content/_index.md"
