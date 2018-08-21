#!/usr/bin/env bash


cd /root/retrospect/media/

# 查看一下大于300k的图片
find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k -exec convert -resize 90%x90% {} {} \;

find /root/retrospect/media/ -regex '.*\(jpg\|JPG\|png\|jpeg\)' -size +200k

cd ~


#for i in /root/retrospect/media/*.jpg; do jpegoptim $i; done

#pngcrush -brute -d "/root/retrospect/media/" *.png

