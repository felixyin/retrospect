#!/usr/bin/env bash

# 创建备份目录，如果不存在
mkdir /root/backup

send=`date '+%Y%m%d-%H%M%S'`

# 压缩media目录下用户上传的图片到备份目录，并按日期命名
tar -czvf  /root/backup/media-${send}.tar.gz /root/retrospect/media/

# 切换到项目根目录
cd /root/retrospect

# 覆盖本地的方式，检出代码
git fetch --all
git reset --hard origin/master
git pull

# 赋予updat命令权限（如果命令更新了，则权限会丢失）
sudo chmod 777 update.sh

# 收集静态文件，为nginx使用
python manage.py collectstatic

# 计算和生成数据库升级脚本
python manage.py makemigrations

# 执行数据库升级操作
python manage.py migrate

# 停止web服务
killall -9 uwsgi

# 启动web服务
nohup uwsgi --ini uwsgi.ini & ls

# 产看启动的集群进程，好放心
ps -ef | grep uwsgi



