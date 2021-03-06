"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
number1 = simpledialog.askinteger(title = "Two numbers", prompt = 'Input a number')
number2 = simpledialog.askinteger(title = "Two numbers", prompt = 'Input another number')
sum = number1 + number2
messagebox.showinfo (title = 'Sum', message= 'Your sum is ' + str(sum))