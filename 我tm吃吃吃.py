import tkinter as tk
import random
maze_layout = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', '#', '#', ' ', ' ', ' ', ' ', '#', '#' ,'#']]

class SnakeGameGUI:
    def __init__(self, maze):
        self.maze = maze
        self.width = len(maze[0])
        self.height = len(maze)

        self.snake = [(self.width // 2, self.height // 2)]
        self.direction = "Right"
        self.generate_food()

    def start_game(self):
        self.root = tk.Tk()
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(self.root, width=self.width * 20, height=self.height * 20)
        self.canvas.pack()

        self.root.bind("<Up>", self.set_direction_up)
        self.root.bind("<Down>", self.set_direction_down)
        self.root.bind("<Left>", self.set_direction_left)
        self.root.bind("<Right>", self.set_direction_right)

        self.update_snake()

        self.root.mainloop()

    def generate_food(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.maze[y][x] == ' ' and (x, y) not in self.snake:
                self.food = (x, y)
                break

    def is_valid_move(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and self.maze[y][x] != '#'

    def set_direction_up(self, event):
        if self.direction != "Down":
            self.direction = "Up"

    def set_direction_down(self, event):
        if self.direction != "Up":
            self.direction = "Down"

    def set_direction_left(self, event):
        if self.direction != "Right":
            self.direction = "Left"

    def set_direction_right(self, event):
        if self.direction != "Left":
            self.direction = "Right"

    def update_snake(self):
        x, y = self.snake[0]

        if self.direction == "Up":
            y -= 1
        elif self.direction == "Down":
            y += 1
        elif self.direction == "Left":
            x -= 1
        elif self.direction == "Right":
            x += 1

        if self.is_valid_move(x, y) and (x, y) not in self.snake[1:]:
            self.snake.insert(0, (x, y))

            if (x, y) == self.food:
                self.generate_food()
            else:
                self.snake.pop()

        self.draw_game()

        if not self.is_game_over():
            self.root.after(200, self.update_snake)

    def draw_game(self):
        self.canvas.delete("all")

        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == '#':
                    self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="black")
                elif self.maze[y][x] == ' ' and (x, y) != self.food:
                    self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="white")

        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green")

        x, y = self.food
        self.canvas.create_oval(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="red")

    def is_game_over(self):
        x, y = self.snake[0]
        return not self.is_valid_move(x, y) or (x, y) in self.snake[1:]


game = SnakeGameGUI(maze_layout)
game.start_game()