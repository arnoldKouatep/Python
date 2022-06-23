from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def vue_de_test(request):
    return HttpResponse("<h1>Vue de test</h1>")

def index(request):
    return render(request, "DocBlog/index.html", context={"date":datetime.today()})