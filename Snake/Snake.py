import turtle
import random

# Constants representing the move arrow keys.
KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_SPACE = \
    "Up", "Down", "Left", "Right", "space"


# The event that occurs when the up arrow key is pressed.
def up():
    global motion
    aim[0] = 0
    aim[1] = 20
    motion = "Up"
    update_motion()

# The event that occurs when the down arrow key is pressed.
def down():
    global motion
    aim[0] = 0
    aim[1] = -20
    motion = "Down"
    update_motion()

# The event that occurs when the left arrow key is pressed.
def left():
    global motion
    aim[0] = -20
    aim[1] = 0
    motion = "Left"
    update_motion()

# The event that occurs when the right arrow key is pressed.
def right():
    global motion
    aim[0] = 20
    aim[1] = 0
    motion = "Right"
    update_motion()

# The event that occurs when the space key is pressed.
def paused():
    global motion
    # If the status isn't Paused, make the snake stop and change status into Paused.
    if motion != "Paused":
        aim[0] = 0
        aim[1] = 0
        motion = "Paused"
    # If the status is Paused, make the snake move along the direction before Paused
    # and change status into the direction.
    else:
        # Find the direction before Paused and change motion in it.
        xd = snake[-1][0] - snake[-2][0]
        yd = snake[-1][1] - snake[-2][1]
        if xd > 0 and yd == 0:
            right()
        elif xd < 0 and yd == 0:
            left()
        elif xd == 0 and yd > 0:
            up()
        elif xd == 0 and yd < 0:
            down()
    update_motion()

# Bind snake movements to keyboard events.
def control():
    g_screen.onkey(up, KEY_UP)
    g_screen.onkey(down, KEY_DOWN)
    g_screen.onkey(left, KEY_LEFT)
    g_screen.onkey(right, KEY_RIGHT)
    g_screen.onkey(paused, KEY_SPACE)

# Create the main screen.
def create_screen():
    global g_screen
    g_screen = turtle.Screen()
    g_screen.title("Snake")  # Set screen's title.
    g_screen.setup(width=660, height=740) # Set screen's size.

# Draw the area which is used to show status.
def create_status_area():
    a = turtle.Turtle()
    a.hideturtle()
    a.penup()
    a.pensize(2)
    # Draw upper status area = 500 (w) x 80 (h).
    a.goto(-250, 210)
    a.pendown()
    a.goto(-250, 290)
    a.goto(250, 290)
    a.goto(250, 210)
    a.pensize(3)
    a.goto(-250, 210)

# Show Contact status.
def print_contact():
    global contact
    c.goto(-150, 250)
    c.write("Contact: %-6d" %contact, align="center", font=("Arial", 14, "normal"))

# Show Time status.
def print_time():
    global time
    t.goto(0, 250)
    t.write("Time: %-6d" % time, align="center", font=("Arial", 14, "normal"))

# Show Motion status.
def print_motion():
    global motion
    m.goto(150, 250)
    m.write("Motion: %-6s" % motion, align="center", font=("Arial", 14, "normal"))

# Refresh Contact status.
def update_contact():
    global contact
    # Judge whether the monster overlaps with the snake.
    for i in range(len(snake)):
        if monster.distance(snake[i][0], snake[i][-1]) < 20:
            contact += 1
            break
    # Refresh Contact times.
    c.clear()
    c.write("Contact: %-6d" % contact, align="center", font=("Arial", 14, "normal"))

# Refresh Time status.
def update_time():
    global time
    # Judge whether the game over, if so, stop the timer.
    if judge_win() or judge_over():
        return
    time += 1
    # Refresh time.
    t.clear()
    print_time()
    g_screen.ontimer(update_time, 1000)  # Repeat the function every 1 second.

# Refresh Motion status.
def update_motion():
    global motion
    if judge_win() or judge_over():  # Judge whether the game over, if so, stop change Motion status.
        return
    m.clear()
    m.write("Motion: %-6s" % motion, align="center", font=("Arial", 14, "normal"))

# Draw the area which is used to show game.
def create_motion_area():
    b = turtle.Turtle()
    b.hideturtle()
    b.penup()
    b.pensize(2)
    # Draw the lower motion area = 500 (w) x 500 (w).
    b.goto(-250, 210)
    b.pendown()
    b.goto(-250, -290)
    b.goto(250, -290)
    b.goto(250, 210)

