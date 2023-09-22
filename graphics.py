from math import *
from turtle import *
import turtle
image = "G:\Pictures\Screenshots\Screenshot (159) - Copy.png"
screen = Screen()

#screen.addshape(image)
#turtle.shape(image)

#register_shape("triangle", ((5,-3),(0,5),(-5,-3)))
turtle.mainloop()
color('black', 'yellow')
begin_fill()
old=0
m=int(input("slope : "))
c=int(input("y-intercept : "))
def intercept(a):
	left(90)
	forward(a)
	right(90)
intercept(c)
olds=tuple()
left(tan((pi/180)*m))
while True:
	for x in range(1):
		forward(1)
		a=pos()
		if(old!=a):
			olds+=(old,)
			print(a)
		elif(a in olds):
			print(olds)
			break
		old=a
	if abs(pos()) < 1:
		break
end_fill()
done()
