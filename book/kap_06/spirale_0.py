# spirale_1.py
from turtle import *

def spirale(x):
    forward(x)
    right(90)
    spirale(0.9*x) # rekursiver Aufruf
    return

speed(10)
spirale(200)
