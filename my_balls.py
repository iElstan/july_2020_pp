from tkinter import *
from random import randrange as rnd, choice

name = input("Введите имя:\n")
root = Tk()
root.geometry("800x600")

canv = Canvas(root, bg='lightblue')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'blue', 'green', 'orange', 'yellow', 'black']


def new_ball():
    """Функция отображения шарика случайного размера в случайном месте"""
    global x, y, R
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 700)
    R = rnd(30, 50)
    canv.create_oval(x - R, y - R, x + R, y + R, fill=choice(colors), width=0)
    root.after(1000, new_ball)


score = 0


def click(event):
    """Функциия регистрации клика левой кнопкой мыши, плюс попадание по шарику и счет"""
    global score
    print(event.x, event.y, x, y, R)
    if x + R > event.x > x - R and y + R > event.y > y - R:
        score += 1
        lab['text'] = (name + ' - Score = ' + str(score))


new_ball()
canv.bind('<Button-1>', click)
lab = Label(root, text=(name + ' - Score = ' + str(score)), font="Arial 14")
lab.pack()
root.mainloop()
