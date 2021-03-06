"""

* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    riddle = simpledialog.askstring(title = '', prompt = 'A man is sitting in his cabin in Michigan. 3 hours later, he gets out of his cabin in Texas. How is this possible?')
    if riddle == 'He is a pilot in the cabin of an airplane':
        messagebox.showinfo(title = '', message = 'You are Correct!')
    else:
        messagebox.showerror(title = '', message = 'You are Incorrect')
    anotherRiddle = simpledialog.askstring(title = '', prompt = 'A woman was sitting in her hotel room when there was a knock on her door.\n She opened the door to see a man whom she had never seen before. He said oh I am sorry, I have made a mistake , I thought this was my room. \n He then went down the corridor and in the elevator. The woman went back into her room and phoned security. What made the woman so suspicious of the man?')
    if anotherRiddle == 'You do not knock on your own hotel door':
        messagebox.showinfo(title='', message='You are Correct!')
    else:
        messagebox.showerror(title='', message='You are Incorrect')
    lastRiddle = simpledialog.askstring(title = '', prompt = 'A boy had just got out of the shower and was getting ready for the prom, shaved. \n There was also going to be an after party. His mom and dad said to be home for the next sunrise and he did, and came home with a fully grown beard? \n How can this be?')
    if lastRiddle == "He lives in Alaska and there is a sunrise every six months":
        messagebox.showinfo(title='', message='You are Correct!')
    else:
        messagebox.showerror(title='', message='You are Incorrect')