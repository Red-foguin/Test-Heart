import math
from turtle import *

def hearta(k):
    return 12 * math.sin(k) ** 3

def heartb(k):
    return 10 * math.cos(k) - 4 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("black")
color("#f73487")
pensize(2)
hideturtle()

for i in range(1000):
    k = i / 100 * math.pi
    goto(hearta(k) * 20, heartb(k) * 20)
    dot(3)

done()
