from graph import *

windowSize(500, 500)


def my_circle(x, y, R, pen_c, brush_c):
    penColor(pen_c)
    brushColor(brush_c)
    circle(x, y, R)


my_circle(250, 250, 200, (0, 0, 0), (255, 255, 0))
my_circle(180, 170, 30, (0, 0, 0), (255, 0, 0))
my_circle(320, 170, 30, (0, 0, 0), (255, 0, 0))
my_circle(180, 170, 10, (0, 0, 0), (0, 0, 0))
my_circle(320, 170, 10, (0, 0, 0), (0, 0, 0))

penColor(0, 0, 0)
brushColor(0, 0, 0)
rectangle(160, 330, 340, 360)

penColor(0, 0, 0)
brushColor(0, 0, 0)
polygon([(140, 100), (210, 160), (220, 165), (145, 90), (140, 100)])
polygon([(360, 100), (290, 160), (300, 165), (370, 90), (360, 100)])
run()