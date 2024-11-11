from rest_framework.serializers import ValidationError


class LinkValidator:
    '''
        Проверка ссылок на сторонние ресурсы кроме youtube.com
    '''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = value.get(self.field)
        if url and not url.startswith('https://www.youtube.com/'):
            raise ValidationError('Допустимы ссылки только с youtube.com')
