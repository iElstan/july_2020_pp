from graph import *
import random as r


windowSize(500, 750)
canvasSize(500, 750)


def window():
    rect(260, 20, 490, 290, (0, 120, 120))
    rect(270, 30, 370, 90, (0, 0, 0))
    rect(270, 100, 370, 280, (0, 0, 0))
    rect(380, 30, 480, 90, (0, 0, 0))
    rect(380, 100, 480, 280, (0, 0, 0))


def cat():
    ovl(310, 400, 550, 440, (0, 0, 0), (210, 120, 100))
    ovl(80, 395, 350, 520, (0, 0, 0), (210, 120, 100))
    circ(80, 450, 55, (0, 0, 0), (210, 120, 100))
    circ(340, 500, 40, (0, 0, 0), (210, 120, 100))
    ovl(80, 495, 150, 530, (0, 0, 0), (210, 120, 100))
    ovl(370, 500, 390, 560, (0, 0, 0), (210, 120, 100))


def threadball():
    circ(310, 650, 40, (0, 0, 0), (150, 150, 150))
    for i in range(4):
        polyline([thread(), thread(), thread(), thread(), thread(), thread(), thread(), thread()])


def rect(x1, y1, x2, y2, color):
    penColor(color)
    brushColor(color)
    rectangle(x1, y1, x2, y2)


def circ(x, y, R, pen_color, brush_color):
    penColor(pen_color)
    brushColor(brush_color)
    circle(x, y, R)


def ovl(x1, y1, x2, y2, pen_color, brush_color):
    penColor(pen_color)
    brushColor(brush_color)
    oval(x1, y1, x2, y2)


def thread():
    x_coord = r.randint(270, 340)
    y_coord = r.randint(620, 680)
    return x_coord, y_coord


rect(0, 0, 500, 300, (200, 200, 0))
rect(0, 300, 500, 750, (120, 120, 0))
window()
threadball()
cat()

dy = 10
penColor(0, 0, 0)
for i in range(3):
    moveTo(70, 480)
    lineTo(15, 500 - dy)
    dy += 10


run()
