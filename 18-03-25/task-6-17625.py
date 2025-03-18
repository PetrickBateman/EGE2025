from turtle import *

screensize(2000, 2000)
tracer(0)
k = 20
lt(90)

down()
for i in range(10):
    fd(22 * k)
    rt(90)
    fd(16 * k)
    rt(90)
up()
fd(k)
rt(90)
fd(k)
lt(90)
down()
for i in range(10):
    fd(72 * k)
    rt(90)
    fd(79 * k)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')

done()