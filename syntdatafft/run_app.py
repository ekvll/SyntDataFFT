import matplotlib

matplotlib.use("TkAgg")

import PySimpleGUI as sg
import syntdatafft as sdf


def run_app():
    """
    Run the PySimpleGUI application.

    The application includes functionality to update a plot based on user input.

    Returns:
    None
    """
    layout = sdf.make_layout()
    window = sdf.make_window(layout)
    fig, ax, canvas = sdf.define_plot(window)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break

        if event == "About":
            sdf.open_about_window()

        if event == "Contact":
            sdf.open_contact_window()

        if event == "Update plot":
            plot_dict = sdf.create_plot_dict(values)
            plot_dict = sdf.change_type_to_float(plot_dict)

            if sdf.are_all_floats(plot_dict):
                duration = plot_dict["duration"]
                sampling_rate = plot_dict["sampling_rate"]
                noise_level = plot_dict["noise_level"]

                anomalies = sdf.generate_anomalies(plot_dict)

                time, data = sdf.gen_1d_test_data(
                    duration, sampling_rate, noise_level, anomalies
                )

                data_windowed, data_window, freq, magnitude_db = sdf.workflow_fft(
                    data, sampling_rate
                )

                sdf.update_plot(
                    fig, ax, time, data, data_windowed, data_window, freq, magnitude_db
                )
                canvas.draw()
    window.close()
