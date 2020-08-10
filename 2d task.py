from graph import *
import time

width = 1000
height = 1000
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
         x + width / 4 - width / 100, y + height / 2.5 - height * 2 / 75,
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
    ovl(x - r / 2, y,
        x, y + abs(r) * 4 / 3,
        pen_color, color
        )  # лапа слева
    ovl(x + r * 4, y - abs(r),
        x + r * 8, y,
        pen_color, color
        )  # хвост
    ovl(x, y - abs(r) * 4 / 3,
        x + r * 5, y + abs(r) * 4 / 3,
        pen_color, color
        )  # тело
    circ(x, y, r,
         pen_color, color
         )  # голова (80, 450, 55)
    circ(x + r * 4.3, y + abs(r) * 3 / 4, r * 3 / 4,
         pen_color, color
         )  # ляжка
    ovl(x + r / 3, y + abs(r) * 3 / 4,
        x + r * 3 / 2, y + abs(r) * 4 / 3,
        pen_color, color
        )  # лапа справа
    ovl(x + r * 4.8, y + abs(r),
        x + r * 5.1, y + abs(r) * 2,
        pen_color, color)  # нога
    circ(x - r / 2.5, y, r / 3.67,
         pen_color, eye_color
         )  # глаз
    circ(x + r / 2.5, y, r / 3.67,
         pen_color, eye_color
         )  # глаз
    ovl(x - r / 2.7, y - abs(r) / 5,
        x - r / 3.3, y + abs(r) / 5,
        pen_color, pen_color
        )  # зрачек
    ovl(x + r / 2, y - abs(r) / 5,
        x + r / 2.3, y + abs(r) / 5,
        pen_color, pen_color
        )  # зрачек
    dy = abs(r) / 5
    penColor(0, 0, 0)
    for i in range(3):  # усы
        moveTo(x - r / 6, y + abs(r) / 2)
        lineTo(x - r * 3 / 2, y + abs(r) - dy)
        moveTo(x + r / 6, y + abs(r) / 2)
        lineTo(x + r * 3 / 2, y + abs(r) - dy)
        dy += abs(r) / 5
    brushColor(210, 180, 180)
    polygon([(x + r * 4 / 5, y - abs(r) / 2),
             (x + r / 2, y - abs(r) * 3 / 5),
             (x + r, y - abs(r) * 1.2)
             ]
            )  # уши
    polygon([(x - r * 4 / 5, y - abs(r) / 2),
             (x - r / 2, y - abs(r) * 3 / 5),
             (x - r, y - abs(r) * 1.2)
             ]
            )  # уши
    polygon([(x - r / 10, y + abs(r) / 2.2),
             (x + r / 10, y + abs(r) / 2.2),
             (x, y + abs(r) / 1.8)
             ]
            )  # нос
    line(x, y + abs(r) / 1.8, x, y + abs(r) * 3 / 4)


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


rect(0, 0, width, width / 5 * 3, (200, 200, 0))
rect(0, width / 5 * 3, width, height, (120, 120, 0))
window(width / 2, 0, (50, 50, 100), (0, 0, 0))
threadball(310, 650, 40, (0, 0, 0), (150, 150, 150))
threadball(600, 400, 10, (0, 0, 0), (150, 150, 150))
threadball(100, 320, -70, (0, 0, 0), (150, 150, 150))
cat(80, 450, 50, (0, 0, 0), (210, 120, 100), (100, 190, 100))
cat(300, 500, -30, (0, 0, 0), (210, 120, 100), (100, 190, 100))
c = cat(500, 600, 70, (0, 0, 0), (20, 40, 40), (100, 100, 240))

init_x = 100
init_y = 850
dx = 0
dy = 0

coords(c)

for i in range(100):
    # penColor(120, 120, 0)
    # brushColor(120, 120, 0)
    # rectangle(100 + dx + 20, 800, init_x - dx - 20, 900)
    dx += 10
    moveObjectTo(c, init_x + dx, init_y + dy)
    update()
    time.sleep(0.1)

run()
