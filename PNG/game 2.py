import tkinter as tk
import random

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

        x1, y1, x2, y2 = self.canvas.bbox(self.fly)
        dx, dy = self.fly_direction

        if x1 + dx < 0 or x2 + dx > 600:
            self.fly_direction[0] *= -1
        if y1 + dy < 0 or y2 + dy > 400:
            self.fly_direction[1] *= -1

        self.canvas.move(self.fly, self.fly_direction[0], self.fly_direction[1])

        self.root.after(50, self.move_fly)

    def hit_fly(self, event):
        if self.fly:
            fly_coords = self.canvas.bbox(self.fly)
            swatter_coords = self.canvas.bbox(self.swatter)

            if (fly_coords[0] < swatter_coords[2] and
                fly_coords[2] > swatter_coords[0] and
                fly_coords[1] < swatter_coords[3] and
                fly_coords[3] > swatter_coords[1]):

                self.canvas.delete(self.fly)
                self.fly = None
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left} sec")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.running = False
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg)
        self.canvas.create_text(300, 200, text=f"Game Over!\nYour Score: {self.score}",
                                 font=("Arial", 24), fill="black")

if __name__ == "__main__":
    root = tk.Tk()
    game = FlyGame(root)
    root.mainloop()
