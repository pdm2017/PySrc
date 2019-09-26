# turtle02.py

# 1)숫자를 입력받으세요
#   그 숫자의 해당 각형 도형을 만드세요

# 2) 다음의 color를 펜에 입혀보세요
colors = ['red','orange','yellow','green','blue','purple']

import turtle
ts = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle")
t.width(4)

n = int(input(" 몇 각형 도형을 만들까요? ==>"))

for i in range(n):
    print(i)
    t.pencolor(colors[i%len(colors)])
    t.left(360/n)
    t.forward(50)

ts.mainloop()



