



# Python program to draw square  
# using Turtle Programming 
import turtle  

s = turtle.Screen()  
turtle.speed(500)
#for i in range(4): 
#    skk.forward(50) 
#    skk.right(90) 

#turtle.done() 
class Sto:
  def __init__(self,tt,ll):
    self.t=tt
    self.l=ll
  l=1

st = Sto(turtle.Turtle(),1)
#tsr = [Sto(turtle.Turtle())] 
#tsl = [Sto(turtle.Turtle())] 


ts = [Sto(turtle.Turtle(),1)] 

au=45

def update(t):
  t.t.forward(10)
  t.t.left(au*t.l)
  #t.l*=-1
  print(t.l)

def newt(t):
  nt=Sto(turtle.Turtle(),t.l*1.2)
  nt.t.up()
  x,y=t.t.position()
  print(x,y)
  nt.t.goto(x,y)
  nt.t.down()
  nt.t.left(au*nt.l)
  nt.t.forward(10)
  #nt.t.speed(500)
  ts.append(nt)
  

for i in range(4):
  st.t.forward(10)
  st.l*=-1
  newt(st);st.l*=-1
  newt(st)

for i in range(2):
  for t in ts: 
    t.t.speed(500)
    update(t)
    newt(t)
    print(' ')
    
  

for i in range(10):
  for t in ts: 
    update(t)
    print(' ')
    
  
turtle.up()
turtle.goto(-100,-100)
for t in ts: 
  t.t.up()
  t.t.goto(-100,-100)
  

