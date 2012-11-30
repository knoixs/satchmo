# -*- coding: utf-8 -*-
import glob
import os
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_noop as _


def impressum(request):

    ctx = RequestContext(request, {
            'description': _('Get the stars from the sky. potstar - LED - light design for indoors and outdoors.'),
            'email': "thomas.rega@potstar.biz",
            'full_address': "Reinbeckstrasse 7, 12459 Berlin",
            'full_name': "Thomas Rega",
            'keywords': _('Solar powered flower pots, LED flower pots, garden lighting, balcony lighting, garden party, solar Flowerpot, LED, lighting design'),
            'telephone': "+49 (0) 176 811 899 71",
            'title': "potstar - lighting and furniture design",
          })

    return render_to_response('impressum.html', ctx)


def index(request):
    ctx = RequestContext(request, {
        'keywords': _('Solar powered flower pots, LED flower pots, garden lighting, balcony lighting, garden party, solar Flowerpot, LED, lighting design'),
        'description': _('Get the stars from the sky. potstar - LED - light design for indoors and outdoors.'),
    })
    return render_to_response('index.html', context_instance=ctx)


def offers_and_prices(request):
    image_path_names = glob.glob(os.path.join(settings.EXAMPLE_IMAGE_PATH, '*.jpg'))
    imgs = []
    for img in image_path_names:
        imgs.append(img.split('/')[-1])

    ctx = RequestContext(request, {
        'image_path_names': imgs,
        'keywords': _('Solar powered flower pots, LED flowerpots, prices, deals'),
        'description': _('LED - light design for indoors and outdoors - prices and special offers.'),
    })

    return render_to_response('offers_and_prices.html', context_instance=ctx)
