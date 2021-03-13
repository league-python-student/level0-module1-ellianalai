from tkinter import *

window_width = 800
window_height = 800
root = Tk()

canvas = Canvas(root, width=window_width, height=window_height, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()


# this code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # Draws a dark blue background
    canvas.create_rectangle(0, 0, window_width, window_height, fill="#000050")

    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y
    
    # This defines the x and y coordinated of all three points
    # of a triangle
    #          x1, y1,  x2,  y2, x3, y3

    
    # 1. Add details to your rocket to make it look better. You can look at
    #    rocket.png for inspiration.

    canvas.create_oval(x,y,x+110,y+130, fill = 'red')
    canvas.create_oval(x, y, x+98, y+115, fill='orange')
    canvas.create_oval(x, y, x+85, y+95, fill='yellow')
    points = [x+40, y-65, x+100, y+35, x, y+35]
    canvas.create_polygon(points, fill='gray', width=2)  # draws triangle
    # 2. Modify the locations of the shapes above so the rocket will be drawn
    #    where the mouse is clicked
    

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()
