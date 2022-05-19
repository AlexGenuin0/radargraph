# Quantos dias tem o mês
def qdias(year, month):
    for i in ['01', '03', '05', '08', '10', '12']:
        if month == i:
            return 31

    for i in ['04', '06', '07', '09', '11']:
        if month == i:
            return 30

    if month == '02':
        if int(year) % 100 == 0:
            if int(year) % 400 == 0:
                return 29
            return 28
        elif int(year) % 4 == 0:
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
    month = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    return month.get(m)