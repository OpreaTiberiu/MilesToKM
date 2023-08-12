from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=15, justify=CENTER)
miles_input.grid(column=0, row=0, padx=5, pady=5)
miles_label = Label(text="Miles")
miles_label.grid(column=1, row=0, padx=5, pady=5)

km_res = Label(background="white", width=13)
km_res.grid(column=0, row=1, padx=5, pady=5)
km_label = Label(text="KM")
km_label.grid(column=1, row=1, padx=5, pady=5)

convert_button = Button(
    text="Convert",
    command=lambda: km_res.config(text=f"{round(float(miles_input.get()) * 1.609, 1)}"))
convert_button.grid(column=0, row=2, columnspan=2, padx=5, pady=5)

window.mainloop()
