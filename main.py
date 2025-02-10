from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import ttk

# FUNCTIONS
def calculate():
    try:
        km = float(text_box.get())  # KM
        mph = km / 3.6  # MPH
        result.set(f"Result: {mph:.2f} mph")
    except ValueError:
        result.set("Please enter a valid number")

# GUI
window_home = Tk()
window_home.title('KM to MPH Converter')
window_home.geometry('300x150')
window_home.resizable(False, False)

# STYLES
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12))
style.configure('TButton', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))

# WIDGETS
text1 = ttk.Label(window_home, text="Enter value in KM:")
text_box = ttk.Entry(window_home)
button = ttk.Button(window_home, text="Convert", command=calculate)
result = StringVar()
text2 = ttk.Label(window_home, textvariable=result)

# LAYOUT
text1.grid(row=0, column=0, padx=10, pady=10, sticky='W')
text_box.grid(row=0, column=1, padx=10, pady=10)
button.grid(row=1, column=0, columnspan=2, pady=10)
text2.grid(row=2, column=0, columnspan=2, pady=10)

window_home.mainloop()