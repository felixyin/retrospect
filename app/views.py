from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic.detail import DetailView

from dysms_python import demo_sms_send as ss
from .models import *
from .util import *


# Create your views here.


# 核销详情
class WineItemDetailView(DetailView):
    model = WineItem


def wine_item(request, id):
    wi = get_object_or_404(WineItem, id=id)
    wi.count += 1
    if wi.first_visit_time is None:
        wi.first_visit_time = now()
    wi.last_visit_time = now()
    wi.save()

    banners = HomeAttach.objects.all()

    return render(request, 'app/show.html', {'wi': wi, 'banners': banners})


# 发送验证码
def get_verify_code(request):
    if request.is_ajax():
        phone = request.POST.get('phone')
        print(phone)

        __business_id = uuid.uuid1()
        print(__business_id)
        vc = str(veri_code())
        request.session['vc'] = vc
        print(vc)

        params = "{\"code\":\"" + vc + "\",\"product\":\"xx\"}"
        result = {'Code': 'OK'}
        try:
            result = ss.send_sms(__business_id, phone, "阿里云短信测试专用", "SMS_142330060", params)
        except Exception as e:
            pass

        print(result)

        return HttpResponse(result)
        # return HttpResponse(json.dumps({'result': result}))
        # return JsonResponse({'phone': phone, 'status': result.Code})


# 校验验证码
def verify_code(request):
    vc = request.session['vc']
    print(vc)
    p_vc = request.POST['vc']
    if vc == p_vc:
        # // todo 记录数据库
        return JsonResponse({'status': True, 'msg': ''})
    return JsonResponse({'status': False, 'msg': '验证码不匹配'})


# 核销
def he_xiao(request):
    id = request.POST.get('id')
    security_code = request.POST.get('security_code')
    print(id)
    print(security_code)

    wi = WineItem.objects.get(id__exact=id)
    if wi.security_code == security_code:
        wi.status = 'y'
        wi.save()

    return redirect(reverse('app:wine-item-detail', kwargs={'id': id}))
