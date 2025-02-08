from tkinter import *
from tkinter import ttk


def clear_frame():
    #clear window
    for widget in window.winfo_children():
        widget.destroy()


def is_float(string_input):
    # checks if string can be turned to float
    is_float_i = 0
    try:
        float(string_input)
    except ValueError:
        is_float_i = 1
    return is_float_i


def length_execute():
    # length inputs placed and entered for calculation
    if len(entered_value.get()) != 0:
        # ensure not empty input and float
        can_run = is_float(entered_value.get())
        if can_run == 0:
            # output calculation
            entry_out['text'] = length_convertor(float(entered_value.get()), inputted_unit.get(), outputted_unit.get())


def pressure_execute():
    # pressure inputs placed and entered for calculation
    if len(entered_value.get()) != 0:
        # ensure not empty input and float
        can_run = is_float(entered_value.get())
        if can_run == 0:
            # output calculation
            entry_out['text'] = pressure_convertor(float(entered_value.get()), inputted_unit.get(),
                                                   outputted_unit.get())


def temperature_execute():
    # temperature inputs placed and entered for calculation
    if len(entered_value.get()) != 0:
        # ensure not empty input and float
        can_run = is_float(entered_value.get())
        if can_run == 0:
            # output calculation
            entry_out['text'] = temperature_convertor(float(entered_value.get()), inputted_unit.get(),
                                                      outputted_unit.get())


def length_parameter():
    # length button clicked
    clear_frame()
    length_choices = ["mm", "cm", "m", "km", "nm", "inches"]
    main_interface(length_choices)


def pressure_parameter():
    # pressure button clicked
    clear_frame()
    pressure_choices = ["Pa", "kPa", "MPa", "GPa"]
    main_interface(pressure_choices)


def temperature_parameter():
    # temperature button clicked
    clear_frame()
    temperature_choices = ["K", u"\u00b0" + "C", u"\u00b0" + "F"]
    main_interface(temperature_choices)


def length_convertor(value, from_unit, to_unit):
    # length conversion based on units
    answer = float('nan')
    if from_unit in lengths_dict and to_unit in lengths_dict:
        # calculates only when acceptable units
        answer = value * lengths_dict[from_unit] / lengths_dict[to_unit]
    return answer


def pressure_convertor(value, from_unit, to_unit):
    # pressure conversion based on units
    answer = float('nan')
    if from_unit in pressure_dict and to_unit in pressure_dict:
        # calculates only when acceptable units
        answer = value * pressure_dict[from_unit] / pressure_dict[to_unit]
    return answer


def temperature_convertor(value, from_unit, to_unit):
    # temperature conversion based on units
    answer = float('nan')
    if from_unit in temperature_dict and to_unit in temperature_dict:
        # calculate only when acceptable units
        x = (value - temperature_dict[from_unit][1]) / temperature_dict[from_unit][0]
        answer = temperature_dict[to_unit][0] * x + temperature_dict[to_unit][1]
        if answer < temperature_dict[to_unit][2]:
            # absolute zero reached
            answer = float('nan')
    return answer


def main_interface(list_in):
    # build main user interface after choice made
    # top row labels
    label_input = Label(window, text='Input value:')
    label_input.grid(row=0, column=0)
    label_input_unit = Label(window, text='Input unit:')
    label_input_unit.grid(row=0, column=1)
    label_output = Label(window, text='Output value:')
    label_output.grid(row=0, column=2)
    label_output_unit = Label(window, text='Output unit:')
    label_output_unit.grid(row=0, column=3)
    # Value enter and output display
    entry = Entry(window, textvariable=entered_value)
    entry.grid(row=1, column=0)
    global entry_out
    entry_out = Label(window)
    entry_out.grid(row=1, column=2)
    # unit drop selection
    input_unit = ttk.Combobox(window, values=list_in, textvariable=inputted_unit)
    input_unit.grid(row=1, column=1)
    output_unit = ttk.Combobox(window, values=list_in, textvariable=outputted_unit)
    output_unit.grid(row=1, column=3)
    # change computation calculation based on choice made on first interface
    if list_in[0] == "mm":
        enter = Button(window, text='Enter', command=length_execute)
        enter.grid(row=2, column=4)
    elif list_in[0] == "Pa":
        enter = Button(window, text='Enter', command=pressure_execute)
        enter.grid(row=2, column=4)
    else:
        enter = Button(window, text='Enter', command=temperature_execute)
        enter.grid(row=2, column=4)


# variables
lengths_dict = {
    "mm": 1e-3,
    "cm": 1e-2,
    "m": 1,
    "km": 1000,
    "nm": 1e-9,
    "inches": 0.0254
}

pressure_dict = {
    "Pa": 1,
    "kPa": 1000,
    "MPa": 1e6,
    "GPa": 1e9
}

temperature_dict = {
    "K": [1, 273.15, 0],
    u"\u00b0" + "C": [1, 0, -273.15],
    u"\u00b0" + "F": [9 / 5, 32, -460]
}

global entry_out
# code
# main window
window = Tk()
window.title('Unit Converter')
# window variables
inputted_unit = StringVar()
outputted_unit = StringVar()
entered_value = StringVar()
exited_value = StringVar()
# length, pressure, and temperature buttons
button_length = Button(window, text='Length')
button_length.config(command=length_parameter)
button_length.pack()

button_pressure = Button(window, text='Pressure')
button_pressure.config(command=pressure_parameter)
button_pressure.pack()

button_temperature = Button(window, text='Temperature')
button_temperature.config(command=temperature_parameter)
button_temperature.pack()
window.mainloop()
