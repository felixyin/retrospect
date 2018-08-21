from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic.detail import DetailView
from django.core.cache import cache
from django.http import HttpRequest
from django.utils.cache import get_cache_key
from dysms_python import demo_sms_send as ss
from .models import *
from .util import *


# Create your views here.


# 核销详情
class WineItemDetailView(DetailView):
    model = WineItem


# 扫码查看
def wine_item(request, id):
    wi = get_object_or_404(WineItem, id=id)
    wi.count += 1
    if wi.first_visit_time is None:
        wi.first_visit_time = now()
    wi.last_visit_time = now()
    wi.save()

    banners = HomeAttach.objects.all()

    # hx_status = request.session.get('hx_status')

    return render(request, 'app/show.html', {'wi': wi, 'banners': banners})


# 发送验证码
def get_verify_code(request):
    if request.is_ajax():
        phone = request.POST.get('phone')

        __business_id = uuid.uuid1()
        vc = str(veri_code())
        request.session['vc'] = vc

        params = "{\"code\":\"" + vc + "\",\"product\":\"xx\"}"
        result = {'Code': 'OK'}
        try:
            result = ss.send_sms(__business_id, phone, "珍柏追溯", "SMS_142510198", params)
        except Exception as e:
            pass

        return HttpResponse(result)
        # return HttpResponse(json.dumps({'result': result}))
        # return JsonResponse({'phone': phone, 'status': result.Code})


# 校验验证码
def verify_code(request):
    vc = request.session.get('vc')
    p_vc = request.POST['vc']
    if vc == p_vc:
        # 验证成功，第一次则写入数据库
        wine_item_id = request.POST['wine_item_id']
        wechat_id = request.POST['wechat_id']
        phone = request.POST['phone']
        (wu, is_created,) = WineUser.objects.get_or_create(phone=phone, wechat_id=wechat_id)
        wi = WineItem.objects.get(id__exact=wine_item_id)
        wi.w_user = wu
        wi.save()
        return JsonResponse({'status': True, 'msg': ''})
    return JsonResponse({'status': False, 'msg': '验证码不匹配'})


# 核销
def he_xiao(request):
    id = request.POST.get('id')
    security_code = request.POST.get('security_code')
    phone = request.POST.get('phone')

    wi = WineItem.objects.get(id__exact=id)
    if wi.security_code == security_code:
        # 保存和核销人
        wu = WineUser.objects.filter(phone=phone).all()[0]
        wi.w_user = wu
        wi.status = 'y'
        wi.save()
        # 清除页面缓存
        key = get_cache_key(request)
        if cache.has_key(key):
            cache.delete(key)
        # request.session['hx_status'] = '核销成功'
    # else:
    #     request.session['hx_status'] = '核销失败'

    return redirect(reverse('app:wine-item-detail', kwargs={'id': id}))
