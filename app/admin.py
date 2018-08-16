import random
import time

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *


# Register your models here.
class ChateauAttachInline(admin.TabularInline):
    model = ChateauAttach
    min_num = 1
    max_num = 5


class AreaAttachInline(admin.TabularInline):
    model = AreaAttach
    min_num = 1
    max_num = 5


class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_mod_time', 'sequence', 'is_enable')
    search_fields = ('name', 'description', 'feature')
    list_filter = ('is_enable',)
    exclude = ('created_time',)
    inlines = [ChateauAttachInline, AreaAttachInline]


class HomeAttachAdmin(admin.ModelAdmin):
    list_display = ['pk', 'banner', ]


# 按规则计算瓶身编码
def get_next_wine_code(max_code: int):
    begin = time.strftime("%y%m%d", time.localtime())
    max_code += 1
    max_code_str = str(max_code)
    end = max_code_str.zfill(6)
    return "{0}{1}".format(begin, end)


# 生成六位验证码
def veri_code():
    li = []
    for i in range(6):  # 循环6次,生成6个字符
        r = random.randrange(0, 5)  # 随机生成0-4之间的数字
        # if r == 1 or r == 4:  # 如果随机数字是1或者4时,生成0-9的数字
        num = random.randrange(0, 9)
        li.append(str(num))
        # else:  # 如果不是1或者4时,生成65-90之间的数字
        #     temp = random.randrange(65, 91)
        #     char = chr(temp)  # 将数字转化为ascii列表中对应的字母
        #     li.append(char)
    r_code = ''.join(li)  # 6个字符拼接为字符串
    #  print('\033[31;1m%s\033[0m' % r_code)
    return r_code  # 返回字符串


# 生成核销信息
def gen_wine_items(modeladmin, request, queryset):
    from django.contrib.sites.models import Site
    site = Site.objects.get_current().domain
    row_list = queryset.all()
    for row in row_list:
        count = row.count
        pk = row.pk
        is_gen = row.is_gen
        if not is_gen:
            max_line = WineItem.objects.order_by('-wine_code').first()
            max_wine_code = 1
            if max_line is not None:
                max_wine_code = int(max_line.wine_code[6:])
            for c in range(count):
                sc = str(veri_code())  # 验证码
                # wc = str(shortuuid.random(11))  # 核销编号
                wc = get_next_wine_code(max_wine_code)  # 核销编号
                max_wine_code += 1
                _id = str(uuid.uuid4())  # id、url加密
                url = site + reverse('app:wine-item-detail', kwargs={'id': _id, })  # 二维码url
                WineItem.objects.create(id=_id, wine_code=wc, security_code=sc, url=url, created_time=now(), batch_id=pk)

            queryset.update(is_gen=True)  # 生成完毕，更新匹配生成状态


gen_wine_items.short_description = '生成'


def view_wine_item(modeladmin, request, queryset):
    pk = queryset.all()[0].pk
    return redirect('/admin/app/wineitem?q=&batch__id__exact=' + str(pk))


view_wine_item.short_description = '查看'


class BatchAdmin(admin.ModelAdmin):
    list_display = ('created_time', 'batch_code', 'wine', 'count', 'is_gen', 'last_mod_time', 'sequence',)
    search_fields = ('batch_code', 'wine', 'count')
    list_filter = ('wine', 'is_gen',)
    exclude = ('created_time',)
    view_on_site = True

    actions = [gen_wine_items, view_wine_item]

    class Meta:
        editable = False


class WineItemResource(resources.ModelResource):
    class Meta:
        model = WineItem
        fields = ('url', 'security_code', 'wine_code',)


class WineItemAdmin(ImportExportModelAdmin):
    resource_class = WineItemResource
    search_fields = ('wine_code', 'security_code', 'batch',)
    list_display = ('wine_code', 'security_code', 'batch', 'status', 'count', 'first_visit_time', 'last_visit_time')
    list_filter = ('status', 'batch',)
    exclude = ('created_time',)
    sortable_by = ('-created_time',)


class ActivityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'pub_date', 'begin_date', 'end_date',)
    list_display = ('name', 'img', 'pub_date', 'begin_date', 'end_date',)


admin.site.register(Wine, WineAdmin)
admin.site.register(HomeAttach, HomeAttachAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(WineItem, WineItemAdmin)
admin.site.register(Activity, ActivityAdmin)
