import locale

from django import template

from web_app.models import EventModel

from rolfing_django_project import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def date_period(context, event: EventModel):
    """ Glues dates to period like:  24 Nov 2023 - 10 Dec 2023 -> 24 Nov - 10 Dec 2023"""
    LC_TIME_STRINGS = {
        'ru': ('ru_RU.utf8', 'ru', 'Russian'),
        'en': ('en_US.utf8', 'en', 'English'),
    }

    lang_code = context.request.COOKIES.get('lang_code', settings.LANGUAGE_CODE.casefold())
    LC_TIME_formates = LC_TIME_STRINGS.get(lang_code)
    for formate in LC_TIME_formates:
        try:
            locale.setlocale(locale.LC_TIME, formate)
            break
        except:
            print(f'{__name__}.\nWrong {formate=}. Skipped.') if settings.DEBUG else None
            continue
    format = '%d %b %Y'
    start_date: str = event.start_date.strftime(format)
    end_date: str = event.end_date.strftime(format)
    ret = []
    start_date_split = start_date.split()
    end_date_split = end_date.split()
    for idx in range(2, -1, -1):
        if start_date_split[idx] == end_date_split[idx]:
            ret.append(start_date_split[idx])
        else:
            ret.extend([*end_date_split[idx::-1], '-', *start_date_split[idx::-1]])
            break

    return ' '.join(ret[::-1])
