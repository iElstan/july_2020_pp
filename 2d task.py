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


def cat(size, color, eye_color):
    ovl(35, 470, 60, 520, (0, 0, 0), color)  # лапа слева
    ovl(310, 400, 550, 440, (0, 0, 0), color)  # нога
    ovl(80, 395, 350, 520, (0, 0, 0), color)  # тело
    circ(80, 450, 55, (0, 0, 0), color)  # голова
    circ(340, 500, 40, (0, 0, 0), color)  # ляжка
    ovl(80, 495, 150, 530, (0, 0, 0), color)  # лапа справа
    ovl(370, 500, 390, 560, (0, 0, 0), color)  # хвост
    circ(55, 440, 15, (0, 0, 0), eye_color)  # глаз
    circ(105, 440, 15, (0, 0, 0), eye_color)  # глаз
    ovl(60, 430, 65, 450, (0, 0, 0), (0, 0, 0))  # зрачек
    ovl(110, 430, 115, 450, (0, 0, 0), (0, 0, 0))  # зрачек
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


def circ(x, y, R, pen_color, brush_color):
    penColor(pen_color)
    brushColor(brush_color)
    circle(x, y, R)


def ovl(x1, y1, x2, y2, pen_color, brush_color):
    penColor(pen_color)
    brushColor(brush_color)
    oval(x1, y1, x2, y2)


rect(0, 0, width, width / 5 * 3, (200, 200, 0))
rect(0, width / 5 * 3, width, height, (120, 120, 0))
window(width / 2, 0, (50, 50, 100), (0, 0, 0))
threadball(310, 650, 40, (0, 0, 0), (150, 150, 150))
cat(1, (210, 120, 100), (100, 190, 100))

run()
