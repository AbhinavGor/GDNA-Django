import datetime, json, itertools
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from ifsc_app.apps import ifsc_data, bank_leaderboard, stats

class IndexView(TemplateView):
    context = {
        "ifsc_data": ifsc_data
    }
    template_name = 'index.html'

def indexView(request, template_name="index.html"):
    args = {
        "ifsc_data": ifsc_data
    }

    return render(request, template_name, args)

def ifscRequest(request, ifsc_code):
    if(ifsc_code in bank_leaderboard.keys()):
        bank_leaderboard[ifsc_code]+=1
        stats.append({ifsc_code, datetime.datetime.now()})
    elif(ifsc_code in set(ifsc_data['IFSC'])):
        bank_leaderboard[ifsc_code] = 1
        stats.append({ifsc_code, datetime.datetime.now()})
    else:
        return JsonResponse({"error": "Invalid IFSC code " + ifsc_code})
    
    bank_data = ifsc_data.loc[ifsc_data["IFSC"] == ifsc_code].to_dict()
    response = {
        "bank": list(bank_data['BANK'].values())[0],
        "ifsc": list(bank_data['IFSC'].values())[0],
        "micr": list(bank_data['MICR'].values())[0],
        "branch": list(bank_data['BRANCH'].values())[0],
        "address": list(bank_data['ADDRESS'].values())[0],
        "city1": list(bank_data['CITY1'].values())[0],
        "city2": list(bank_data['CITY2'].values())[0],
        "state": list(bank_data['STATE'].values())[0],
        "std": list(bank_data['STD CODE'].values())[0],
        "phone": list(bank_data['PHONE'].values())[0],
    }

    response = json.dumps(response)

    return JsonResponse(response, safe=False)

def getLeaderboard(request, order, num_banks):
    if(order.upper() == "ASC"):
        sorted_dict = dict( sorted(bank_leaderboard.items(),
                           key=lambda item: item[1],
                           reverse=False))
    else:
        sorted_dict = dict( sorted(bank_leaderboard.items(),
                           key=lambda item: item[1],
                           reverse=True))
    
    if(num_banks):
        required_banks = dict(itertools.islice(sorted_dict.items(), num_banks))
    else:
        required_banks = dict(itertools.islice(sorted_dict.items(), 10))
    
    return JsonResponse(required_banks, safe=False)