# Print game introduction on the screen.
def print_introduction():
    global intr
    intr1 = "Welcome to the game named \"Snake\"..."
    intr2 = "You are going to use the 4 arrow keys to move the snake"
    intr3 = "around the screen, trying to consume all the food items"
    intr4 = "before the monster catches you..."
    intr5 = "Click anywhere on the screen to start the game, have fun!!"
    intr = turtle.Turtle()
    intr.hideturtle()
    intr.penup()
    # Print the game introduction in the upper half of the motion area.
    intr.goto(-200, 190)
    intr.write(intr1, font=("Arial", 12, "normal"))
    intr.goto(-200, 160)
    intr.write(intr2, font=("Arial", 12, "normal"))
    intr.goto(-200, 145)
    intr.write(intr3, font=("Arial", 12, "normal"))
    intr.goto(-200, 130)
    intr.write(intr4, font=("Arial", 12, "normal"))
    intr.goto(-200, 100)
    intr.write(intr5, font=("Arial", 12, "normal"))

# Randomly place all digital foods initial positions.
def initilize_food_items():
    global foods
    foods = []  # Store the coordinates of each food. The represented digit is index+1.
    # Make the position of the 9 digital food not repeated.
    n = 1
    while n < 10:
        f.goto(random.randrange(-240, 250, 20),
               random.randrange(-280, 200, 20))
        if list(f.position()) not in foods:
            foods.append(list(f.position()))
            # Make the coordinates correspond to the exact center of the number.
            f.right(90)
            f.forward(10)
            f.write('%s' % str(n), align="center", font=("Arial", 12, "normal"))
            f.left(90)
            n += 1
    g_screen.update()

# When one food is eaten, refresh it be disappeared on the screen.
def update_foods():
    f.clear() # Clear all foods.
    # Draw the food that hasn't been eaten yet.
    for i in foods:
        if i != "":
            f.goto(i)
            f.right(90)
            f.forward(10)
            f.write('%s' % str(foods.index(i) + 1), align="center", font=("Arial", 12, "normal"))
            f.left(90)

# Determine whether the snake has hit the wall or not.
def collide_wall():
    if snake[-1][0] >= 240 and motion == 'Right':  # Right wall.
        return True
    elif snake[-1][0] <= -240 and motion == 'Left':  # Left wall.
        return True
    elif snake[-1][1] >= 200 and motion == 'Up':  # Up wall.
        return True
    elif snake[-1][1] <= -280 and motion == 'Down':  # Down wall.
        return True
    return False

# Draw the snake on the screen.
def draw_snake():
    global snake
    # Use a list to simulate snake.
    # The last element in the list is the snake head coordinate.
    for i in range(len(snake)):
        s.goto(snake[i])
        if i == len(snake) - 1:  # Draw snake head.
            s.color("red", "red")
            s.stamp()
        else:  # Draw snake body.
            s.color("blue", "black")
            s.stamp()

# Refresh the move of the snake.
def snake_move():
    global snake_speed, snake, foods, motion
    if judge_over():  # If game over, the snake stop moving.
        return
    # If the status is Paused or the snake collide walls, 
    # the snake will stay put.
    if motion != "Paused":
        if collide_wall() == False:
            head = [snake[-1][0], snake[-1][1]]
            head = [head[0] + aim[0], head[1] + aim[1]]
            snake.append(head)
            snake.pop(0)
            if head in foods:  # If the snake eat food, the snake length will be extended.
                for i in range(len(foods)):
                    if head == foods[i]:
                        w = snake[0]
                        for j in range(i + 1):
                            snake.insert(0, w)
                        foods[i] = ""
                        update_foods()
                        break
    s.clearstamps()
    draw_snake()
    g_screen.update()
    # If win, the snake will stop moving.
    if judge_win():
        s.write("Winner!!", font=("Arial", 12, "normal"))
        return
    # The snake will motion slower while the tail being extended
    if snake[0][0] == snake[1][0] and snake[0][1] == snake[1][1] and "" in foods:
        snake_speed = 270
    else:  # Restore snake speed as it has finished been extened.
        snake_speed = 250
    g_screen.ontimer(snake_move, snake_speed)  # Repeat snake move every 0.3 second.

