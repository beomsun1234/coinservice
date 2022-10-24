from django.shortcuts import render
from django.http      import HttpResponse
from coinapp import coin_crw
import json
from django.core.serializers.json import DjangoJSONEncoder

def coin_price(request):

    jsonData = json.dumps(coin_crw.getCoinInfo(), ensure_ascii=False, cls=DjangoJSONEncoder)
    return HttpResponse(jsonData)

def hello(request):
    return HttpResponse("hello")

# Create your views here.
