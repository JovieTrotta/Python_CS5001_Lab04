'''
Jovienne Trotta
CS 5001 | Fall 2022
5001 Lab : 4 Patterns with While Loops

This program contains my pattern and driver functions. 
'''

import turtle as t
import sys

#sends the turtle to specific coordinates
def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#sends the turtle to the home position
def go_home():
    t.penup()
    t.home()
    t.pendown()

#brings the turtle back to the home position and clears the screen
def reset_turtle():
    t.clear()
    go_home()

#creates a basic square
def square(x,y,square_size):
    goto(x,y)
    count = 0 
    while count < 4:
        t.forward(square_size)
        t.left(90)
        count += 1
    go_home()

#creates a grid frame
def frame(square_size):
    t.setup(1.0,1.0,None,None)
    t.speed(10)
    square(0,0,square_size)
    square(-square_size,0,square_size)
    square(-square_size,-square_size,square_size)
    square(0,-square_size,square_size)
    go_home()

#creates horizontal stripes in the top left quadrant
def window_slates(x,y,slate_size,square_size):
    t.speed(10)
    t.pencolor("pink")
    yPos = 0 
    while yPos < square_size:
        if(yPos % slate_size == 0):
            yPos = yPos + slate_size
            goto(x,y)
        t.forward(square_size)
        yPos += 1
        goto(x,yPos)
    go_home()

#creates zebra stripes in the top right quadrant
def zebra_stripes(x,y,stripe_size,square_size):
    t.speed(10)
    t.pencolor("purple")
    xPos = 0 
    t.left(90)
    while xPos < square_size:
        if(xPos % stripe_size == 0):
            xPos = xPos + stripe_size
            goto(x,y)
        t.forward(square_size)
        xPos += 1
        goto(xPos,y)
    go_home()

#creates a staircase in the bottom left quadrant
def steps(x,y,step_size):
    t.speed(10)
    t.pencolor("yellow")
    goto(x,y)
    xPos = x
    yPos = y
    while xPos < 0:
        if xPos + step_size > 0:
            t.forward(step_size - (xPos % step_size))
            break
        t.forward(step_size)
        t.up()
        t.left(90)
        t.forward(step_size)
        t.right(90)
        t.down()
        xPos += step_size
    goto(x,y)
    while yPos < 0:
        if yPos + step_size > 0:
            t.forward(step_size - (yPos % step_size))
            break
        t.up
        t.forward(step_size)
        t.down()
        t.left(90)
        t.forward(step_size)
        t.right(90)
        yPos += step_size
    go_home()

#creates a wall paper pattern in the bottom right quadrant
def wall_paper(x,y,radius):
    t.pencolor("light blue")
    x -= radius
    xCount = x
    yCount = y
    goto(x,y)
    while (xCount - radius >= 0) and (yCount + (1.8*radius) < 0):
        t.speed(10)
        t.circle(radius)
        t.up()
        t.back(radius)
        t.down()
        xCount -= radius
        if xCount - radius < 0:
            xCount = x
            y += radius
            yCount += radius
            goto(x,y)
            continue
        elif (yCount + radius >= 0):
            #((0 - yCount) >= radius):
            #(yCount + radius + (yCount % radius):
            break
    go_home()

#quad1-4 are boolean variables letting the function know which quadrants to fill and window_size is the size of square to be filled
#this was used for testing purposes only, not in my final main function
def fill(quad1, quad2, quad3, quad4, window_size):
    frame(window_size)
    while quad1 == True:
        window_slates(-window_size,0,int(input("Please enter the slate width: \n")),window_size)
        break
    while quad2 == True:
        zebra_stripes(window_size,0,int(input("Please enter the stripe width: \n")),window_size)
        break
    while quad3 == True: 
        steps(-window_size,-window_size,int(input("Please enter the stair size: \n")))
        break
    while quad4 == True: 
        wall_paper(window_size,-window_size,int(input("Please enter the radius size: \n")))
        break

#creates a menu where users can select what action they want to take
def menu(menu_choice,square_size):
    if menu_choice == "one" or menu_choice == "1":
        window_slates(-square_size,0,int(input("Please enter the slate width: \n")),square_size)
        t.done()
    elif menu_choice == "two" or menu_choice == "2":
        zebra_stripes(square_size,0,int(input("Please enter the stripe width: \n")),square_size)
        t.done()
    elif menu_choice == "three" or menu_choice == "3":
        steps(-square_size,-square_size,int(input("Please enter the stair size: \n")))
        t.done()
    elif menu_choice == "four" or menu_choice == "4":
        wall_paper(square_size,-square_size,int(input("Please enter the radius size: \n")))
        t.done()
    elif menu_choice == "five" or menu_choice == "5":
        window_slates(-square_size,0,int(input("Please enter the slate width: \n")),square_size)
        zebra_stripes(square_size,0,int(input("Please enter the stripe width: \n")),square_size)
        steps(-square_size,-square_size,int(input("Please enter the stair size: \n")))
        wall_paper(square_size,-square_size,int(input("Please enter the radius size: \n")))
        t.done()
    elif menu_choice == "six" or menu_choice == "6":
        reset_turtle()
        t.done()
    elif menu_choice == "seven" or menu_choice == "7":
        sys.exit()
    else:
        print("Please select a number from 1 through 7.")
        sys.exit()

#this is my driver function
def main():
    #fill(True,True,True,True,200)
    while True:
        try:
            square_size = int(input("Please enter the frame size: \n"))
        except ValueError:
            print("You need to enter a number.")
            continue
        else:
            break
    frame(square_size)
    menu_choice = input("Please make a selection: \n...'1' to fill quadrant top left with horizontal bars \n...'2' to fill quadrant top right with zebra stripes \n...'3' to fill quadrant bottom left with stairs \n...'4' to fill quadrant bottom right with wallpaper pattern \n...'5' to fill all quadrants \n...'6' to clear the screen \n...'7' to quit \n: ")
    menu(menu_choice,square_size)
    t.mainloop()
main()