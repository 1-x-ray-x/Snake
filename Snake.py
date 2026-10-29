import turtle 
import time
import random

# delay to prevent turtle from going off screen
delay = 0.1

# score tracking
score = 0
high_score = 0

# set up the screen (window)
window = turtle.Screen()
window.title("Snake Game by Rayaan")
# background color
window.bgcolor("green")
# geometry
window.setup(width=600, height=600)
# turns off animation
window.tracer(0) # turns off screen updates so turtle not visible

# Snake head (turtle object)

head = turtle.Turtle()
#animation speed of turtle module (instant input)
head.speed(0)

head.shape("square")

head.color("black")
# doesnt draw anything, turtle module is used for drawing
head.penup()
# start at centre
head.goto(0,0)

# head direction stopped, so it sits until player moves
head.direction = "stop"

# creating food for the snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# creating body after eating apple
segments = []

# pen turtle to write the score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 | High Score: 0", align="center", font=("Courier", 24, "normal"))

# function for change direction of head
def go_up():
    # prevent snake from going into its own body
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

    
# function for movement
def move():
    if head.direction == "up":
        # adds 20 px to the y coordinate
        # does this when head moves up
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# keyboard binding calls function based off key press
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")


# Main game loop
while True:
    # updates so we see the turtle 
    window.update()
    
    # check for border collision and endgame if true
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        # pauses game
        time.sleep(1)
        # send back to 0
        head.goto(0,0)
        # stop the head
        head.direction = "stop"
        
        #disappear/hide segments after reset
        for segment in segments:
            # make it go off screen
            segment.goto(1000, 1000)
            
        # clear the segments list to make it disappear after reset
        segments.clear()
        
        # reset the delay
        delay = 0.1
        
        # reset the score
        score = 0
        pen.clear()
        pen.write("Score: {} | High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    
    # check if snake and food are touching
    if head.distance(food) < 20:
        # move the food to a new spot
        # 600 px wide and tall so 300 in both directons from 0,0
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        # sets the position of food to x,y
        food.goto(x,y)
        
        # add a segment to the snake body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        
        # shorten delay when player collides with food to prevent lag
        # turtle module is naturally laggy
        delay -= 0.001
        
        # increase score
        score += 1
        
        if score > high_score:
            high_score = score
        
        # this will draw ontop of the previous score unless you pen.clear()
        pen.clear()
        pen.write("Score: {} | High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        # append the new segment to the list of segments
        segments.append(new_segment)
    
    # attach segment to the head and move along with it
    # move the end segments first in reverse order
    # lets say 10 segments, 9 index(-1), 9 to 0 by 1 each time
    for index in range(len(segments) -1, 0, -1):
        # segment 9 moves to 8, 8 to 7 coords etc
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    # move segment 0 to where the head is, aka x and y cor of the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    # call the move func
    move()
    
    # check if head collides with body and reset if true
    for segment in segments:
        # distance to head
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
         
            for segment in segments:
                # make it go off screen
                segment.goto(1000, 1000)
                    
            # clear the segments list to make it disappear after reset
            segments.clear()
            
            # reset the delay
            delay = 0.1
         
            # reset the score
            score = 0
            pen.clear()
            pen.write("Score: {} | High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    
    # delays the turtle 
    time.sleep(delay)
    
#keeps window open
window.mainloop()
