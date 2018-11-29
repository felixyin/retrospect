#!/usr/bin/env bash



cd /root/retrospect/media/



# 查看一下大于150k的图片
echo '要优化的大于150k的图片：'
find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k



echo '正在压缩图片，可能需要点时间，请耐心等待~~~~'

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k -exec convert -resize 90%x90% {} {} \;



echo '优化后大于150k的图片：'
find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +150k


# 回到之前的目录
cd -


#for i in /root/retrospect/media/*.jpg; do jpegoptim $i; done

#pngcrush -brute -d "/root/retrospect/media/" *.png

