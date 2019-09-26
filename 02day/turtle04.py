# turtle04.py
import turtle as t
colors = ["red", "purple", "blue", "green", "yellow", "orange" ]

n = 60
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.pencolor(colors[i % len(colors)])
    t.circle(120)
    t.right(360/n)

t.mainloop()