from django import template

from web_app.models import EventModel

register = template.Library()


@register.simple_tag(takes_context=True)
def date_period(context, event: EventModel):
    """ Glues dates to period like:  24 Nov 2023 - 10 Dec 2023 -> 24 Nov - 10 Dec 2023"""
    format = '%d %b %Y'
    start_date:str = event.start_date.strftime(format)
    end_date:str = event.end_date.strftime(format)
    ret = []
    start_date_split = start_date.split()
    end_date_split = end_date.split()
    for idx in range(2,-1,-1):
        if start_date_split[idx] == end_date_split[idx]:
            ret.append(start_date_split[idx])
        else:
            ret.extend([*end_date_split[idx::-1], '-', *start_date_split[idx::-1]])
            break

    return ' '.join(ret[::-1])
