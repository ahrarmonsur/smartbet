from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Git off me properdee, ya doggone, goodfernuttin scoocher! (Just Kidding, I LOVE YOU <3)")
