from collections import OrderedDict

from base.sqlpaginator import SqlPaginator
from umra_va_xaj.settings import PER_PAGE
from umravaxajapp.models import Category, Contact


def format_contact(data):
    return OrderedDict([

        ('adress', data.adress),
        ('ishvaqti', data.ishvaqti),
        ('phone', data.phone),
        ('email', data.email),
        ('whatsup', data.whatsup)

    ])


def paginated_contact(requests):
    page = int(requests.GET.get('page', 1))
    contact = Contact.objects.all().order_by('-pk')

    limit = PER_PAGE
    offset = (page - 1) * limit

    result = []
    for x in range(offset, offset + limit):
        try:
            result.append(format_contact(contact[x]))
        except:
            break
    pag = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=len(contact))
    meta = pag.get_paginated_response()

    return OrderedDict([
        ('result', result),
        ('meta', meta)
    ])
