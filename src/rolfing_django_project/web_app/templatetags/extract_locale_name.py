from typing import Optional

from cities_light.models import City
from django import template

from rolfing_django_project import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def extract_locale_name(context, city: City, lang_code: Optional[str] = None) -> str:
    """
    Extracts the first locale inclusion from django_citites_light db.
    Splits the field alternate_names with ; and finds the first locale occurrence.
    If not found returns name_ascii
    """
    CITIES_LIGHT_SPLITTER = ';'

    def _is_cyr_letter(c: str):
        assert len(c)
        cyr_ranges = {*list(range(1040, 1104)), 1025, 1105}  # 1040-1071, 1072-1103, 1025, 1105 А-Я, а-я, Ё, ё
        return ord(c[0]) in cyr_ranges

    def _is_latin_letter(c: str):
        assert len(c)
        lat_ranges = {*list(range(65, 91)), *list(range(97, 122))}  # A-Z, a-z
        return ord(c[0]) in lat_ranges

    # lang_code fetches from template or from cookies or default setting
    lang_code = lang_code or context.request.COOKIES.get('lang_code', '') or settings.LANGUAGE_CODE.casefold()

    validate_funcs = {
        'ru': _is_cyr_letter,
        'en': _is_latin_letter,
    }

    _is_in_local_alpha = validate_funcs[lang_code]

    alternative_names: str = str(city.alternate_names)
    alternative_names_as_list = alternative_names.split(CITIES_LIGHT_SPLITTER)
    for name in alternative_names_as_list[::-1]:  # reverse because somehow the best matches are the latest
        if _is_in_local_alpha(name[0]):
            return name
    return city.name_ascii
