from graph import *
import random as r

windowSize(500 , 750)
canvasSize(500 , 750)


def window():
    rect(260, 20, 490, 290, (0, 120, 120))
    rect(270, 30, 370, 90, (0, 0, 0))
    rect(270, 100, 370, 280, (0, 0, 0))
    rect(380, 30, 480, 90, (0, 0, 0))
    rect(380, 100, 480, 280, (0, 0, 0))
    pass

def cat():
    pass

def treadball():
    penColor(0, 0, 0)
    brushColor(150, 150, 150)
    circle(310, 650, 40)
    pass

def rect(x1, y1, x2, y2, color):
    penColor(color)
    brushColor(color)
    rectangle(x1, y1, x2, y2)

def circ(x, y, R, pen_color, brush_color):
    penColor(pen_color)
    brushColor(brush_color)
    circle(x, y, R)

def tread():
    x_coord = r.randint(270, 340)
    y_coord = r.randint(620, 680)
    return (x_coord, y_coord)

rect(0, 0, 500, 300, (200, 200, 0))
rect(0, 300, 500, 750, (120, 120, 0))
window()
treadball()
penColor(0, 0, 0)
for i in range(4):
    polyline([tread(), tread(), tread(), tread(), tread(), tread(), tread(), tread()])

run()