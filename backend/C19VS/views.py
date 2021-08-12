from django.shortcuts import render
from django.http import HttpResponse
from .dbfunctions import *


def get_query(request, query):
    request = getQuery(query)
    return HttpResponse(request)


def delete_record(request, query):
    request = delete(query)
    return HttpResponse(request)


def edit_record(request, query):
    request = edit(query)
    return HttpResponse(request)


def create_record(request, query):
    request = create(query)
    return HttpResponse(request)
