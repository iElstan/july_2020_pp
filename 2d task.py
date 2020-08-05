from graph import *

width = 500
height = 750
windowSize(width, height)
canvasSize(width, height)


def window(x, y, frame_color, outside_color):
    rect(x + width / 50, y + height / 35,
         x + width / 2 - width / 50, y + height / 2.5 - height / 75,
         frame_color
         )
    rect(x + width / 25, y + height / 25,
         x + width / 4 - width / 100, y + height * 10 / 83,
         outside_color
         )
    rect(x + width / 25, y + height / 7.5,
         x + width / 4 - width / 100, 280,
         outside_color
         )
    rect(x + width / 4 + width / 100, y + height / 25,
         x + width / 2 - width / 25, y + height * 10 / 83,
         outside_color
         )
    rect(x + width / 4 + width / 100, y + height / 7.5,
         x + width / 2 - width / 25, y + height / 2.5 - height * 2 / 75,
         outside_color
         )


def cat(x, y, r, pen_color, color, eye_color):
    ovl(x / 2, y,
        x * 3 / 4, y + y / 6,
        pen_color, color
        )  # лапа слева
    ovl(x * 3, y - y / 12,
        x * 6, y,
        pen_color, color
        )  # хвост
    ovl(x, y - y / 9,
        x * 4, y + y / 6,
        pen_color, color
        )  # тело
    circ(x, y, r,
         pen_color, color
         )  # голова (80, 450, 55)
    circ(x * 3.6, y + y / 9, r / 1.375,
         pen_color, color
         )  # ляжка
    ovl(x, y + y / 9,
        x * 2, y + y / 6,
        pen_color, color
        )  # лапа справа
    ovl(x * 3.85, y + y / 9,
        x * 4.1, y + y * 2 / 9,
        pen_color, color)  # нога
    circ(x / 1.4, y - y / 45, r / 3.67,
         pen_color, eye_color
         )  # глаз
    circ(x * 1.32, y - y / 45, r / 3.67,
         pen_color, eye_color
         )  # глаз
    ovl(x * 3 / 4, y - y * 2 / 45,
        x / 1.23, y,
        pen_color, pen_color)  # зрачек
    ovl(x * 1.375, y - y * 2 / 45,
        x * 1.44, y,
        pen_color, pen_color)  # зрачек
    dy = 10
    penColor(0, 0, 0)
    for i in range(3):  # усы
        moveTo(70, 480)
        lineTo(15, 500 - dy)
        moveTo(90, 480)
        lineTo(145, 500 - dy)
        dy += 10
    brushColor(210, 180, 180)
    polygon([(100, 410), (120, 420), (130, 380)])  # уши
    polygon([(60, 410), (40, 420), (30, 380)])  # уши
    polygon([(75, 460), (85, 460), (80, 467)])  # нос
    line(80, 467, 80, 485)


def threadball(x, y, r, pen_color, brush_color):
    circ(x, y, r, pen_color, brush_color)
    dx = r / 4
    dy = r / 4
    for i in range(3):
        polyline(((x - r * 3 / 8 + dx, y - r * 7 / 8),
                  (x + dx, y - r / 8),
                  (x + r / 8 + dx, y + r * 3 / 8)
                  )
                 )
        polyline(((x - r * 3 / 4, y - r / 4 + dy),
                  (x - r / 4, y - r / 2 + dy),
                  (x + r / 4, y - 5 / 8 + dy)
                  )
                 )
        dx += r / 4
        dy += r / 4
    polyline(((x - r, y),
              (x - r * 2, y - r / 8),
              (x - r * 14 / 8, y + r * 3 / 8),
              (x - r * 21 / 8, y + r * 3 / 8)
              )
             )


def rect(x1, y1, x2, y2, color):
    penColor(color)
    brushColor(color)
    rectangle(x1, y1, x2, y2)


def circ(x, y, r, pen_color, brush_color):
    penColor(pen_color)
    brushColor(brush_color)
    circle(x, y, r)


def ovl(x1, y1, x2, y2, pen_color, brush_color):
    penColor(pen_color)
    brushColor(brush_color)
    oval(x1, y1, x2, y2)

size = 80
rect(0, 0, width, width / 5 * 3, (200, 200, 0))
rect(0, width / 5 * 3, width, height, (120, 120, 0))
window(width / 2, 0, (50, 50, 100), (0, 0, 0))
threadball(310, 650, 40, (0, 0, 0), (150, 150, 150))
cat(size, 5.625 * size, 0.69 * size, (0, 0, 0), (210, 120, 100), (100, 190, 100))

run()
