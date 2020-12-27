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


@register.filter
def tour_min(dictionary, key):
    return min([dictionary[i][key] for i in dictionary])


@register.filter
def tour_max(dictionary, key):
    return max([dictionary[i][key] for i in dictionary])
