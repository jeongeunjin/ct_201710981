
# coding: utf-8

# In[1]:

import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


# In[2]:

def giyukAt(x,y,size):
    t1.goto(x,y)
    t1.fd(size)
    t1.rt(90)
    t1.fd(size)


# In[3]:

def nieunAt(x,y,size):
    t1.goto(x,y)
    t1.fd(size)
    t1.lt(90)
    t1.fd(size)


# In[4]:

def mieumAt():
    t1.penup()
    t1.goto(-300,300)
    t1.pendown()
    giyukAt(-300,300,100)
    t1.penup()
    t1.goto(-300,300)
    t1.pendown()
    nieunAt(-300,300,100)


# In[5]:

mieumAt()

