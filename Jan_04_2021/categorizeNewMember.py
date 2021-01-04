def open_or_senior(data):
    categorized = []
    for d in data:
        if d[0]>= 55 and d[1]> 7:
            categorized.append('Senior')
        else:
            categorized.append('Open')
    return categorized
