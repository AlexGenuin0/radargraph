import xarray as xr
import nameList as nL
from graphs import graphBar
import argparse
# from moviepy.editor import concatenate_videoclips, VideoFileClip
from avgReflectivity import avgReflectivity as avrg
# from animReflectivity import animReflectivity


def main():
    parser = argparse.ArgumentParser(description='Esse sistema lê as informações de arquivos vindos do satélite '
                                                 'TAASRAD19 e coleta as médias de refletividade diárias, que então '
                                                 'são usadas para formar um gráfico com todas elas ao longo de '
                                                 'um determinado período de tempo.')
    parser.add_argument('-di', '--datai', type=str, help='Data inicial (aaaammdd)')
    parser.add_argument('-df', '--dataf', type=str, help='Data final (aaaammdd)')
    parser.add_argument('-c', '--cell', type=str, help='Célula específica a ser analisada (ex: 10-5)')
    parser.add_argument('-p', '--path', type=str,
                        help='O diretório no qual você salvou os arquivos do radar. É necessário especificar '
                             'esse endereço para o funcionamento do código.')
    args = parser.parse_args()

    if len(args.cell) > 0:
        cell = args.cell.split('-')

    d = [args.datai, args.dataf]

    mrdia, ldias, name = [], [], ''
    fileL = nL.fileName(d)
    for i in fileL:
        try:
            arq = args.path + i
            ds = xr.open_dataset(arq)
            mrdia.append(avrg(ds.equivalent_reflectivity_factor, cell))  # media diaria
            ldias.append(i[6:-3])
#            animReflectivity(ds.equivalent_reflectivity_factor, i[:-2])
#            if name == '':
#                name = i[:-2] + 'mp4'
#            else:
#                v1 = VideoFileClip(name)
#                name = i[:-2] + 'mp4'
#                v2 = VideoFileClip(name)
#                video = concatenate_videoclips([v1, v2])
#                video.write_videofile(f'{name}')
        except:
            pass
    graphBar(ldias, mrdia, d, cell)


main()
