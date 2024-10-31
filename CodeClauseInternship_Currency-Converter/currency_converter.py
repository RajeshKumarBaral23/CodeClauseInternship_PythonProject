import tkinter as tk
from tkinter import ttk

# Define exchange rates (as of October 31, 2024)
exchange_rates = {
    "INR": {
        "USD": 0.0119,
        "EUR": 0.0109,
        "GBP": 0.0092,
        "CAD": 0.0165,
        "AUD": 0.0180,
        "JPY": 1.8253,
        "SGD": 0.0157,
        "TWD": 0.3801,
        "CNY": 0.0847,
        "KRW": 0.0164
    },
    "USD": {
        "INR": 84.08,
        "EUR": 0.92,
        "GBP": 0.77,
        "CAD": 1.39,
        "AUD": 1.5152,
        "JPY": 153.47,
        "SGD": 1.32,
        "TWD": 31.96,
        "CNY": 7.12,
        "KRW": 16.40
    },
    "EUR": {
        "INR": 91.39,
        "USD": 1.09,
        "GBP": 0.84,
        "CAD": 1.51,
        "AUD": 1.65,
        "JPY": 142.00,
        "SGD": 1.43,
        "TWD": 34.74,
        "CNY": 7.56,
        "KRW": 15.10
    },
    "GBP": {
        "INR": 109.19,
        "USD": 1.29,
        "EUR": 1.19,
        "CAD": 1.80,
        "AUD": 1.97,
        "JPY": 163.00,
        "SGD": 1.71,
        "TWD": 41.51,
        "CNY": 8.73,
        "KRW": 18.06
    },
    "CNY": {
        "INR": 11.81,
        "USD": 0.14,
        "EUR": 0.13,
        "GBP": 0.11,
        "CAD": 0.19,
        "AUD": 0.21,
        "JPY": 18.73,
        "SGD": 0.18,
        "TWD": 4.49,
        "KRW": 0.37
    },
    "JPY": {
        "INR": 0.55,
        "USD": 0.0065,
        "EUR": 0.0070,
        "GBP": 0.0061,
        "CAD": 0.0102,
        "AUD": 0.0114,
        "SGD": 0.0086,
        "TWD": 0.21,
        "CNY": 0.0535,
        "KRW": 0.0102
    },
    "KRW": {
        "INR": 60.96,
        "USD": 0.061,
        "EUR": 0.055,
        "GBP": 0.055,
        "CAD": 0.085,
        "AUD": 0.094,
        "JPY": 98.04,
        "SGD": 0.076,
        "TWD": 1.85,
        "CNY": 0.27
    },
    "CAD": {
        "INR": 60.49,
        "USD": 0.72,
        "EUR": 0.66,
        "GBP": 0.55,
        "AUD": 0.82,
        "JPY": 98.00,
        "SGD": 0.75,
        "TWD": 18.54,
        "CNY": 5.23,
        "KRW": 11.73
    },
    "AUD": {
        "INR": 55.49,
        "USD": 0.66,
        "EUR": 0.61,
        "GBP": 0.51,
        "CAD": 0.91,
        "JPY": 88.00,
        "SGD": 0.68,
        "TWD": 16.52,
        "CNY": 4.71,
        "KRW": 10.64
    },
    "SGD": {
        "INR": 63.70,
        "USD": 0.76,
        "EUR": 0.70,
        "GBP": 0.58,
        "CAD": 1.05,
        "AUD": 1.14,
        "JPY": 116.27,
        "TWD": 24.21,
        "CNY": 5.39,
        "KRW": 12.42
    },
    "TWD": {
        "INR": 2.63,
        "USD": 0.031,
        "EUR": 0.029,
        "GBP": 0.024,
        "CAD": 0.043,
        "AUD": 0.047,
        "JPY": 4.80,
        "SGD": 0.041,
        "CNY": 0.22,
        "KRW": 0.054
    }
}

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        result_label.config(text="Invalid currency code. Please try again.")
        return

    converted_amount = amount * exchange_rates[from_currency][to_currency]
    result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create labels and entry fields
amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = ttk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = ttk.Label(root, text="From Currency:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)
from_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = ttk.Label(root, text="To Currency:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)
to_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

# Create the convert button
convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Create the result label
result_label = ttk.Label(root, text="")
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

root.mainloop()