# Simple Snake Game

# Part 1 Getting Started



import turtle # Importing Turtle Module
import time # Importing time to cause a delay
import random # Lets us choose random numbers

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @iNode.code") # Game Title
wn.bgcolor("green") #Background Color
wn.setup(width=600, height=600) # This is for sizing of Screen
wn.tracer(0) # Turns off screen updates/animations

# Snake head
head = turtle.Turtle() #Creating Turtle
head.speed(0) #Animation speed of turtle module (Move as fast as possible)
head.shape("triangle")
head.color("black")
head.penup() # Turtles were designed to draw lines, putting pen up so it doesnt draw lines
head.goto(0,0) # When the head starts you want it in the beginning of screen, turtles always appear at 0, 0, this is good practice
head.direction = "stop" # When game starts, turtle will sit in middle

# Snake food
food = turtle.Turtle() #Creating Turtle
food.speed(0) #Animation speed of turtle module (Move as fast as possible)
food.shape("circle") # Circle shape for food
food.color("red") # Alert player to grab color
food.penup() # Turtles were designed to draw lines, putting pen up so it doesnt draw lines
food.goto(0,100) # Starting away from center of screen

segments = []

# Pen //creating pen turtles to display score and high score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up(): # Function to change direction of head
    if head.direction != "down": # Prevention from snake crossing over itself
        head.direction = "up"

def go_down(): # Function to change direction of head
    if head.direction != "up": # Prevention from snake crossing over itself
        head.direction = "down"

def go_left(): # Function to change direction of head
    if head.direction != "right": # Prevention from snake crossing over itself
        head.direction = "left"

def go_right(): # Function to change direction of head
    if head.direction != "left": # Prevention from snake crossing over itself
        head.direction = "right"

def move(): # Calling function "move" because that is what we want the turtle to do
    if head.direction == "up": # When up is called, head will move up 20 on y axis
        y = head.ycor() # new variable Y named Y, cordinant of the variable
        head.sety(y + 20) # Turtle starts at 0, every time move function is called, if head direction is up, it will move by 20 on y axis each time

    if head.direction == "down": # When down is called, head will move down 20 on y axis
        y = head.ycor() # new variable Y named Y, cordinant of the variable
        head.sety(y - 20) # Turtle starts at 0, every time move function is called, if head direction is down, it will move by 20 on y axis each time

    if head.direction == "left": # When left is called, head will move left 20 on x axis
        x = head.xcor() # new variable x named x, cordinant of the variable
        head.setx(x - 20) # Turtle starts at 0, every time move function is called, if head direction is left, it will move by 20 on x axis each time

    if head.direction == "right": # When right is called, head will move right 20 on x axis
        x = head.xcor() # new variable x named x, cordinant of the variable
        head.setx(x + 20) # Turtle starts at 0, every time move function is called, if head direction is right, it will move by 20 on x axis each time

# Keyboard bindings__This connects a key press with a particular function
wn.listen() # Telling window to listen for key presses
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True: # It repeats over and over
    wn.update() # Everytime through this loop, it updates screen


    # Overview of what is happening here
    # When we touch the food, we are measuring distance(<20)
    # We create a new segment, and we append it to the segment list
    # Starting at the last segment

    # Check for a collision with the boarder
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290: # If head crosses these coardinants, execute this block
        time.sleep(1) # Pauses game for 1 second
        head.goto(0,0) # Sets head back at 0,0 x & y
        head.direction = "stop" # Stops the head for moving

        # Hide the segments
        for segment in segments: #Goes through list of segments, starts at 0
            segment.goto(1000, 1000) # Moving segments off screen

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()  # Clearing for new score to be displayed when you die 
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # Writing updated score

    # Check for collisions with the food
    if head.distance(food) < 20: # Basic turtle shape is 20x20, built in function to measure distance between turtles
        # Move the food to a random spot
        x = random.randint(-290,290) # size is 300x300, so 290 is to keep food from going off screen
        y = random.randint(-290,290) # size is 300x300, so 290 is to keep food from going off screen
        food.goto(x, y) # The food will go to a random spot based on what numbers the random tool chose

        # Add a segment
        new_segment = turtle.Turtle() # This segment is also a turtle object
        new_segment.speed(0) # Animation speed
        new_segment.shape("square") # Matches rest of snake
        new_segment.color("grey") # To show color difference in body for addition to said body
        new_segment.penup() # Doesnt draw on screen
        segments.append(new_segment) # append our new segment to our lists of segments

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score: # If score is greater than high score, set high score to current score
            high_score = score # if greater, its new high score
            
        pen.clear()  # Clears so there is no overlap  
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # Writing updated score

    # Move the end segments first in reverse order //This will only work if there are more than one segment
    for index in range(len(segments) - 1, 0, -1): # [list count 0-9]Takes the length -1 to get 9, 9 down to 1, zero is non inclusive, -1 to go down by 1 each time
        x = segments[index-1].xcor() # segments are turtles, they have x & y cordinates
        y = segments[index-1].ycor() # segments are turtles, they have x & y cordinates 
        segments[index].goto(x, y) # This loop goes through all segments

    # Move segment 0 to where the head is
    if len(segments) > 0: # If length is greater than zero, we want first segment-index 0, to move where the head is
        x = head.xcor()  
        y = head.ycor() 
        segments[0].goto(x,y) # moving first segment to head

    move() # Calling function move

    # Check for head collisions witht the body segments
    for segment in segments: # This will go through segments, starts at 0
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments: #Goes through list of segments, starts at 0
                segment.goto(1000, 1000) # Moving segments off screen

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            pen.clear()  # Clearing for new score to be displayed when you die 
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) # Writing updated score

    time.sleep(delay) # Taking time tool to make the app sleep for the amount of time set to variable delay

wn.mainloop()

