
from tkinter import *


# FUNCTIONS
def calculate():
    v1 = float(text_box.get())  # KM
    v2 = v1 / 3.6  # MPH
    text2["text"] = "Result" + str(v2) + "mph"


# GUI
window_home = Tk()
window_home.title('Conversor')


# WIDGETS
text1 = Label(window_home, text="Digite em KM")
text_box = Entry(window_home)
botao = Button(window_home, text="Converter", command=calculate)
text2 = Label(window_home, text="Result: ")

# LAYOUT
text1.grid()
text_box.grid()
botao.grid()
text2.grid()


window_home.mainloop()
