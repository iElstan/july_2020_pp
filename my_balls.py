from tkinter import *
from random import randrange as rnd, choice

root = Tk()
root.geometry("800x600")

canv = Canvas(root, width=500, height=500, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black']
def new_ball():
    global x, y, R
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 700)
    R = rnd(30, 50)
    canv.create_oval(x - R, y - R, x + R, y + R, fill=choice(colors), width=0)
    root.after(1000, new_ball)

def click(event):
    print(x, y, R)

new_ball()
canv.bind('<Button-1>', click)
root.mainloop()