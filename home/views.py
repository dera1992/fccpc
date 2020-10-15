# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


def dashboard(request):
    return render(request,'home/dashboard.html',)

def category_chart(request):
    return render(request, 'home/dashboard.html', )

def home_list(request):
    return render(request,'home/index.html',)

def ads_list(request):
    return render(request,'home/product_list.html',)

def allads_list(request):
    return render(request,'home/allads_list.html',)

def ad_detail(request):
    return render(request, 'home/detail.html',)

def login(request):
    return render(request, 'home/login.html',)

def register(request):
    return render(request, 'home/register.html',)

def favourite_delete(request):
    return render(request, 'home/bookmarked.html', )

def favourite_ads(request):
    return render(request, 'home/bookmarked.html', )

def delete_post(request):
    return render(request, 'home/bookmarked.html', )

def category_count(request):
    return render(request, 'home/footer.html',)

def send_message(request):
    return render(request, 'home/detail.html',)
