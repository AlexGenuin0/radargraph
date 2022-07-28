import numpy as np


def avgReflectivity(reflectivity_ds, cell):

    xmulti = int(cell[0])          # 1-10
    ymulti = int(cell[1])          # 1-10

    # dimensão de cada celula
    xlabel = reflectivity_ds.x.size/10
    ylabel = reflectivity_ds.y.size/10

    # inicio e fim do x da célula
    init_x = int(xlabel*(xmulti-1))
    finish_x = int(xlabel*xmulti)

    # inicio e fim do y da célula
    init_y = int(ylabel*(ymulti-1))
    finish_y = int(ylabel*ymulti)

    mx, my = [], []
    for min in reflectivity_ds:
        for y in min[init_y:finish_y]:
            mx.append(np.mean(y[init_x:finish_x].values))
        my.append(np.mean(mx))
    mm = np.mean(my)
    return mm
