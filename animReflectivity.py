from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter, FFMpegFileWriter
import matplotlib.pyplot as plt


def animReflectivity(rds, name):
    def animate(i):
        fig.clear()
        plt.title('teste')
        return rds[i].plot.pcolormesh(x='x', y='y', add_colorbar=True)

    fig = plt.figure(figsize=(10, 8))
    anim = FuncAnimation(fig, animate, frames=rds.time.size, interval=250, blit=False)
    anim.save(f'./video/{name}.mp4', writer='ffmpeg', fps=1)

