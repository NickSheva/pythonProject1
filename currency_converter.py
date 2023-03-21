from tkinter import *

window = Tk()
window.title('Currency Converter')

input_label = Label(window, text='Input the Amount for Conversion:', font='arial 12 bold', borderwidth=5)
input_fc = Label(window, text='Convert From Currency:', font='arial 12 bold', borderwidth=5)
input_tc = Label(window, text='Convert To Currency:', font='arial 12 bold', borderwidth=5)
outputlabel = Label(window, text='Converted Amount:', font='arial 12 bold', borderwidth=5)

input_amount = Entry(window, font='arial 12 bold', borderwidth=5)
from_currency = Entry(window, font='arial 12 bold', borderwidth=5)
to_currency = Entry(window, font='arial 12 bold', borderwidth=5)
output = Entry(window, font='arial 12 bold', borderwidth=5)

input_label.grid(row=0, column=0, padx=20, pady=20)
input_fc.grid(row=1, column=0)
input_tc.grid(row=2, column=0)
outputlabel.grid(row=4, column=0)

input_amount.grid(row=0, column=1)
from_currency.grid(row=1, column=1)
to_currency.grid(row=2, column=1, padx=20, pady=20)
output.grid(row=4, column=1, padx=20, pady=20)

ACCESS_KEY = '1cf94c2fd27ab40a0b510ccec2d0014b'
url = str.__add__('http://data.fixer.io/api/latest?access_key=', ACCESS_KEY)
import requests
data = requests.get(url).json()
rates = data['rates']

def covert(from_currency, to_currrency, input_amount):
    from_currency = from_currency.get()
    to_currrency = to_currrency.get()
    input_amount = float(input_amount.get())
    if from_currency != 'EUR':
        input_amount = input_amount / rates[from_currency]
    output.insert(0, round(input_amount * rates[to_currrency], 2))
    return



my_button = Button(window, text='CONVERT', font='arial 14 bold', borderwidth=10,
                   padx=50, pady=10, bg='blue', comman=lambda: covert(from_currency, to_currency, input_amount))
my_button.grid(row=3, column=1, columnspan=1)



window.mainloop()