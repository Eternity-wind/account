from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest

from acc_records.models import Account
from datetime import datetime
import json


# Create your views here.

def calibratorfunc(account_dataset):
    money = account_dataset.get('account_money')
    if not isinstance(money, int):
        return HttpResponseNotFound("money format error")

    content = account_dataset.get('account_content')
    if content is None:
        return HttpResponseBadRequest("content format error")

    # account_dataset.__contains__('account_datetime')
    if 'account_datetime' in account_dataset and isinstance(account_dataset['account_datetime'], str):
        try:
            day_time = datetime.strptime(account_dataset['account_datetime'], '%Y%m%d')
        except ValueError:
            return HttpResponseBadRequest("datetime format error")#400
    else:
        return HttpResponseNotFound("datetime error")
    return {
        'account_money': money,
        'account_content': content,
        'account_datetime': day_time}


def list_account_view(request):
    # for item in dir(request):
    #     print(f"{item}: {getattr(request, item)}")
    if request.method == 'GET':
        account_dataset = Account.objects.all()
        account_list = list(account_dataset.values())
        return JsonResponse({
            'list_account': account_list
        })
    elif request.method == 'POST':
        account_postdata = json.loads(request.body.decode("utf-8"))
        # 校验数据
        dict_accargs = calibratorfunc(account_postdata)
        databaseset = Account(**dict_accargs)
        databaseset.save()

        return JsonResponse({
            'operate': 'save data to database',
            'account_id': databaseset.account_id,
            'account_money': databaseset.account_money,
            'account_content': databaseset.account_content,
            'account_datetime': databaseset.account_datetime
        })


def detail_account_view(request, account_id):
    # 单条account详情，patch，delete此处实现，拿一条的
    if request.method == 'PATCH':
        account_patchdata = json.loads(request.body.decode("utf-8"))
        if not Account.objects.filter(pk=account_id).exists():
            return HttpResponseNotFound("PATCH Data not exits database")  # 404
        else:
            # 校验数据
            dict_accargs = calibratorfunc(account_patchdata)
            Account.objects.filter(pk=account_id).update(**dict_accargs)
            account_delete = Account.objects.get(pk=account_id)
            update_accdict = model_to_dict(account_delete)
        return JsonResponse(
            {
                'operate': 'update succeed',
                'account': update_accdict})

    elif request.method == 'DELETE':
        if not Account.objects.filter(account_id=account_id).exists():
            return HttpResponseNotFound("DELETE Data not exits database")#404
        # id = account_deletedata['account_id']
        account_delete = Account.objects.get(pk=account_id)
        delete_accdict = model_to_dict(account_delete)
        account_delete.delete()
        return JsonResponse({
            'operate': 'delete succeed',
            'account': delete_accdict
        })
    elif request.method == 'GET':
        if not Account.objects.filter(account_id=account_id).exists():
            return HttpResponseNotFound("query Data not exits database")#404
        account_query = Account.objects.get(pk=account_id)
        query_accdict = model_to_dict(account_query)
    return JsonResponse({
        'operate': 'query succeed',
        'account': query_accdict
    })
