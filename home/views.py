from django.shortcuts import render
from tweets.models import *
from django.http import HttpResponse, Http404, JsonResponse


def homeView(request, *args, **kwargs):
    context = {}
    return render(request, 'home/index.html', context,  status=200)


def tweetListView(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)


def tweetDetailView(request, id, * args, **kwargs):
    data = {
        'id': id,
    }
    status= 200
    try:
        obj = Tweet.objects.get(id=id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404
    return JsonResponse(data, status=status)
