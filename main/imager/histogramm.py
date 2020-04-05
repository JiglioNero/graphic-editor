"""Пользователь вводит имя файла с изображением,
гистограммы которого нужно построить.
Строятся гистограммы по каждому из каналов, по яркости(Luminance), и RGB гистограмма.
Программа строит гистограммы и сохраняет в текущей папке.
Полученные гистограммы практически не отличаются от гистограмм,
полученных в коммерческих программах
Для работы программы необходим Python 2.7 с установленной PIL"""
from PIL import Image, ImageDraw  # модули из PIL

def lum(c):  # цвет пиксела RGB -> значение яркости
    # формула, которая обычно используется для определения яркости
    return int(0.3 * c[0] + 0.59 * c[1] + 0.11 * c[2])


def r(c):  # цвет пиксела RGB -> значение R
    return c[0]


def g(c):  # цвет пиксела RGB -> значение G
    return c[1]


def b(c):  # цвет пиксела RGB -> значение B
    return c[2]


def getRGBhist(im):
    W = 256
    H = 200

    clrs = im.getcolors(im.size[0] * im.size[1])

    rharr = [0 for i in range(W)]
    gharr = list(rharr)
    bharr = list(rharr)
    for n, c in clrs:
        rharr[r(c)] += n
        gharr[g(c)] += n
        bharr[b(c)] += n
    harr = [(rharr[i] + gharr[i] + bharr[i]) / 3 for i in range(W)]

    W = len(harr)  # кол-во элементов массива
    hist = Image.new("RGB", (W, H), "white")  # создаем рисунок в памяти
    draw = ImageDraw.Draw(hist)  # объект для рисования на рисунке
    maxx = float(max(harr))  # высота самого высокого столбика
    if maxx == 0:  # столбики равны 0
        draw.rectangle(((0, 0), (W, H)), fill="black")
    else:
        for i in range(W):
            draw.line(((i, H), (i, H - harr[i] / maxx * H)), fill="black")  # рисуем столбики
    del draw  # удаляем объект
    return hist, im.size[0] * im.size[1],
