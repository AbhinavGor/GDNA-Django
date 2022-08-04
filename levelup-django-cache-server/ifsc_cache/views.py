import json
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
import requests
from ifsc_cache.apps import hit_count

def ifscResponse(request, ifsc_code):
    if(cache.get(ifsc_code)):
        hit_count
        bank_data = cache.get(ifsc_code)
        if(hit_count[ifsc_code]):
            hit_count[ifsc_code]+=1
        else:
            hit_count[ifsc_code] = 1
        print("hit cache")
    else:
        try:
            url = 'http://127.0.0.1:8000/ifsc/' + ifsc_code
            bank_data = requests.get(url)
            cache.set(ifsc_code, bank_data)
            print("hit db")
        except:
            return JsonResponse("error encountered")
    # print(json.dumps(bank_data))
    return HttpResponse(bank_data)

def getLeaderBoard(request, num_banks, order):
    try:
        url = 'http://127.0.0.1:8000/ifsc/'
        
        if(order):
            url += order + "/"
        else:
            url += "DESC/"
        
        if(num_banks):
            url += num_banks + "/"
        else:
            url += "10/"
        
        bank_leaderboard = requests.get(url)
    except:
        return JsonResponse("Error encountered")
    
    return JsonResponse(bank_leaderboard)