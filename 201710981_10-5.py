
# coding: utf-8

# In[1]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


# In[2]:

width=wn.window_width()
w3 = (width - 40) / 3
x1 = 0.0 - w3
x2 = 0.0
x3 = 0.0 + w3


# In[3]:

def drawTriangleAt(size,pos):
    t1.penup()
    t1.goto(pos,0)
    t1.setheading(0)
    t1.pendown()
    t1.rt(60)
    t1.fd(size)
    t1.rt(120)
    t1.fd(size)
    t1.rt(120)
    t1.fd(size)


# In[4]:

def drawPentagonAt(size,pos):
    t1.penup()
    t1.goto(pos,0)
    t1.setheading(0)
    t1.pendown()
    t1.rt(36)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)
    t1.rt(72)
    t1.fd(size)


# In[5]:

def drawStarAt(size,pos):
    t1.penup()
    t1.goto(pos,0)
    t1.setheading(0)
    t1.pendown()
    t1.rt(72)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)
    t1.rt(144)
    t1.fd(size)


# In[6]:

drawTriangleAt(100,x1)
drawPentagonAt(100,x2)
drawStarAt(100,x3)


# In[ ]:

wn.exitonclick()

