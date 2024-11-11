from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    '''
        Кастомная Пагинация
    '''
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'  # Query parameter for changing page size
    max_page_size = 100  # Maximum allowed page size
