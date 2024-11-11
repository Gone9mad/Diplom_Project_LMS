from rest_framework import pagination

class CastomTestingPaginators(pagination.BasePagination):
    page_size = 5  # Default page size
    page_size_query_param = 'page_size'  # Query parameter for changing page size
    max_page_size = 10  # Maximum allowed page size
