import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    ellie = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title = 'Shape', prompt = 'Do you want to draw a triangle, square, or circle? ')
    # Draw the shape requested by the user using if-elif-else statements
    if shape == 'triangle':
        for i in range(3):
            ellie.forward(120)
            ellie.left(120)
    if shape == 'square':
        for i in range(4):
            ellie.forward(120)
            ellie.right(90)
    if shape == 'circle':
        ellie.circle(100,360,50)


    # Call the turtle .done() method
    turtle.done()