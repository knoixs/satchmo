# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext


def impressum(request):

    ctx = RequestContext(request, {
            'full_name': "Thomas Rega",
            'full_address': "Reinbeckstrasse 7, 12459 Berlin",
            'email': "thomas.rega@potstar.biz",
            'keywords': "Licht Design, leuchtende Blumentöpfe, Solarblumentopf",
            'telephone': "+49176 811 899 71",
            'title': "potstar - Licht- und Möbeldesign",
          })

    return render_to_response('impressum.html', ctx)


def index(request):
    ctx = RequestContext(request, {})
    return render_to_response('index.html', context_instance=ctx)
