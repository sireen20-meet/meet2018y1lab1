import turtle

turtle.penup() #Pick up the pen so it doesn’t 
               #draw
turtle.goto(-200,-100) #Move the turtle to the 
 #position (-200, -100) 
 #on the screen
turtle.pendown() #Put the pen down to start
                 #drawing
#Draw the M:
turtle.goto(-200,-100+200) 
turtle.goto(-200+50,-100) 
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)

turtle.penup()
turtle.goto(-50,-100)
turtle.pendown()
turtle.goto(-50,100)
turtle.goto(50,100)
turtle.penup()
turtle.goto(50,-10)
turtle.pendown()
turtle.goto(-50,-10)
turtle.penup()
turtle.goto(50,-100)
turtle.pendown()
turtle.goto(-50,-100)
turtle.penup()

turtle.goto(100,-100)

turtle.pendown()
turtle.goto(100,100)
turtle.goto(200,100)
turtle.penup()
turtle.goto(200,-10)
turtle.pendown()
turtle.goto(100,-10)
turtle.penup()
turtle.goto(200,-100)
turtle.pendown()
turtle.goto(100,-100)
turtle.penup()

turtle.goto(325,-100)
turtle.pendown()
turtle.goto(325,100)
turtle.goto(250,100)
turtle.goto(400,100)
turtle.mainloop()
