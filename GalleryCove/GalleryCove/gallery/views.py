from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
import requests
import json
import urllib.parse


def index(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable
    page = request.GET.get('page', '1')

    try:
        page = int(page)
        if page == 0:
            page = 1
    except ValueError:
        page = 1

    query = request.GET.get('q', '')
    query = urllib.parse.quote_plus(query)

    if query == '':
        r = requests.get(
            f'https://api.artic.edu/api/v1/artworks?page={page}&limit=12&fields=id,title,image_id,thumbnail,artist_display')
    else:
        r = requests.get(
            f'https://api.artic.edu/api/v1/artworks/search?q={query}&page={page}&limit=12&fields=id,title,image_id,thumbnail,artist_display')

    if r.status_code == 403:
        return HttpResponseForbidden()
    res = r.json()

    data = r.json().get('data')
    end_index = res['pagination']['total_pages']

    if end_index <= 5:
        pages = list(range(1, end_index + 1))
    elif page <= 3:
        pages = [*list(range(1, page + 2)), '...', end_index]
    elif page >= end_index - 2:
        pages = [1, '...', *list(range(page - 1, end_index + 1))]
    else:
        pages = [1, "...", *list(range(page - 1, page + 2)), "...", end_index]

    page_obj = {
        'has_previous': page > 1,
        'has_next': page != res['pagination']['total_pages'],
        'previous_page_number': page - 1,
        "next_page_number": page + 1,
        'pages': pages,
        'number': page,
        'query': query
    }

    context = {'pictures': data, 'page_obj': page_obj}

    return render(request, 'gallery/index.html', context=context)
