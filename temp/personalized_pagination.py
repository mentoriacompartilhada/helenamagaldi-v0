from typing import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class MyPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'size'
    
    # {
    #     'page': 1,
    #     'size': 0,
    #     'total': 0,
    #     'items': []
    # }

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('total', self.page.paginator.count),
            ('size', len(data)),
            ('page', self.page.number),
            ('items', data)
        ]))

    