import pygame
import random


class GameConf:
    def __init__(self):
        self.solver_name = None  
        self.mode = None         


class GameMode:
    NORMAL = "normal"
    HARD = "hard"
    

# Snake game class
class Game:
    def __init__(self, conf):
        self.conf = conf
        self.running = True
        self.screen = None
        self.clock = pygame.time.Clock()
        self.snake = [(100, 100), (90, 100), (80, 100)]  
        self.snake_direction = (10, 0)  
        self.food_position = None
        self.food_spawn = True

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  
        pygame.display.set_caption("Snake Game")
        self.generate_food()

    def generate_food(self):
        
        self.food_position = (random.randrange(1, (800 // 10)) * 10, random.randrange(1, (600 // 10)) * 10)

    def draw_snake(self):
        for block in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (block[0], block[1], 10, 10))  

    def draw_food(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food_position[0], self.food_position[1], 10, 10))  # Draw food

    def update_snake_position(self):
        head_x, head_y = self.snake[0]
        new_head = (head_x + self.snake_direction[0], head_y + self.snake_direction[1])
        self.snake = [new_head] + self.snake[:-1]

    def check_collision(self):
        head_x, head_y = self.snake[0]
        
        if head_x < 0 or head_x >= 800 or head_y < 0 or head_y >= 600:
            return True
        
        if (head_x, head_y) in self.snake[1:]:
            return True
        return False

    def check_food_collision(self):
        head_x, head_y = self.snake[0]
        if (head_x, head_y) == self.food_position:
            return True
        return False

    def grow_snake(self):
        
        self.snake.append(self.snake[-1])

    def run(self):
        self.initialize()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.snake_direction != (10, 0):
                        self.snake_direction = (-10, 0)
                    elif event.key == pygame.K_RIGHT and self.snake_direction != (-10, 0):
                        self.snake_direction = (10, 0)
                    elif event.key == pygame.K_UP and self.snake_direction != (0, 10):
                        self.snake_direction = (0, -10)
                    elif event.key == pygame.K_DOWN and self.snake_direction != (0, -10):
                        self.snake_direction = (0, 10)

            self.update_snake_position()

            if self.check_collision():
                self.running = False

            if self.check_food_collision():
                self.grow_snake()
                self.food_spawn = False
                self.generate_food()

            
            self.screen.fill((0, 0, 0))  
            self.draw_snake()
            self.draw_food()

            pygame.display.flip()  
            self.clock.tick(15)    #  framerate 15 FPS

        pygame.quit()
        print("Game over!")


class GreedySolver:
    def solve(self):
        print("Greedy solver logic here")

class HamiltonSolver:
    def solve(self):
        print("Hamilton solver logic here")
