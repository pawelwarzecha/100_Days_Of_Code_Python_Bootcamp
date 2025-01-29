from tkinter import *

#Converts miles to Km and changes the calculate_result_label
def calculate():
    value = int(input_window.get())
    km = value * 1.609344
    calculate_result_label.config(text=round(km, 2))

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=280, height=100)
window.config(padx=40, pady=20)

#Input
input_window = Entry(width=10)
input_window.insert(END, string="0")
input_window.grid(column=1, row=0)

#Input label
input_label = Label(text="Miles")
input_label.grid(column=2, row=0)

#Text labels
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

#Label that shows the result of calculate func
calculate_result_label = Label(text="0")
calculate_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#calls calculate when pressed
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()