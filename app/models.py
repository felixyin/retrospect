import uuid

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models as m
from django.utils.timezone import now


# 基类
class BaseModel(m.Model):
    created_time = m.DateTimeField('创建时间', default=now(), editable=False)
    # last_mod_user = m.ForeignKey(User, on_delete=m.DO_NOTHING, verbose_name='更新人')
    last_mod_time = m.DateTimeField('修改时间', default=now(), editable=False)
    is_enable = m.BooleanField('是否启用', default=True)
    sequence = m.IntegerField('排列顺序', unique=True, null=True, blank=True, editable=False)

    # def save(self, *args, **kwargs):
    #     self.last_mod_user = User.objects.filter()
    #     super().save(*args, **kwargs)

    class Meta:
        abstract = True


class HomeAttach(m.Model):
    banner = m.ImageField('轮播图', upload_to='upload/home/banner/%y/%m/')


# Create your models here.
# 葡萄酒产品
class Wine(BaseModel):
    name = m.CharField('名称', max_length=50, blank=False)
    description = RichTextField(max_length=500, config_name='full', verbose_name='产品介绍')
    feature = RichTextField(max_length=500, config_name='full', verbose_name='产品特点')
    chateau_name = m.CharField('酒庄名称', max_length=50, blank=False)
    chateau = m.ImageField('酒庄介绍', upload_to='upload/wine/chateau/%Y/%m/')
    area_name = m.CharField('产区名称', max_length=50, blank=False)
    area = m.ImageField('产区介绍', upload_to='upload/wine/area/%Y/%m/')

    certificate = m.ImageField('原产地证', upload_to='upload/wine/cert/%y/%m/', default=None, null=True)
    element = RichTextField(max_length=50, config_name='mini', verbose_name='成分', default=None, null=True)

    sober_up_time_best = m.IntegerField('最佳醒酒时间', blank=False)

    sober_up_time1 = m.IntegerField('醒酒时间1', blank=False)
    sober_up_taste1 = m.TextField('口感1', max_length=50, blank=False)

    sober_up_time2 = m.IntegerField('醒酒时间2', blank=False)
    sober_up_taste2 = m.TextField('口感2', max_length=50, blank=False)

    sober_up_time3 = m.IntegerField('醒酒时间3', blank=False)
    sober_up_taste3 = m.TextField('口感3', max_length=50, blank=False)

    sober_up_time_worst = m.IntegerField('不易超过醒酒时间', blank=False)

    storage_mode = m.TextField('存放方式', max_length=30, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-last_mod_time', ]
        verbose_name = "红酒"
        verbose_name_plural = verbose_name


# 批次
class Batch(BaseModel):
    wine = m.ForeignKey(Wine, on_delete=m.DO_NOTHING)
    batch_code = m.UUIDField('批次编号', unique=True, default=uuid.uuid4(), blank=False, editable=False)
    count = m.IntegerField('生成数量', blank=False)
    is_gen = m.BooleanField('已经生成？', blank=False, editable=False, default=False)

    element = m.CharField('成分', max_length=50, default=None, null=True)
    agent_com = m.CharField('进口代理商', max_length=50, default=None, null=True)
    promise_book = m.ImageField('企业承诺书', upload_to='upload/batch/promise/%y/%m/', default=None, null=True)
    check_date = m.DateTimeField('检测日期', default=None, null=True)
    check_code = m.CharField('商检单号', max_length=30, default=None, null=True)
    check_prove = m.ImageField('检验检疫证明', upload_to='upload/batch/checkprove/%y/%m/', default=None, null=True)
    analyze_book = m.ImageField('成分分析证书', upload_to='upload/batch/analyze/%y/%m/', default=None, null=True)
    inspection_com = m.CharField('报检企业', max_length=50, default=None, null=True)

    bill_time = m.DateTimeField('报关时间', default=None, null=True)
    bill_code = m.CharField('报关单号', max_length=30, default=None, null=True)
    bill_img = m.ImageField('通关单', upload_to='upload/batch/bill/%y/%m/', default=None, null=True)
    bill_com = m.CharField('报关企业', max_length=30, default=None, null=True)

    def __str__(self):
        return "{0}:{1}".format(self.wine, self.count)

    class Meta:
        ordering = ['-last_mod_time', ]
        verbose_name = "批次"
        verbose_name_plural = verbose_name


# 核销信息
class WineItem(m.Model):
    id = m.UUIDField('主键', primary_key=True, blank=False, editable=False)
    wine_code = m.CharField('瓶身编码', blank=False, unique=True, max_length=15, default=None, editable=False)
    security_code = m.CharField('验证码', max_length=10, blank=False, editable=False)
    STATUS = (
        ('w', '未核销'),
        ('y', '已核销'),
    )
    status = m.CharField('核销状态', max_length=1, choices=STATUS, default='w')
    count = m.IntegerField('第几次访问？', blank=False, default=0, editable=False)
    created_time = m.DateTimeField('创建时间', blank=False, editable=False)
    first_visit_time = m.DateTimeField('第一次访问时间', null=True, editable=False)
    last_visit_time = m.DateTimeField('最后访问时间', null=True, editable=False)
    batch = m.ForeignKey(Batch, on_delete=m.CASCADE, editable=False)
    url = m.URLField('二维码地址', null=False, default=None)

    def __str__(self):
        return self.wine_code

    class Meta:
        ordering = ['-wine_code', ]
        verbose_name = "核销"
        verbose_name_plural = verbose_name


# 活动
class Activity(m.Model):
    name = m.CharField('活动名称', default=None, max_length=50, blank=False)
    img = m.ImageField(upload_to='upload/activity/%Y/')
    pub_date = m.DateTimeField('发布时间', blank=True, default=now())
    begin_date = m.DateTimeField('开始时间', blank=True, default=None)
    end_date = m.DateTimeField('结束时间', blank=True, default=None)

    def __str__(self):
        return '活动:{0}'.format(self.id)

    class Meta:
        ordering = ['-pub_date', ]
        verbose_name = "活动"
        verbose_name_plural = verbose_name


class TEst1(m.Model):
    name = m.CharField('活动名称', default=None, max_length=50, blank=False)
