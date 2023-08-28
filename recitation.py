'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab : 4 Patterns with While Loops

This program is part of our in-class recittion demonstration.
'''

import turtle as t

#sends the turtle to specific coordinates
def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#brings the turtle back to the home position
def resetTurtle():
    t.penup()
    t.home()
    t.pendown()

#creates a basic square
def square(x,y,scale):
    goto(x,y)
    count = 0 
    while count < 4:
        t.forward(scale)
        t.left(90)
        count += 1

#creates a grid frame
def frame(scale):
    square(0,0,scale)
    square(-scale,0,scale)
    square(-scale,-scale,scale)
    square(0,-scale,scale)

def windowSlates(x,y,scale,width):
    yPos = 0 
    while yPos < scale:
        if(yPos%width == 0):
            yPos = yPos + width
            goto(x,y)
        t.forward(scale)
        yPos += 1
        goto(x,yPos)

    def windowSlates(x,y,scale,width):
        yPos = 0 
        while yPos < scale:
            if(yPos%width == 0):
                yPos = yPos + width
                goto(x,y)
            t.forward(scale)
            yPos += 1
            goto(x,yPos)
    '''
    while yPos <= 10:
        goto(x,y)
        t.width(width)
        t.pendown()
        t.forward(scale)
        y += scale*0.1
        yPos += 1
    '''
'''
menu(): - print the following menu: 
1. Fill quadrant top left with horizontal bars
2. Fill quadrant top right with zebra stripes
3. Fill quadrant bottom left with stairs
4. Fill quadrant bottom right with wallpaper pattern
5. Fill all quadrants
6. Clear screen
7. Quit
'''

#1. max out the turtle drawing speed
#2. setup any variables you are going to need
#3. create an infinite while loop
#4. print user menu
#5. ask user for selection 
#6. validate user input
#7. call fill method based on user selection (See instructions below)
#8. or if the user selects 6, clear and redraw the frame
#9. or if the user selects 7, close the turtle window and exit the while loop


#this will execute the program
def main():
    #goto(-100,-80)
    t.speed(10)
    t.setup(800,800,None,None)
    frame(300)
    resetTurtle()
    windowSlates(-300,0,300,10)
    t.mainloop()
main()


