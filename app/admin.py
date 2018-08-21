import time

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *
from .util import *


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
                WineItem.objects.create(id=_id, wine_code=wc, security_code=sc, url=url, created_time=now(),
                                        batch_id=pk)

            queryset.update(is_gen=True)  # 生成完毕，更新匹配生成状态


gen_wine_items.short_description = '生成'


def view_wine_item(modeladmin, request, queryset):
    pk = queryset.all()[0].pk
    return redirect('/admin/app/wineitem?q=&batch__id__exact=' + str(pk))


view_wine_item.short_description = '查看'


class BatchAdmin(admin.ModelAdmin):
    list_display = ('created_time', 'batch_code', 'wine', 'count', 'is_gen', 'last_mod_time', 'sequence',)
    search_fields = ('batch_code', 'count')
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

    def get_export_headers(self):
        # 是你想要的导出头部标题headers
        return ['二维码地址', '核销验证码', '瓶身编号']

    # def dehydrate_full_title(self, wi):
    #     return '%s-%s'.format(wi.batch.wine.name, wi.batch.batch_code)


class WineItemAdmin(ImportExportModelAdmin):
    resource_class = WineItemResource
    search_fields = ('wine_code', 'security_code', 'batch.batch_code', 'w_user.phone',)
    list_display = (
        'wine_code', 'security_code', 'batch', 'w_user', 'status', 'count', 'first_visit_time', 'last_visit_time')
    list_filter = ('status', 'batch__wine', 'batch',)
    exclude = ('created_time',)
    sortable_by = ('-created_time',)


class WineUserAdmin(admin.ModelAdmin):
    search_fields = ('phone', 'wechat_id',)
    list_display = ('phone', 'wechat_id',)


class ActivityAdmin(admin.ModelAdmin):
    search_fields = ('name', 'pub_date', 'begin_date', 'end_date',)
    list_display = ('name', 'img', 'pub_date', 'begin_date', 'end_date',)


admin.site.register(Wine, WineAdmin)
admin.site.register(HomeAttach, HomeAttachAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(WineItem, WineItemAdmin)
admin.site.register(WineUser, WineUserAdmin)
admin.site.register(Activity, ActivityAdmin)
