from collections import OrderedDict

from base.sqlpaginator import SqlPaginator
from umra_va_xaj.settings import PER_PAGE
from umravaxajapp.models import SubCategory


def format_tarif(data):
    return OrderedDict([
        ('ID', data.id),
        ('ctg', data.ctg.name),
        ('city', data.city),
        ('tarif', data.tarif),
        ('date', data.date),
        ('muddati', data.muddati),
        ('menu', data.menu),
        ('distance', data.distance)
    ])


def paginated_tarif(requests):
    page = int(requests.GET.get('page', 1))
    tarif = SubCategory.objects.all().order_by('-pk')

    limit = PER_PAGE
    offset = (page - 1) * limit

    result = []
    for x in range(offset, offset + limit):
        try:
            result.append(format_tarif(tarif[x]))
        except:
            break
    pag = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=len(tarif))
    meta = pag.get_paginated_response()

    return OrderedDict([
        ('result', result),
        ('meta', meta)
    ])
