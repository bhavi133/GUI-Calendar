import calendar
import tkinter as tk

window = tk.Tk()
window.title("Calendar")
window.geometry('550x650')

calendar = calendar.calendar(2021)

label = tk.Label(window, text="Calendar", font=('times', 28, 'bold'))
label.grid(row=1, column=1)

label_cal = tk.Label(window, text=calendar, font=('Consolas', 10, 'bold'))
label_cal.grid(row=2, column=1, padx=20, pady=20)

window.mainloop()
