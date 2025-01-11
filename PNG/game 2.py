import tkinter as tk
import random

# Параметры окна
WIDTH = 800
HEIGHT = 600
FLY_SIZE = 50
GAME_TIME = 30  # Время игры в секундах
MOVE_TIME = 2000  # Время движения мухи в одной позиции (в миллисекундах)

# Глобальные переменные
score = 0
remaining_time = GAME_TIME
fly_x = random.randint(0, WIDTH - FLY_SIZE)
fly_y = random.randint(0, HEIGHT - FLY_SIZE)

# Направления для случайного движения
DIRECTIONS = ['up', 'down', 'left', 'right']


# Функция для обновления позиции мухи
def move_fly():
    global fly_x, fly_y, current_direction, move_duration
    if move_duration > 0:
        # Двигаем муху в выбранном направлении
        if current_direction == 'up':
            fly_y -= 5
        elif current_direction == 'down':
            fly_y += 5
        elif current_direction == 'left':
            fly_x -= 5
        elif current_direction == 'right':
            fly_x += 5

        # Ограничиваем движение в пределах экрана
        fly_x = max(0, min(fly_x, WIDTH - FLY_SIZE))
        fly_y = max(0, min(fly_y, HEIGHT - FLY_SIZE))

        canvas.coords(fly, fly_x, fly_y)

        # Уменьшаем оставшееся время движения в текущем направлении
        move_duration -= 100
        root.after(100, move_fly)
    else:
        # Телепортация в новое место
        teleport_fly()


# Функция для телепортации мухи в новое место и направления
def teleport_fly():
    global fly_x, fly_y, current_direction, move_duration
    # Выбираем случайное направление
    current_direction = random.choice(DIRECTIONS)
    # Телепортируем муху в случайную позицию
    fly_x = random.randint(0, WIDTH - FLY_SIZE)
    fly_y = random.randint(0, HEIGHT - FLY_SIZE)
    # Устанавливаем время на движение в новом направлении
    move_duration = MOVE_TIME
    canvas.coords(fly, fly_x, fly_y)
    move_fly()


# Обработчик клика по мухе
def on_fly_click(event):
    global score
    if fly_x <= event.x <= fly_x + FLY_SIZE and fly_y <= event.y <= fly_y + FLY_SIZE:
        score += 1
        score_label.config(text=f"Счет: {score}")
        teleport_fly()


# Функция для обновления таймера
def update_timer():
    global remaining_time
    if remaining_time > 0:
        remaining_time -= 1
        timer_label.config(text=f"Время: {remaining_time}")
        root.after(1000, update_timer)
    else:
        end_game()


# Завершение игры
def end_game():
    canvas.unbind("<Button-1>")
    canvas.delete(fly)
    canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"Игра окончена! Ваш счет: {score}", font=("Arial", 24),
                       fill="red")


# Создание окна
root = tk.Tk()
root.title("Мухобойка")

# Создание холста
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# Добавление фона (используем формат .gif)
background_photo = tk.PhotoImage(file="Back.png")  # Замените на путь к вашему фону
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Создание мухи (используем формат .gif)
fly_photo = tk.PhotoImage(file="Muha.png")  # Замените на путь к изображению мухи
fly = canvas.create_image(fly_x, fly_y, image=fly_photo)

# Счетчик и таймер
score_label = tk.Label(root, text=f"Счет: {score}", font=("Arial", 16))
score_label.pack(side=tk.LEFT, padx=20)

timer_label = tk.Label(root, text=f"Время: {remaining_time}", font=("Arial", 16))
timer_label.pack(side=tk.RIGHT, padx=20)

# Запуск игры
move_duration = MOVE_TIME  # Время, которое муха двигается в одном направлении
current_direction = random.choice(DIRECTIONS)  # Случайное начальное направление
move_fly()
update_timer()
root.mainloop()
