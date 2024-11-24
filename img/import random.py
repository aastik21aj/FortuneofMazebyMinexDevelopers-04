import random
import time
import pygame

# Initialize Pygame
pygame.init()

# Game settings
maze_size = 8
cell_size = 100  # Each cell in the maze will be 100x100 pixels
screen_width = maze_size * cell_size
screen_height = maze_size * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze of Fortune")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (169, 169, 169)


# Load the player image (replace 'runner.png' with your image file)
player_image = pygame.image.load('runner.png')  # Replace with the path to your player image
player_image = pygame.transform.scale(player_image, (cell_size // 2, cell_size // 2))  # Resize to fit within the cell

# Maze setup
maze = [['.' for _ in range(maze_size)] for _ in range(maze_size)]
lasers = []
start_pos = (0, 0)
end_pos = (maze_size - 1, maze_size - 1)
reward = 20000
time_limit = 3600  # 1 hour in seconds

# Player setup
player_pos = start_pos

# Place lasers randomly
while len(lasers) < 5:
    x, y = random.randint(0, maze_size - 1), random.randint(0, maze_size - 1)
    if (x, y) != start_pos and (x, y) != end_pos and (x, y) not in lasers:
        lasers.append((x, y))

# Game timer setup
start_time = time.time()

# Font setup
font = pygame.font.Font(None, 36)

# Function to draw the maze and player
def draw_maze():
    for i in range(maze_size):
        for j in range(maze_size):
            # Draw grid cells
            rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            if (i, j) in lasers:
                pygame.draw.rect(screen, RED, rect)  # Draw laser as red square
            else:
                pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 3)  # Draw the grid lines
           
            # Draw the player image at the player's position
            if (i, j) == player_pos:
                # Center the image inside the cell
                player_rect = player_image.get_rect(center=rect.center)
                screen.blit(player_image, player_rect)  # Draw the player image
            # Draw the goal
            elif (i, j) == end_pos:
                pygame.draw.circle(screen, (0, 0, 255), rect.center, cell_size // 3)

# Function to handle time and display remaining time
def draw_time_left(time_left):
    time_text = font.render(f"Time Left: {time_left} seconds", True, BLACK)
    screen.blit(time_text, (10, 10))

# Function to check for laser collision
def check_collision():
    if player_pos in lasers:
        return Tru
