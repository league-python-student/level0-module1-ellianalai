from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

radius = simpledialog.askinteger(title = '', prompt = 'What is the radius of a circle?')
circle = simpledialog.askstring(title = '', prompt = 'Would you like to calculate the area or circumference of a circle')
if circle == 'area':
    area = radius * radius * math.pi
    messagebox.showinfo(title='', message='The area is ' + str(area))
elif circle =='circumference':
    circumference = 2*radius*math.pi
    messagebox.showinfo(title='', message='The circumference is ' + str(circumference))
else:
    messagebox.showerror(title = '', message = 'Choose the area or circumference')

# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr 