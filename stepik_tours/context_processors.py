from tours.data import departures, description, subtitle, title


def header_proc(request):
    return {
        'departures': departures,
        'description': description,
        'subtitle': subtitle,
        'title': title,
    }
