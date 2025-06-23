from rest_framework.pagination import CursorPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination


class CustomCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'id'

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 50

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 50