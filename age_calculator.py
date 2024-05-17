# Code With Drex
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import datetime
from tkinter import messagebox

window = ttk.Window()

window.title('Age Calculator')
ttk.Style('superhero')
window.geometry('400x370')

# Variables
date = ''
present_date = ttk.StringVar()
p_day = ttk.StringVar()
p_month = ttk.StringVar()
p_year = ttk.StringVar()
dob_day = ttk.StringVar()
dob_month = ttk.StringVar()
dob_year = ttk.StringVar()

main_frame = ttk.Frame(window, width=400, height=370)
main_frame.pack()

title = ttk.Label(main_frame, text='Age Calculator', font=('Sedan', 25, 'bold'))
title.pack()

calc_frame = ttk.Frame(main_frame)
calc_frame.pack(pady=10)

birth_date_label = ttk.Label(calc_frame, text='Birth Date', font=('Times', 20, 'bold'))
birth_date_label.grid(row=0, column=0, padx=(0, 10))

present_date_label = ttk.Label(calc_frame, text='Present Date', font=('Times', 20, 'bold'))
present_date_label.grid(row=0, column=1, padx=(10, 0))

dob_frame = ttk.Frame(calc_frame)
dob_frame.grid(row=1, column=0, padx=10, pady=10)

pd_frame = ttk.Frame(calc_frame)
pd_frame.grid(row=1, column=1, padx=(0, 10), pady=10)

dob_day_label = ttk.Label(dob_frame, text='Day: ', font=('Times', 12), style=INFO)
dob_day_label.grid(row=0, column=0, pady=(5, 0))

dob_day_entry = ttk.Entry(dob_frame, style=INFO, textvariable=dob_day)
dob_day_entry.grid(row=0, column=1, pady=(5, 0))

dob_month_label = ttk.Label(dob_frame, text='Month: ', font=('Times', 12), style=INFO)
dob_month_label.grid(row=1, column=0, pady=(5, 0))

dob_month_entry = ttk.Entry(dob_frame, style=INFO, textvariable=dob_month)
dob_month_entry.grid(row=1, column=1, pady=(5, 0))

dob_year_label = ttk.Label(dob_frame, text='Year: ', font=('Times', 12), style=INFO)
dob_year_label.grid(row=2, column=0, pady=(5, 0))

dob_year_entry = ttk.Entry(dob_frame, style=INFO, textvariable=dob_year)
dob_year_entry.grid(row=2, column=1, pady=(5, 0))



pd_day_label = ttk.Label(pd_frame, text='Day: ', font=('Times', 12), style=INFO)
pd_day_label.grid(row=0, column=0, pady=(5, 0))

pd_day_entry = ttk.Entry(pd_frame, style=INFO, textvariable=p_day)
pd_day_entry.grid(row=0, column=1, pady=(5, 0))

pd_month_label = ttk.Label(pd_frame, text='Month: ', font=('Times', 12), style=INFO)
pd_month_label.grid(row=1, column=0, pady=(5, 0))

pd_month_entry = ttk.Entry(pd_frame, style=INFO, textvariable=p_month)
pd_month_entry.grid(row=1, column=1, pady=(5, 0))

pd_year_label = ttk.Label(pd_frame, text='Year: ', font=('Times', 12), style=INFO)
pd_year_label.grid(row=2, column=0, pady=(5, 0))

pd_year_entry = ttk.Entry(pd_frame, style=INFO, textvariable=p_year)
pd_year_entry.grid(row=2, column=1, pady=(5, 0))


def calculate():
    dob_day = dob_day_entry.get()
    dob_month = dob_month_entry.get()
    dob_year = dob_year_entry.get()
    p_day = pd_day_entry.get()
    p_month = pd_month_entry.get()
    p_year = pd_year_entry.get()


    try: 
        birth_d = datetime.datetime(int(dob_year), int(dob_month), int(dob_day))
        present_d = datetime.datetime(int(p_year), int(p_month), int(p_day))
    except:
        messagebox.showerror('Invalid Date', 'Please enter a valid date')


    age = present_d - birth_d

    age = str(int((age.days + age.seconds/86400)/365.2425))
    age_label.configure(text=f"You are {age} years old")





btn_frame  = ttk.Frame(main_frame)
btn_frame.pack(pady=5)

calc_btn = ttk.Button(btn_frame, text='Calculate', style=INFO, command=calculate)
calc_btn.pack()

age_label = ttk.Label(main_frame, text='', font=('Times', 30, 'bold'), style=SUCCESS)
age_label.pack()


window.mainloop()
