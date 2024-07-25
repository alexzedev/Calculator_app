import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator by alexzedev")
        master.geometry("400x400")
        master.resizable(False, False)

        self.total = 0
        self.entered_number = 0
        self.current_operation = ""
        self.result_displayed = False

        # Create and set up the display
        self.display = tk.Entry(master, width=20, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.display.insert(0, "0")

        # Create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        # Add buttons to the calculator
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=7, height=2, font=("Arial", 14)).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Add equals button
        tk.Button(master, text="=", command=self.calculate, width=16, height=2, font=("Arial", 14)).grid(row=row, column=0, columnspan=2, padx=2, pady=2)

    def click(self, key):
        if self.result_displayed:
            self.clear_display()
            self.result_displayed = False

        if key.isdigit() or key == '.':
            current = self.display.get()
            if current == '0' and key != '.':
                self.display.delete(0, tk.END)
            self.display.insert(tk.END, key)
        elif key in ['+', '-', '*', '/']:
            self.total = self.get_displayed_number()
            self.current_operation = key
            self.clear_display()
        elif key == 'C':
            self.clear_display()
            self.total = 0
            self.current_operation = ""

    def get_displayed_number(self):
        try:
            return float(self.display.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input")
            self.clear_display()
            return 0

    def clear_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")

    def calculate(self):
        if self.current_operation:
            self.entered_number = self.get_displayed_number()
            if self.current_operation == '+':
                self.total += self.entered_number
            elif self.current_operation == '-':
                self.total -= self.entered_number
            elif self.current_operation == '*':
                self.total *= self.entered_number
            elif self.current_operation == '/':
                if self.entered_number == 0:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    self.clear_display()
                    return
                self.total /= self.entered_number
            
            self.clear_display()
            self.display.delete(0, tk.END)  # Remove the initial '0'
            self.display.insert(0, str(self.total))
            self.current_operation = ""
            self.result_displayed = True

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()