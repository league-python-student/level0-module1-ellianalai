"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

number1 = simpledialog.askfloat(title = "Two numbers", prompt = 'Input a number')
number2 = simpledialog.askfloat(title = "Two numbers", prompt = 'Input another number')

calculator = simpledialog.askstring(title = '', prompt = 'Would you like to add, subtract, multiply, or divide')

if calculator == "add":
    sum = number1 + number2
    messagebox.showinfo(title='Sum', message='Your sum is ' + str(sum))
elif calculator == 'subtract':
    otherSum = number1 - number2
    messagebox.showinfo(title='Sum', message='Your sum is ' + str(otherSum))
elif calculator == 'multiply':
    anotherSum = number1 * number2
    messagebox.showinfo(title='Sum', message='Your sum is ' + str(anotherSum))
elif calculator == 'divide':
    lastSum = number1/number2
    messagebox.showinfo(title='Sum', message='Your sum is ' + str(lastSum))

else:
    messagebox.showerror(title = '', message = 'Please input one of the 4 math things')

