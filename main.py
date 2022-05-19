import xarray as xr
import numpy as np
import os
import nameList as nl
import graphs
import timedate as td


def main():
    mrdia, ldias = [], []
    fileL, year, month = nl.fileName()
    for i in fileL:
        try:
            path = 'C:\\Users\\PC\\Desktop\\arquivos_netcdf'
            arq = os.path.join(path, i)
            ds = xr.open_dataset(arq)
            mrdia.append(np.mean(ds.equivalent_reflectivity_factor))  # media diaria
            ldias.append(i[6:-3])
        except:
            pass
    graphs.graphicBar(ldias, mrdia, year, td.monthName(month))


main()