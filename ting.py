import turtle
import sys
import os

def tortle(size, rotation, rotationl, repeat):
    turtle.bgcolor("black")
    turtle.pencolor("white")
    for i in range(repeat):
        turtle.rt(rotation)
        turtle.forward(size)
        turtle.rt(rotationl)
    turtle.getscreen().getcanvas().postscript(file='input.ps')
    os.system('gswin64 -o output.png -sDEVICE=pngalpha -r300 input.ps')

size = int(sys.argv[1])
rotat = int(sys.argv[2])
rotatl = int(sys.argv[3])
times = int(sys.argv[4])

tortle(size, rotat, rotatl, times)