# Randomly place the monster's initial position.
def initilize_monster():
    monster.color("purple")
    # The monster can't get too close to the snake at first.
    x = random.randrange(-230, 231, 20)
    y = random.randrange(-270, -109, 20)
    monster.goto(x, y)
    monster.showturtle()

# Refresh the move of the monster.
def monster_move():
    global snake_speed, snake
    if judge_win():
        return
    # Obtain the current positions of monster and snake head.
    s_x = snake[-1][0]
    s_y = snake[-1][1]
    m_x = monster.xcor()
    m_y = monster.ycor()
    # Accroding to the positions, make the monster track the snake head.
    if s_x > m_x and s_y > m_y:
        if s_x - m_x <= s_y - m_y:
            monster.setheading(90)
        else:
            monster.setheading(0)
    elif s_x > m_x and s_y == m_y:
        monster.setheading(0)
    elif s_x > m_x and s_y < m_y:
        if s_x - m_x <= m_y - s_y:
            monster.setheading(270)
        else:
            monster.setheading(0)
    elif s_x == m_x and s_y > m_x:
        monster.setheading(90)
    elif s_x == m_x and s_y < m_y:
        monster.setheading(270)
    elif s_x < m_x and s_y > m_y:
        if m_x - s_x <= s_y - m_y:
            monster.setheading(90)
        else:
            monster.setheading(180)
    elif s_x < m_x and s_y == m_x:
        monster.setheading(180)
    elif s_x < m_x and s_y < m_y:
        if m_x - s_x <= m_y - s_y:
            monster.setheading(270)
        else:
            monster.setheading(180)
    monster.forward(20)
    g_screen.update()
    update_contact()
    # If the monster catch the snake head, game over, the monster stop moving.
    if judge_over():
        monster.write("Game Over!!", font=("Arial", 12, "normal"))
        return
    # Repeat monster move slightly faster or slower than snake.
    g_screen.ontimer(monster_move, 250 + random.randrange(-50, 101))

# Judge whether the snake consumes all foods and its body is fully extended or not.
def judge_win():
    if foods == [""] * 9:
        if snake[0][0] == snake[1][0] and snake[0][1] != snake[1][1]:
            return True
        elif snake[0][0] != snake[1][0] and snake[0][1] == snake[1][1]:
            return True
    return False

# Judge whether the monster catch up the snake head or not.
def judge_over():
    return monster.distance(snake[-1][0], snake[-1][1]) < 20

# The event to happen after clicking on the screen.
def start_game(x, y):
    intr.clear()  # Clear the introduction of game.
    g_screen.onclick(None)  # Release the clicking event.

    initilize_food_items()  # Place foods.
    
    control()  # Start keyboard events.

    g_screen.ontimer(snake_move, snake_speed)  # Start snake move.
    g_screen.ontimer(monster_move, 250 + random.randrange(-50, 101))  # Start monster move.
    g_screen.ontimer(update_time, 1000)  # Start update time.


if __name__ == "__main__":
    snake = [[0, -40]] * 6 # The initial length of snake is 6, including head.
    snake_speed = 250  # The initial speed of snake.
    aim = [0, 0]  # The initial motion status of snake is Paused.

    contact = 0
    time = 0
    motion = "Paused"

    create_screen()  
    g_screen.tracer(0)  # Turn off automatic refresh.

    # Create turtle object which is used to draw Time status.
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    # Create turtle object which is used to draw Motion status.
    m = turtle.Turtle()
    m.hideturtle()
    m.penup()

    # Create turtle object which is used to draw Contact status.
    c = turtle.Turtle()
    c.hideturtle()
    c.penup()

    # Create turtle object which is used to draw digital foods.
    f = turtle.Turtle()
    f.hideturtle()
    f.penup()

    # Create turtle object which is used to draw the snake.
    s = turtle.Turtle("square")
    s.color("red")
    s.pensize(20)
    s.penup()
    s.goto(0, -40)

    # Create turtle object which is used to draw the monster.
    monster = turtle.Turtle("square")
    monster.hideturtle()
    monster.penup()
    initilize_monster()

    create_status_area()
    create_motion_area()
    print_contact()
    print_time()
    print_motion()
    print_introduction()
    g_screen.update()
    
    g_screen.listen()  # Listen for events.
    g_screen.onclick(start_game)

    g_screen.mainloop()
