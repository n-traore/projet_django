# -*- coding: utf-8 -*-

from django.shortcuts import render

# Vue pour la page index.html
def index(request):
    return render(request, "index.html")
