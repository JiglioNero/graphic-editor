import threading
import random

from PIL import ImageDraw, Image


def addNoise(factor, img):
    noiseImg = Image.new("RGB", img.size, "white")
    draw = ImageDraw.Draw(noiseImg)  # Создаем инструмент для рисования.
    width = img.size[0]  # Определяем ширину.
    height = img.size[1]  # Определяем высоту.
    pix = img.load()  # Выгружаем значения пикселей.

    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            if (a < 0):
                a = 0
            if (b < 0):
                b = 0
            if (c < 0):
                c = 0
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))

    return noiseImg
