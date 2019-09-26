# turtle05.py
import turtle as t
colors = ["red", "purple", "blue", "green", "yellow", "orange" ]

t.shape('turtle')
t.speed('fastest')
for i in range(300):
    t.pencolor(colors[i % len(colors)])
    t.forward(i)
    t.right(91)

t.mainloop()