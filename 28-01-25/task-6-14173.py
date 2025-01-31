from turtle import *
screensize(2000, 2000)
tracer(0)
k = 20
up()

for i in range(2):
    down()
    for i in range(2):
        fd(8*k)
        rt(90)
        fd(8*k)
        rt(90)
    up()
    fd(6*k)
    rt(90)
    fd(6*k)
    lt(90)
rt(180)
fd(4*k)
down()
for i in range(4):
    fd(8*k)
    rt(270)

