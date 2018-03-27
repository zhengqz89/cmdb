from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import models
from . import handler

# Create your views here.
@csrf_exempt
def report(request):
    if request.method == "POST":
        asset_data = request.POST.get("asset_data")
        data = json.loads(asset_data)
        if not data:
            return HttpResponse("没有数据")
        if not issubclass(dict, type(data)):
            return HttpResponse("数据格式不正确，必须为JSON")
        sn = data.get("sn")
        if sn:
            asset_obj = models.Asset.objects.filter(sn=sn)
            if asset_obj:
                pass
                return HttpResponse("资产数据已经更新")
            else:
                obj = handler.NewAsset(request, data)
                response = obj.add_to_new_assets_zone()
                return HttpResponse(response)
        else:
            return HttpResponse("没有资产sn序列号， 请检查数据!")
