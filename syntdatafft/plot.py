import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def define_plot(window):
    fig, ax = plt.subplots(nrows=3, figsize=(12, 8))
    fig.tight_layout()
    canvas_elem = window["-CANVAS-"]
    canvas = FigureCanvasTkAgg(fig, canvas_elem.Widget)
    canvas.draw()
    canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
    return fig, ax, canvas


def update_plot(fig, ax, time, data, data_windowed, window, freq, magnitude_db):
    for subplot in ax:
        subplot.clear()

    if hasattr(update_plot, 'ax1') and update_plot.ax1 is not None:
        update_plot.ax1.clear()

    ax[0].set_title("Raw signal")
    ax[0].plot(time, data, "k", linewidth=1)
    ax[0].set_xlabel("Duration (s)")
    ax[0].set_ylabel("Amplitude")
    ax[0].grid(alpha=0.6)
    ylim_ax0 = ax[0].get_ylim()

    # ===================
    ax[1].set_title("Windowed signal")
    (line1,) = ax[1].plot(time, data_windowed, "k", linewidth=1)
    ax[1].set_xlabel("Duration (s)")
    ax[1].set_ylabel("Amplitude")
    ax[1].grid(alpha=0.6)
    ax[1].set_ylim(ylim_ax0)

    if not hasattr(update_plot, 'ax1') or update_plot.ax1 is None:
        update_plot.ax1 = ax[1].twinx()
    else:
        update_plot.ax1.clear()

    (line2,) = update_plot.ax1.plot(time, window, "r", label="Hamming window", linewidth=1)
    update_plot.ax1.set_ylabel("Amplitude", color="r")
    update_plot.ax1.tick_params("y", colors="r")
    
    update_plot.ax1.yaxis.set_label_coords(1.07, 0.5)

    lines = [line1, line2]
    labels = [line.get_label() for line in lines]
    update_plot.ax1.legend(lines, labels, loc="upper right")

    # ===================
    ax[2].set_title("Frequency spectrum of windowed signal")
    ax[2].plot(freq, magnitude_db, "k", label="Frequency spectrum", linewidth=1)
    ax[2].set_xlabel("Frequency (Hz)")
    ax[2].set_ylabel("Magnitude (dB)")
    ax[2].grid(alpha=0.6)

    fig.tight_layout()
