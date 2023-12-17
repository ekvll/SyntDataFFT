import PySimpleGUI as sg


def make_layout():
    text_pad = (14, 1)
    pad = (15, 1)
    pad1 = (13, 1)

    layout = [
        [sg.MenuBar([["File", ["Exit"]], ["Help", ["About", "Contact"]]])],
        [
            sg.Text("Signal duration (s):", size=text_pad),
            sg.InputText(default_text="200", key="duration", size=pad),
        ],
        [
            sg.Text("Sampling rate (Hz):", size=text_pad),
            sg.InputText(default_text="40", key="sampling_rate", size=pad),
        ],
        [
            sg.Text("Noise level:", size=text_pad),
            sg.InputText(default_text="0.10", key="noise_level", size=pad),
        ],
        [
            sg.Text("", size=text_pad),
            *[
                sg.Text(label, size=pad1)
                for label in [
                    "Amplitude",
                    "Start time (s)",
                    "Duration (s)",
                    "Frequency (Hz)",
                    "Exponential decay",
                ]
            ],
        ],
        [
            sg.Text("Anomaly 1:", size=text_pad),
            sg.InputText(key=f"input_1_1", default_text="2.5", size=pad),
            sg.InputText(key=f"input_1_2", default_text="50", size=pad),
            sg.InputText(key=f"input_1_3", default_text="10", size=pad),
            sg.InputText(key=f"input_1_4", default_text="5", size=pad),
            sg.InputText(key=f"input_1_5", default_text="1.0", size=pad),
        ],
        [
            sg.Text("Anomaly 2:", size=text_pad),
            sg.InputText(key=f"input_2_1", default_text="2.1", size=pad),
            sg.InputText(key=f"input_2_2", default_text="100", size=pad),
            sg.InputText(key=f"input_2_3", default_text="9", size=pad),
            sg.InputText(key=f"input_2_4", default_text="10", size=pad),
            sg.InputText(key=f"input_2_5", default_text="0.8", size=pad),
        ],
        [sg.Button("Update plot")],
        [sg.Canvas(key="-CANVAS-")],
    ]

    return layout


def make_window(layout):
    window_width = 1100
    window_height = 950
    title = "SyntDataFFT"
    window = sg.Window(title, layout, finalize=True, size=(window_width, window_height))
    return window


def open_about_window():
    sg.popup("Version: 0.1", "License: MIT", "Homepage: https://nppd.se/syntdatafft/index.html","Source code: https://github.com/ekvll/SyntDataFFT")


def open_contact_window():
    sg.popup("erik.k.lindvall@gmail.com")
