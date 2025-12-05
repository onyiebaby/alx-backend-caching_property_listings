from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
# Create your views here.

def property_list(request): , @cache_page(60 * 15)
return JsonResponse({"", "properties", "data"})