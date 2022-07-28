from timedate import qdias


# gerando nomes para selecionar arquivos de um mês especifico
def fileName(datas):
    if datas[1] == '00000000':
        datas[1] = datas[0]
        di, mi, ai = int(datas[0][-2:]), int(datas[0][4:6]), int(datas[0][:4])
        df, mf, af = int(datas[1][-2:]), int(datas[1][4:6]), int(datas[1][:4])
    else:
        di, mi, ai = int(datas[0][-2:]), int(datas[0][4:6]), int(datas[0][:4])
        df, mf, af = int(datas[1][-2:]), int(datas[1][4:6]), int(datas[1][:4])

    if mf < 12: m, a= mf+1, af
    elif mf == 12:
        m = 1
        a = af+1

    fileL=[]
    while True:
        for n in range(1, 13):
            n += 1
            if n == mi:
                for d in range(1, (qdias(ai, mi)+1)):
                    if mi < 10:
                        if d < 10: fileL.append(str(ai) + '0' + str(mi) + '0' + str(d) + '.nc')
                        if d > 10: fileL.append(str(ai) + '0' + str(mi) + str(d) + '.nc')

                    if mi >= 10:
                        if d < 10: fileL.append(str(ai) + str(mi) + '0' + str(d) + '.nc')
                        if d >= 10: fileL.append(str(ai) + str(mi) + str(d) + '.nc')
                mi += 1
                if mi >= 13: mi = 1
            if ai == a and mi == m: break
        if ai == a and mi == m: break
        ai += 1

    pi = fileL.index(f'{datas[0]}.nc')
    pf = fileL.index(f'{datas[1]}.nc')+1
    return fileL[pi:pf]
