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
sudo chmod 777 zipimg.sh


# 压缩图片
zipimg


# 收集静态文件，为nginx使用
python manage.py collectstatic

# 免输入yes或no，默认yes
/usr/bin/expect <<-EOF
send "yes\n"
expect eof
EOF


# 计算和生成数据库升级脚本
python manage.py makemigrations


# 执行数据库升级操作
python manage.py migrate


# 停止和启动memcached缓存服务
systemctl restart memcached
systemctl status memcached


# 停止和启动web服务集群
killall -9 uwsgi
nohup uwsgi --ini uwsgi.ini & ls

# 停止和启动nginx
systemctl restart nginx
systemctl status nginx


# 产看启动的集群进程，好放心
ps -ef | grep uwsgi



