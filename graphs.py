import matplotlib.pyplot as plt

# def graphicLine(mr):
#     plt.plot(mr)
#     plt.show
#     plt.savefig('linha.png')
#     print("Arquivo 'linha.png' gerado com sucesso.")


def graphicBar(x, mr, year, month):
    plt.figure(figsize=(len(x), 8))
    plt.xticks(rotation=45)
    plt.title(f'{month} {year}')
    plt.ylabel('Reflectivity')
    plt.xlabel('Datetime')
    plt.bar(x, mr, color='blue')
    # plt.show
    plt.savefig(f'./img/{year}-{month}.png')
    print("Arquivo gerado com sucesso.")