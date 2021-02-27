from tkinter import messagebox, simpledialog, Tk
import tkinter as tk

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
tomato = simpledialog.askstring(title = 'Color of Tomato', prompt = 'What color tomato would you like? Red, Yellow, or Green')

# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
if tomato == 'red':
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
elif tomato == 'Yellow':
    canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
elif tomato =='Green':
    canvas.create_oval(200, 200, 525, 450, fill="yellow", outline="")
else:
    messagebox.showerror(title = '', message = 'Please insert one of the colors said')

canvas.create_rectangle(275, 100, 200, 230, fill="green", outline="")


root.mainloop()
