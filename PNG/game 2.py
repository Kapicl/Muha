import tkinter as tk
import random

<<<<<<< HEAD
class FlyGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Fly Game")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        self.bg = tk.PhotoImage(file="Back.png")  # Фон
        self.fly_image = tk.PhotoImage(file="Muha.png")  # Муха
        self.swatter_image = tk.PhotoImage(file="Boyka.png")  # Мухобойка

        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()

        self.canvas.create_image(0, 0, anchor="nw", image=self.bg)

        self.score = 0
        self.fly_count = 0
        self.time_left = 20
        self.running = True
        self.fly = None
        self.fly_direction = [0, 0]

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack(anchor="nw")

        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_left} sec", font=("Arial", 14))
        self.timer_label.pack(anchor="ne")

        self.root.bind("<Motion>", self.move_swatter)
        self.root.bind("<Button-1>", self.hit_fly)

        self.swatter = self.canvas.create_image(0, 0, image=self.swatter_image, anchor="center")

        self.spawn_fly()
        self.update_timer()

    def move_swatter(self, event):
        self.canvas.coords(self.swatter, event.x, event.y)

    def spawn_fly(self):
        if not self.running:
            return

        if self.fly:
            self.canvas.delete(self.fly)

        x, y = random.randint(50, 550), random.randint(50, 350)
        self.fly = self.canvas.create_image(x, y, image=self.fly_image)
        self.fly_direction = [random.choice([-1, 1]) * random.randint(5, 10),
                              random.choice([-1, 1]) * random.randint(5, 10)]


        self.move_fly()
        self.root.after(1000, self.spawn_fly)

    def move_fly(self):
        if not self.running or not self.fly:
            return
=======

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
>>>>>>> 2d33884a9ab1c9c9754840d9b2e3da87a2d4042c

        x1, y1, x2, y2 = self.canvas.bbox(self.fly)
        dx, dy = self.fly_direction

<<<<<<< HEAD
        if x1 + dx < 0 or x2 + dx > 600:
            self.fly_direction[0] *= -1
        if y1 + dy < 0 or y2 + dy > 400:
            self.fly_direction[1] *= -1
=======

        move_duration -= 100
        root.after(100, move_fly)
    else:
        teleport_fly()
>>>>>>> 2d33884a9ab1c9c9754840d9b2e3da87a2d4042c

        self.canvas.move(self.fly, self.fly_direction[0], self.fly_direction[1])

<<<<<<< HEAD
        self.root.after(50, self.move_fly)
=======
def teleport_fly():
    global fly_x, fly_y, current_direction, move_duration
    current_direction = random.choice(DIRECTIONS)
    fly_x = random.randint(0, WIDTH - FLY_SIZE)
    fly_y = random.randint(0, HEIGHT - FLY_SIZE)
    move_duration = MOVE_TIME
    canvas.coords(fly, fly_x, fly_y)
    move_fly()
>>>>>>> 2d33884a9ab1c9c9754840d9b2e3da87a2d4042c

    def hit_fly(self, event):
        if self.fly:
            fly_coords = self.canvas.bbox(self.fly)
            swatter_coords = self.canvas.bbox(self.swatter)

<<<<<<< HEAD
            if (fly_coords[0] < swatter_coords[2] and
                fly_coords[2] > swatter_coords[0] and
                fly_coords[1] < swatter_coords[3] and
                fly_coords[3] > swatter_coords[1]):
=======
def on_fly_click(event):
    global score
    if fly_x <= event.x <= fly_x + FLY_SIZE and fly_y <= event.y <= fly_y + FLY_SIZE:
        score += 1
        score_label.config(text=f"Счет: {score}")
        teleport_fly()
>>>>>>> 2d33884a9ab1c9c9754840d9b2e3da87a2d4042c

                self.canvas.delete(self.fly)
                self.fly = None
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")

<<<<<<< HEAD
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left} sec")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()
=======
def update_timer():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        timer_label.config(text=f"Время: {remaining_time}")
        root.after(1000, update_timer)
    else:
        end_game()
>>>>>>> 2d33884a9ab1c9c9754840d9b2e3da87a2d4042c

    def end_game(self):
        self.running = False
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg)
        self.canvas.create_text(300, 200, text=f"Game Over!\nYour Score: {self.score}",
                                 font=("Arial", 24), fill="black")

<<<<<<< HEAD
if __name__ == "__main__":
    root = tk.Tk()
    game = FlyGame(root)
    root.mainloop()
=======
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
>>>>>>> 2d33884a9ab1c9c9754840d9b2e3da87a2d4042c
