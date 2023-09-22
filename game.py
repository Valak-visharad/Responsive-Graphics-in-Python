from turtle import *
import keyboard
left(90)
def right_d():
    right(5)
def left_d():
    left(5)
def conti():
    forward(2)
while(True):
    if keyboard.is_pressed("right"):
        right_d()
        conti()
    elif keyboard.is_pressed("left"):
        left_d()
        conti()
    else:
        conti()
    print(pos())
