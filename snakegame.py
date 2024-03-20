from tkinter import *
import random

WIDTH = 500
HEIGHT = 700
SPEED = 80
SIZE = 30
BODY_PART = 3
SNAKE_COLOR = 'red'
FOOD_COLOR = 'blue'
BG_COLOR = 'white'

class Snake:
    
    def __init__(self):
        self.body_size = BODY_PART
        self.coordinates= []
        self.squares=[]

        for i in range(0,BODY_PART):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)

class Food:
    
    def __init__(self):

        x = random.randint(0,int((WIDTH/SIZE)-2)) * SIZE
        y = random.randint(0,int((HEIGHT/SIZE)-2)) * SIZE

        self.coordinates = [x,y]
        canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    x,y = snake.coordinates[0]

    if direction == "up":
        y -= SIZE
    elif direction == "down":
        y += SIZE
    elif direction == "right":
        x += SIZE
    elif direction == "left":
        x -= SIZE

    snake.coordinates.insert(0, (x,y))
    square = canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill=SNAKE_COLOR, tag="snake")
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 2
        label.config(text="Score : {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        gameover()
    else:
        window.after(SPEED, next_turn, snake, food)

def check_collision(snake):
    x,y = snake.coordinates[0]
    
    if x<0 or x>= WIDTH:
        return True
    elif y<0 or y>=HEIGHT:
        return True
        
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False
    
def gameover():
    canvas.delete(ALL)
    label.config(width=WIDTH, height=HEIGHT, text="GAME OVER\n Score: {}".format(score), font=('calibri',30,'bold'))


def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


window = Tk()
window.title("Snake Game")

sc_width = window.winfo_screenwidth()
sc_height = window.winfo_screenheight()

x = (sc_width//2) - 250
y = (sc_height//2) - 400

window.geometry('{}x{}+{}+{}'.format(WIDTH,HEIGHT,x,y))
window.resizable(False,False)

score = 0
direction = "down"

label = Label(window,text="Score : {}".format(score), pady=15, font=("Times", 18, 'bold'))
label.pack()

canvas = Canvas(window, height=HEIGHT, width=WIDTH, bg=BG_COLOR, relief=RIDGE, bd=5)
canvas.pack()

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()
next_turn(snake,food)

window.mainloop()