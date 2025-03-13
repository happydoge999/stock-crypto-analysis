from tkinter import Tk, Label, Button, Frame, StringVar, messagebox
from analysis.stock_analysis import StockAnalysis
from analysis.crypto_analysis import CryptoAnalysis

class App:
    def __init__(self, master):
        self.master = master
        master.title("Stock and Cryptocurrency Analysis")

        self.frame = Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.label = Label(self.frame, text="Welcome to Stock and Crypto Analysis")
        self.label.pack()

        self.stock_button = Button(self.frame, text="Analyze Stocks", command=self.analyze_stocks)
        self.stock_button.pack(pady=5)

        self.crypto_button = Button(self.frame, text="Analyze Cryptocurrencies", command=self.analyze_crypto)
        self.crypto_button.pack(pady=5)

        self.result_var = StringVar()
        self.result_label = Label(self.frame, textvariable=self.result_var)
        self.result_label.pack(pady=10)

    def analyze_stocks(self):
        try:
            stock_analysis = StockAnalysis()
            stock_analysis.fetch_data()
            report = stock_analysis.generate_report()
            self.result_var.set(report)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def analyze_crypto(self):
        try:
            crypto_analysis = CryptoAnalysis()
            crypto_analysis.fetch_data()
            report = crypto_analysis.generate_report()
            self.result_var.set(report)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()