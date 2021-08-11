from django.shortcuts import render
from django.http import HttpResponse
from .dbfunctions import *


def function(request):
    msg = "Hello World from Django!"
    results = get_Persons()
    return HttpResponse(results)


def get_query(request, query):
    request = getQuery(query)
    return HttpResponse(request)