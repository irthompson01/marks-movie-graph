import pygame
import random
import os

# Configuration
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS_START = 10
SPEED_INCREMENT = 0.5
FOOD_SCORE = 10
HIGH_SCORE_FILE = "highscore.txt"

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
OPPOSITE = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}


class Snake:
    def __init__(self):
        # Start with 3 segments in the middle of the grid
        mid_x = GRID_WIDTH // 2
        mid_y = GRID_HEIGHT // 2
        self.positions = [
            (mid_x, mid_y),
            (mid_x - 1, mid_y),
            (mid_x - 2, mid_y),
        ]
        self.direction = RIGHT  # initial direction
        self.grow_pending = 0

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        # Wall collision
        if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
            return False

        # Self collision
        if new_head in self.positions:
            return False

        self.positions.insert(0, new_head)
        if self.grow_pending:
            self.grow_pending -= 1
        else:
            self.positions.pop()
        return True

    def change_direction(self, new_dir):
        if new_dir != OPPOSITE.get(self.direction):
            self.direction = new_dir

    def grow(self):
        self.grow_pending += 1


class Food:
    def __init__(self, snake_positions):
        self.position = self.random_position(snake_positions)

    def random_position(self, snake_positions):
        empty = [
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            if (x, y) not in snake_positions
        ]
        return random.choice(empty) if empty else None

    def respawn(self, snake_positions):
        self.position = self.random_position(snake_positions)


def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    return 0


def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    snake = Snake()
    food = Food(snake.positions)
    score = 0
    high_score = load_high_score()
    fps = FPS_START

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    snake.change_direction(UP)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    snake.change_direction(DOWN)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    snake.change_direction(LEFT)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    snake.change_direction(RIGHT)

        if not snake.move():
            running = False  # Collision

        head = snake.positions[0]
        if food.position and head == food.position:
            snake.grow()
            score += FOOD_SCORE
            if score > high_score:
                high_score = score
            food.respawn(snake.positions)

        # Drawing
        screen.fill((0, 0, 0))
        if food.position:
            fx, fy = food.position
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                pygame.Rect(fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )
        for pos in snake.positions:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )
        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        high_surf = font.render(f"High: {high_score}", True, (255, 255, 255))
        screen.blit(score_surf, (5, 5))
        screen.blit(high_surf, (5, 25))
        pygame.display.flip()

        # Increase speed over time
        # fps += SPEED_INCREMENT * (score // 50)
        clock.tick(int(fps))

    save_high_score(high_score)
    pygame.quit()


if __name__ == "__main__":
    main()