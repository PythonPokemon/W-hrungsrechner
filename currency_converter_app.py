from tkinter import *
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Währungsrechner")

        self.c = CurrencyRates()

        self.from_currency_label = Label(self.root, text="Von Währung:")
        self.from_currency_label.pack(padx=10, pady=5)
        
        self.from_currency_var = StringVar()
        self.from_currency_var.set("USD")
        self.from_currency_menu = OptionMenu(self.root, self.from_currency_var, *self.c.get_rates("").keys())
        self.from_currency_menu.pack(padx=10, pady=5)

        self.amount_label = Label(self.root, text="Betrag:")
        self.amount_label.pack(padx=10, pady=5)

        self.amount_entry = Entry(self.root)
        self.amount_entry.pack(padx=10, pady=5)

        self.to_currency_label = Label(self.root, text="Zu Währung:")
        self.to_currency_label.pack(padx=10, pady=5)

        self.to_currency_var = StringVar()
        self.to_currency_var.set("EUR")
        self.to_currency_menu = OptionMenu(self.root, self.to_currency_var, *self.c.get_rates("").keys())
        self.to_currency_menu.pack(padx=10, pady=5)

        self.convert_button = Button(self.root, text="Umrechnen", command=self.convert)
        self.convert_button.pack(padx=10, pady=5)

        self.result_label = Label(self.root, text="")
        self.result_label.pack(padx=10, pady=5)

    def convert(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = float(self.amount_entry.get())
        
        converted_amount = self.c.convert(from_currency, to_currency, amount)
        result_text = f"{amount:.2f} {from_currency} entsprechen {converted_amount:.2f} {to_currency}"
        
        self.result_label.config(text=result_text)

if __name__ == "__main__":
    root = Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
