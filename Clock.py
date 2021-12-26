
import turtle
import time

addis=turtle.Screen()
addis.bgcolor("#3fb1cf")

adaa=turtle.Turtle()
addisu=turtle.Turtle()
adaa.hideturtle()
addisu.hideturtle()
# the function below draws the circle part of our clock
def draw_circle(radius,pen_size):
       addisu.penup()
       addisu.goto(0,-radius)
       addisu.pendown()
       addisu.pensize(pen_size)
       addisu.circle(radius)
       addisu.penup()
       addisu.home()
       addisu.left(90)

'''draw clock pointer functions draws line that represents the 12 common oclocks on analog watches'''

def draw_clock_pointer(radius):
       for i in range(1,13):
       	addisu.right((30)*(i+1))
       	addisu.color("white")
       	addisu.penup()
       	addisu.forward(radius-40)
       	addisu.pendown()
       	addisu.pensize(10)
       	addisu.forward(20)
       	addisu.penup()
       	addisu.home()
       	addisu.left(90)
       


def draw_hour_arm(hour,h_arm_size):
        
        adaa.color("red")
        adaa.pensize(15)
        adaa.pendown()
#this line of code changes hour given to the function to degree and moves as hour changes
        angle=(hour/12)*360
        adaa.right(angle)
        adaa.forward(h_arm_size)
        adaa.backward(h_arm_size)
        adaa.right(90)
        
#draw minute arm
def draw_min_arm(minute,m_arm_size): 
	   adaa.color("green")
	   adaa.pensize(10)
#this changes minute to degree
	   angle=(minute/60)*360
	   adaa.right(angle)
	   adaa.forward(m_arm_size) 
	   adaa.home()
	   adaa.left(90)
#draw second arm	   
def draw_sec_arm(sec,arm_size):
	  adaa.color("#3560d0")
	  adaa.pensize(4)
	  angle=(sec/60)*360
	  adaa.right(angle)
	  adaa.forward(arm_size)
	  adaa.home()
	  adaa.setheading(90)

addis.tracer(0)

#calling functions
addisu.color("orange")
addisu.begin_fill()
draw_circle(300,2)
addisu.end_fill()
addisu.home()
addisu.color("black")
addisu.begin_fill()
draw_circle(250,2)
addisu.end_fill()
draw_clock_pointer(250)
#write my name
addisu.goto(-125,90)
addisu.color("gold")
addisu.write("Addisu_clock",font = ("Times",8,'normal'))

while True:
        hour=int(time.strftime("%I"))
        minute=int(time.strftime("%M"))
        sec=int(time.strftime("%S"))
        
        draw_hour_arm(hour,100)
        draw_min_arm(minute,150)
        draw_sec_arm(sec,200)
        addis.update()
        adaa.undo()
        time.sleep(0)
        adaa.clear()
       
	 

turtle.done()