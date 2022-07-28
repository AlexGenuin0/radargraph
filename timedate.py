# Quantos dias tem o mês
def qdias(year, month):
    if month in [1, 3, 5, 8, 10, 12]: return 31
    if month in [4, 6, 7, 9, 11]: return 30
    if month == 2:
        if year % 100 == 0:
            if year % 400 == 0:
                return 29
            return 28
        elif year % 4 == 0:
            return 29
        else:
            return 28


# Faz uma lista com as horas do dia num intervalo de cinco minutos
def lhoras(mr):
    h, m = 0, 0
    horas = []
    for i in range(len(mr)):
        if i % 12 == 0 and i != 0: h += 1
        if h < 10:
            if m < 10:
                horas.append('0{}:0{}'.format(h, m))
            elif m > 9:
                horas.append('0{}:{}'.format(h, m))
        elif h > 9:
            if m < 10:
                horas.append('{}:0{}'.format(h, m))
            elif m > 9:
                horas.append('{}:{}'.format(h, m))

        if m >= 55:
            m = 0
        else:
            m += 5

    return horas


# Nomeia os meses
def monthName(m):
    m = int(m)
    month = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    return month.get(m)
