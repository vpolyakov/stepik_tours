from django import template

register = template.Library()


@register.filter(name='star_multiply')
def star_multiply(value, arg: str = '★', sep: str = ' ') -> str:
    """
    Размножитель символов
    :param value: количество символов в пакете
    :param arg: повторяемый символ
    :param sep: разделитель между символами
    :return: пакет символов
    """
    return sep.join(arg * int(value))


@register.filter(name='from_depart')
def get_depart_city(depart_dict, city_id) -> str:
    from_city = depart_dict[city_id][0].lower() + depart_dict[city_id][1:]
    return from_city


@register.filter
def tour_min(dictionary, key):
    return min([dictionary[i][key] for i in dictionary])


@register.filter
def tour_max(dictionary, key):
    return max([dictionary[i][key] for i in dictionary])
