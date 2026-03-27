import tkinter as tk
from tkinter import messagebox
import math


# -------------------------------
# Calculator Logic (Clean & Modular)
# -------------------------------

def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def safe_sqrt(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)


def safe_log(a):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers.")
    return math.log10(a)


# Operation mapping (BIG UPGRADE)
OPERATIONS = {
    "ADD": lambda a, b: a + b,
    "SUB": lambda a, b: a - b,
    "MULT": lambda a, b: a * b,
    "DIV": safe_divide,
    "POW": lambda a, b: math.pow(a, b),

    "SQR": lambda a, _: a ** 2,
    "SQRT": lambda a, _: safe_sqrt(a),
    "CUB": lambda a, _: a ** 3,
    "CBRT": lambda a, _: math.copysign(abs(a) ** (1/3), a),

    "LOG": lambda a, _: safe_log(a),
    "SIN": lambda a, _: math.sin(math.radians(a)),
    "COS": lambda a, _: math.cos(math.radians(a)),
    "TAN": lambda a, _: math.tan(math.radians(a)),
}


# -------------------------------
# UI Logic
# -------------------------------

def get_inputs():
    try:
        num1 = float(entry1.get())
    except ValueError:
        raise ValueError("First number is required and must be valid.")

    try:
        num2 = float(entry2.get()) if entry2.get() else 0
    except ValueError:
        raise ValueError("Second number must be valid.")

    return num1, num2


def calculate(operation):
    try:
        num1, num2 = get_inputs()

        func = OPERATIONS.get(operation)
        if not func:
            raise ValueError("Invalid operation.")

        result = func(num1, num2)
        result_label.config(text=f"Result: {result:.6g}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -------------------------------
# UI Setup
# -------------------------------

root = tk.Tk()
root.title("Calculator GUI (Pro)")
root.geometry("420x520")


# Input Section
tk.Label(root, text="First Number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Second Number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)


# Buttons Layout (Cleaner grid)
buttons = [
    ["ADD", "SUB", "MULT", "DIV"],
    ["SQR", "SQRT", "CUB", "CBRT"],
    ["LOG", "SIN", "COS", "TAN"],
    ["POW"]
]

row_start = 2
for i, row in enumerate(buttons):
    for j, op in enumerate(row):
        tk.Button(
            root,
            text=op,
            width=8,
            command=lambda op=op: calculate(op)
        ).grid(row=row_start + i, column=j, padx=5, pady=5)


# Result Display
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.grid(row=10, column=0, columnspan=4, pady=20)


# Run App
root.mainloop()
