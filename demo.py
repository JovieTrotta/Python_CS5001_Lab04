from turtle import *
import random
 
'''
Support Functions
'''
def move(x,y):
    penup()
    setpos(x,y)
    pendown()
 
def box(x=0,y=0,size=100):
    move(x,y)
    count = 0
    while count < 4:
        forward(size)
        left(90)
        count +=1
 
'''
Here's a warm up. Predict what this function will draw and then see if you were correct
'''
def shape1():
    count = 100
    while(count > 0):
        forward(100)
        setpos(xcor(),ycor()+1)
        backward(100)
        count -=1
 
 
'''
Challenge one: allow for the resizing of the drawn shape
 
'''

def shape1c(size, scale):
    count = size
    while(count > 0):
        forward(100)
        setpos(xcor(),ycor()+1)
        backward(100)
        count -= 1
    size = size * scale
    print(size)
 
 
'''
Challenge two:
First, you'll notice this function doesn't do anything. Why is that?
Fix it without running it.
Then, predict what this function will draw and see if you were correct.
'''
def shape2():
    count = 0
    while(count >= 0):
        forward(50)
        right(144)
        count +=1
 
 
'''
Challenge three: Explain the code
You might recognize this code segment or what it does, but how does it work? It might
be useful to print something and observe the results.
 
'''
def shape3():
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
 
'''
Challenge four: Explain the code to each other.
What could you print out to better understand what's going on?
Why is count2 set to 1 instead of 0?
Warning: don't base your lab assignment on this or it will take forever....
'''
def shape4():
    count = 5
    count2 = 1
    while(count > 0):
        while (count2 < 10):
            forward(5)
            if xcor() % 5 == 0 :
                if(isdown()):penup()
                else: pendown()
            count2 +=1
        count2 = 1
        move(0,ycor()+1)
        count -=1
        pendown()
 
 
'''
Challenge five: Create the inverse of shape4. That is have white spaces where
there were black and black where there was white.
'''
def shape4a():
    count = 5
    count2 = 1
 
'''
Challenge six: Use Shapes 4 and 4a to make a checkerboard pattern
'''
def shape5():
    print("checkers")
 
'''
Challenge seven: Stop the madness
Analyze the below code and explain what it is doing. Why is it an infinite loop?
Make it stop as soon as it draws outside the box.
'''
def shape6():
    box()
    move(50,50)
    while True:
        left(random.randint(0,359))
        forward(5)
 
'''
Challenge eight: Fix it
The below code runs forever. Fix it.
Then predict the shape and see if you were correct.
'''
def shape7():
    count = 0
    while count < 500:
        forward (count)
        left(91)
 
'''
Challenge nine: What's going on
Explain the below code segment to each other.
Alter the shape to something slightly more complex. Be creative.
 '''  
def shape8():
 
    def turn_and_draw(turn_angle, draw_pixels):
        left(turn_angle)
        forward(draw_pixels)
 
    color('blue', 'orange')
    begin_fill()
 
    side_count = 0
 
    while side_count < 3:
        pixels = 200
        if side_count == 0:
            angle = 0
        else:
            angle = 120
        turn_and_draw(angle, pixels)
        side_count += 1
    end_fill()
 
def main():
    speed(0)
    #shape1()
    #shape1c(100)
    #shape2()
    #shape2()
    shape3()
    #shape4()
    #shape4a()
    #shape5()
    #shape6()
    #shape8()
 
    '''
    Challenge 10:
    Analize surprise.py and predict the output
    Run the go function from surprise and see if you were correct
    Add a creative element all your own
    '''
    mainloop()
main()