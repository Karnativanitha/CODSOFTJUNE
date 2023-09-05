import tkinter as tk

# Function to update the input field when buttons are pressed
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to perform calculations
def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an input field
entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define and create calculator buttons
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for text in button_texts:
    if text == '=':
        tk.Button(window, text=text, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    elif text == 'C':
        tk.Button(window, text=text, padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=text, padx=20, pady=20, command=lambda t=text: button_click(t)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the GUI application
window.mainloop()
