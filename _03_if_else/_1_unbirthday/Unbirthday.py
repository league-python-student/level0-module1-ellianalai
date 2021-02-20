from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()


birthday = simpledialog.askstring(title = 'Birthday Question', prompt = 'When is your birthday')

if birthday == ('2/19'):
    messagebox.showinfo(title = "", message = "I wish you a very merry birthday!")

else:
    messagebox.showinfo(title = '', message = 'I wish you a very merry unbirthday')


