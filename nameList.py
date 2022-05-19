import timedate as td

# gerando nomes para selecionar arquivos de um mês especifico
def fileName():
    while True:
        year = input('Ano (2010-2019): ')
        if len(year) == 4: break
    while True:
        month = input('Mês (01-12): ')
        if len(month) == 2 and month != '0' and month != '00': break

    fileL = []

    for i in range(td.qdias(year, month)):
        i += 1
        if i < 10: fileL.append(year + month + '0' + str(i) + '.nc')
        if i > 9: fileL.append(year + month + str(i) + '.nc')

    return fileL, year, month