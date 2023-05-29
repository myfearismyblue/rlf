from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class SwitchLanguageMiddleware(MiddlewareMixin):

    def process_request(self, request):
        lang_code = request.COOKIES.get('lang_code', '')

        if lang_code:
            translation.activate(lang_code)
            request.LANGUAGE_CODE = translation.get_language()

    def process_response(self, request, response):
        request.session['django_language'] = translation.get_language()
        if 'Content-Language' not in response:
            response['Content-Language'] = translation.get_language()
        translation.deactivate()

        return response
