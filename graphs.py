import matplotlib.pyplot as plt
from timedate import monthName


# def graphLine(mr):
# #     plt.plot(mr)
# #     plt.show
# #     plt.savefig('linha.png')
# #     print("Arquivo 'linha.png' gerado com sucesso.")


def graphBar(x, mr, d, cell):
    if d[1][:4] == 0000 and d[1][4:6] == 00:
        y, m, yf, mf = d[0][:4], monthName(d[0][4:6]), d[0][:4], monthName(d[0][4:6])
    else:
        y, m, yf, mf = d[0][:4], monthName(d[0][4:6]), d[1][:4], monthName(d[1][4:6])

    plt.figure(figsize=(len(x), 8))
    plt.xticks(rotation=45)
    plt.title(f'{m} {y}/{mf} {yf}')
    plt.ylabel('Reflectivity')
    plt.xlabel('Datetime')
    plt.bar(x, mr, color='blue')
    # plt.show
    plt.savefig(f'./img/{cell} {m} {y}/{mf} {yf}.png')
    print("Arquivo gerado com sucesso.")
