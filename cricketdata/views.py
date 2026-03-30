from django.shortcuts import render
from .services.crickservice import crickservice_fun,crickservice_info
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
today=timezone.now().date()
# Create your views here.

def service_view(request):
    try:
        data=crickservice_fun('countries',0)
    except Exception as e:
        data={"error":str(e)}
    #return JsonResponse(data)
    return render(request,"home.html",data)
def serieslist_view(request):
    try:
        data=crickservice_fun('series',0)
    except Exception as e:
        data={"error":str(e)}
    #return JsonResponse(data)
    return render(request,"serieslist.html",data)

def series_info(request,id):
    try:
        data=crickservice_info('series_info',id)
        for match in data["data"]["matchList"]:
           match["date_obj"] = datetime.strptime(match["date"], "%Y-%m-%d").date()
        # value_date = datetime.strptime(data["date"], "%Y-%m-%d").date()
        # current_status=""
        # if value_date==today:
        #     current_status="live"
        # elif value_date > today:
        #      current_status="incoming on "+data["date"]
        # else:
        #     current_status=data["status"]
        # data["current_status"]=current_status

     
    except Exception as e:
        data={"error":str(e)}
    # return JsonResponse(data)
    return render(request,"series_info.html",data)
def match_info(request,id):
    try:
        data=crickservice_info('match_info',id)
     
    except Exception as e:
        data={"error":str(e)}
    #return JsonResponse(data)
    return render(request,"match_info.html",data)

def fantacyScorecard(request,id):
    try:
        data=crickservice_info('match_scorecard',id)
        mdata=data["data"]
        team_list = mdata.get("teamInfo", [])
        score_list = mdata.get("score", [])
        score_card_list=mdata.get("scorecard",[])

        for i, team in enumerate(team_list):
           if i < len(score_list):
             team["score"] = score_list[i]
             team["scorecard"]=score_card_list[i]
     
    except Exception as e:
        data={"error":str(e)}
    # return JsonResponse(mdata)
    return render(request,"fantacyscorecard.html",{"data":mdata})


def currentMatches_view(request):
    context={}
    try:
        data=crickservice_fun('currentMatches',0)
     
        
        print(context)

    except Exception as e:
        data={"error":str(e)}
    #return JsonResponse(data)
    return render(request,"currentmatches.html",data)