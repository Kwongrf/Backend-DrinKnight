from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from drinknight.models import User
from drinknight.models import DrinkData
import datetime



def handle_user_data(request, account):
    if request.method == 'POST' :
        #_account = request.POST.get('account')
        user = User.objects.get(account = account)
        user_data = json.loads(request.body)
        if not user_data['password'] == user.password :
            user.password = user_data['password']
        if not  user_data['userName'] == user.userName :
            user.userName = user_data['userName']
        if not  user_data['phoneNumber'] == user.phoneNumber :
            user.phoneNumber = user_data['password']
        if not  user_data['emailAddress'] == user.emailAddress :
            user.emailAddress = user_data['emailAddress']
        if not  user_data['height'] == user.height :
            user.height = user_data['height']
        if not  user_data['weight'] == user.weight :
            user.weight = user_data['weight']
        if not  user_data['age'] == user.age :
            user.age = user_data['age']
        if not  user_data['gender'] == user.gender :
            user.gender = user_data['gender']
        user.save()
    else:
        #_account = request.GET.get('account')
        user = User.objects.get(account=account)
        userJson = json.dumps(user.toDict(),ensure_ascii=False)
        return HttpResponse(userJson)

def handle_drink_data(request,account):
    today = datetime.date.today()
    if request.method == 'GET':
        #_account = request.GET.get('account')
        one_day_datas = DrinkData.objects.filter(account=account,time__year=today.year, time__month=today.month, time__day=today.day)
        one_day_dict = toDicts(one_day_datas)
        one_day_json = json.dumps(one_day_dict,ensure_ascii=False)
        return HttpResponse(one_day_json)
    else:
        drink_data = json.loads(request.body)
        data_obj = DrinkData.objects.get(account=account, time=drink_data['time'])
        if not data_obj == None:
            data_obj.dose = drink_data['dose']
        else:
            data_obj.account=account
            data_obj.time=drink_data['time']
            data_obj.dose= drink_data['dose']
            data_obj.save()


def toDicts(objs):
    obj_arr = []
    for o in objs:
        obj_arr.append(o.toDict())
    return obj_arr

def jsonAll(request):
    all_objs = User.objects.all()
    all_dicts = toDicts(all_objs)
    all_jsons = json.dumps(all_dicts, ensure_ascii=False)
    return HttpResponse(all_jsons)
