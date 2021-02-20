from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    name = simpledialog.askstring(title = 'Remarkable people', prompt = 'Enter a name from our class')

    if name == 'Emma':
        messagebox.showinfo(title = '', message = 'She is a great friend')

    elif name == 'Caris':
        messagebox.showinfo(title='', message='She can draw')

    elif name == 'Mr. Commins':
        messagebox.showinfo(title='', message='He can code')

    else:
        messagebox.showerror(title='', message='Please insert a classmate')
#caris can draw Mr. Commins can code and Emma???