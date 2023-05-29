from collections import OrderedDict

from base.sqlpaginator import SqlPaginator
from umra_va_xaj.settings import PER_PAGE
from umravaxajapp.models import Category


def format_ctg(data):
    return OrderedDict([

        ('id', data.id),
        ('name', data.name),
        ('short_description', data.short_description),
        ('slug', data.slug),

    ])


def paginated_ctg(requests):
    page = int(requests.GET.get('page', 1))
    ctg = Category.objects.all().order_by('-pk')

    limit = PER_PAGE
    offset = (page - 1) * limit

    result = []
    for x in range(offset, offset + limit):
        try:
            result.append(format_ctg(ctg[x]))
        except:
            break
    pag = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=len(ctg))
    meta = pag.get_paginated_response()

    return OrderedDict([
        ('result', result),
        ('meta', meta)
    ])
