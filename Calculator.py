import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numerical values.")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="First Number:")
label_num1.pack(padx=10, pady=5)

entry_num1 = tk.Entry(root)
entry_num1.pack(padx=10, pady=5)

label_num2 = tk.Label(root, text="Second Number:")
label_num2.pack(padx=10, pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(padx=10, pady=5)

button_add = tk.Button(root, text="+", command=lambda: calculate('+'))
button_add.pack(side=tk.LEFT, padx=5, pady=5)

button_subtract = tk.Button(root, text="-", command=lambda: calculate('-'))
button_subtract.pack(side=tk.LEFT, padx=5, pady=5)

button_multiply = tk.Button(root, text="*", command=lambda: calculate('*'))
button_multiply.pack(side=tk.LEFT, padx=5, pady=5)

button_divide = tk.Button(root, text="/", command=lambda: calculate('/'))
button_divide.pack(side=tk.LEFT, padx=5, pady=5)

label_result = tk.Label(root, text="Result: ")
label_result.pack(padx=10, pady=10)

root.mainloop()
