# Bar01.py
import turtle

def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

#data = [120,56,200,156,23]
file = open("Bar.txt",'r')
str= file.read()
data= str.split(',')
for i in range(0,len(data)):
    data[i] = int(data[i])
print(data)

file.close()

t = turtle.Turtle()
t.color("blue")
t.fillcolor ("red")

t.pensize(3)

for d in data:
    drawBar(d)

turtle.mainloop()
