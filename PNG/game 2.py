import tkinter as tk
import random


WIDTH = 800
HEIGHT = 600
FLY_SIZE = 50
GAME_TIME = 30
MOVE_TIME = 2000


score = 0
remaining_time = GAME_TIME
fly_x = random.randint(0, WIDTH - FLY_SIZE)
fly_y = random.randint(0, HEIGHT - FLY_SIZE)


DIRECTIONS = ['up', 'down', 'left', 'right']



def move_fly():
    global fly_x, fly_y, current_direction, move_duration
    if move_duration > 0:
        if current_direction == 'up':
            fly_y -= 5
        elif current_direction == 'down':
            fly_y += 5
        elif current_direction == 'left':
            fly_x -= 5
        elif current_direction == 'right':
            fly_x += 5

        fly_x = max(0, min(fly_x, WIDTH - FLY_SIZE))
        fly_y = max(0, min(fly_y, HEIGHT - FLY_SIZE))

        canvas.coords(fly, fly_x, fly_y)


        move_duration -= 100
        root.after(100, move_fly)
    else:
        teleport_fly()


def teleport_fly():
    global fly_x, fly_y, current_direction, move_duration
    current_direction = random.choice(DIRECTIONS)
    fly_x = random.randint(0, WIDTH - FLY_SIZE)
    fly_y = random.randint(0, HEIGHT - FLY_SIZE)
    move_duration = MOVE_TIME
    canvas.coords(fly, fly_x, fly_y)
    move_fly()


def on_fly_click(event):
    global score
    if fly_x <= event.x <= fly_x + FLY_SIZE and fly_y <= event.y <= fly_y + FLY_SIZE:
        score += 1
        score_label.config(text=f"Счет: {score}")
        teleport_fly()


def update_timer():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        timer_label.config(text=f"Время: {remaining_time}")
        root.after(1000, update_timer)
    else:
        end_game()


def end_game():
    canvas.unbind("<Button-1>")
    canvas.delete(fly)
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"Игра окончена! Ваш счет: {score}", font=("Arial", 24),
                       fill="red")


root = tk.Tk()
root.title("Мухобойка")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

background_photo = tk.PhotoImage(file="Back.png")
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

fly_photo = tk.PhotoImage(file="Muha.png")
fly = canvas.create_image(fly_x, fly_y, image=fly_photo)

score_label = tk.Label(root, text=f"Счет: {score}", font=("Arial", 16))
score_label.pack(side=tk.LEFT, padx=20)

timer_label = tk.Label(root, text=f"Время: {remaining_time}", font=("Arial", 16))
timer_label.pack(side=tk.RIGHT, padx=20)


move_duration = MOVE_TIME
current_direction = random.choice(DIRECTIONS)
move_fly()
update_timer()
root.mainloop()
