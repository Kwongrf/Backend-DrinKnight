from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import json
from drinknight.models import User
from drinknight.models import DrinkData
from drinknight.models import DayDrinkData
from drinknight.models import MonthDrinkData
from drinknight.models import YearDrinkData
import datetime

def login(request,account,password):
    user = User.objects.filter(account=account, password=password)
    if not len(user) == 0:
        return HttpResponse('Success')
    else:
        return HttpResponse('Wrong Password or Account')

def register(request,account):
    user = User.objects.filter(account=account)
    if not len(user) == 0:
        return HttpResponse('Exist Account')
    else:
        user_data = json.loads(request.body)
        User.objects.create(user_data['account'],user_data['password'],user_data['userName'],
                            user_data['phoneNumber'],user_data['emailAddress'],user_data['height'],
                            user_data['weight'],user_data['age'],user_data['gender'])
        return HttpResponse('Create Account Successful')

#change or get user data
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
            user.phoneNumber = user_data['phoneNumber']
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
#get or add or change today's drinkdata
def handle_drink_data(request,account):
    today = datetime.date.today()
    if request.method == 'GET':
        #_account = request.GET.get('account')
        one_day_datas = DrinkData.objects.filter(account=account,time__year=today.year, time__month=today.month, time__day=today.day)
        one_day_dict = toDicts(one_day_datas)
        one_day_json = json.dumps(one_day_dict,ensure_ascii=False)
        updateData(account)
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
    updateData(account)
#update year and month and day drink data
def updateData(account):
    #update day data
    sum = 0
    today = datetime.date.today()
    one_day_datas = DrinkData.objects.filter(account=account, time__year=today.year, time__month=today.month,time__day=today.day)
    for d in one_day_datas:
        sum += d.dose
    day_data = DayDrinkData.objects.filter(account = account, date__year=today.year, date__month=today.month,date__day=today.day)
    if len(day_data) == 0:
        DayDrinkData.objects.create(account = account,date = today ,volume_dose = sum)
    else:
        day_data[0].volume_dose = sum
        day_data[0].save()

    #update month data
    sum = 0
    today = datetime.date.today()
    one_month_datas = DayDrinkData.objects.filter(account=account, date__year=today.year, date__month=today.month)
    for d in one_month_datas:
        sum += d.volume_dose
    month_data = MonthDrinkData.objects.filter(account=account, month__year=today.year, month__month=today.month)
    if len(month_data) == 0:
        MonthDrinkData.objects.create(account=account, month = today, volume_dose=sum)
    else:
        month_data[0].volume_dose = sum
        month_data[0].save()
    #update year data
    sum = 0
    today = datetime.date.today()
    one_year_datas = MonthDrinkData.objects.filter(account=account, month__year=today.year)
    for d in one_year_datas:
        sum += d.volume_dose
    year_data = YearDrinkData.objects.filter(account=account, year__year=today.year)
    if len(year_data) == 0:
        YearDrinkData.objects.create(account=account, year = today, volume_dose=sum)
    else:
        year_data[0].volume_dose = sum
        year_data[0].save()

def get_year_data(request,account,year):
    yd_arr = []
    year_datas = MonthDrinkData.objects.filter(account=account, month__year=year)
    for yd in year_datas:
        yd_arr.append(yd.toDict())
    year_sum = YearDrinkData.objects.filter(account=account, year__year=year)
    yd_dicts = {u'volume_dose': year_sum, u'details': yd_arr}
    yd_json = json.dumps(yd_dicts, ensure_ascii=False)
    return HttpResponse(yd_json)

def get_month_data(request,account,year,month):
    md_arr = []
    month_datas = DayDrinkData.objects.filter(account=account,date__year=year,date__month=month)
    for md in month_datas:
        md_arr.append(md.toDict())
    month_sum = MonthDrinkData.objects.filter(account=account, month__year=year, month__month=month)
    md_dicts = {u'volume_dose': month_sum, u'details': md_arr}
    md_json = json.dumps(md_dicts, ensure_ascii=False)
    return HttpResponse(md_json)

def get_day_data(request,account,year,month,day):
    dd_arr = []
    day_datas = DrinkData.objects.filter(account=account,time__year=year,time__month=month,time__day=day)
    for dd in day_datas:
        dd_arr.append(dd.toDict())
    day_sum = DayDrinkData.objects.filter(account=account,date__year=year,date__month=month,date__day=day)
    dd_dicts = {u'volume_dose':day_sum,u'details':dd_arr}
    dd_json=json.dumps(dd_dicts,ensure_ascii=False)
    return HttpResponse(dd_json)

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

def rank_day_data(request,account):
    today = datetime.date.today()
    rank_arr = []
    #at now we can just rank all users' data, not friends
    rank_users = DayDrinkData.objects.filter(date = today).order_by('-volume_dose')
    for obj in rank_users:
        rank_arr.append(obj.toDict())
    rank_json = json.dumps(rank_arr,ensure_ascii=False)
    return HttpResponse(rank_json)
