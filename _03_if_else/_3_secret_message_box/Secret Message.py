from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    password = simpledialog.askstring(title = 'Password', prompt = 'Enter a password')
    secret = simpledialog.askstring(title = 'Secret', prompt = 'Enter a secret of yours')
    guess = simpledialog.askstring(title = '', prompt = 'Type out the password and you will recieve the secret!')
    if password == guess:
        messagebox.showinfo(title = '', message = secret)
    else:
        messagebox.showerror(title= '', message = "Wrong Password, please try again")