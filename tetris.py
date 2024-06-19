import pygame
import random
from shapes import SHAPES, COLORS
from settings import WIDTH, HEIGHT, CELL_SIZE, ROWS, COLS, FPS, DROP_TIME

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.next_shape = random.choice(SHAPES)
        self.next_color = random.choice(COLORS)
        self.new_shape()
        self.score = 0
        self.lines = 0
        self.level = 1
        self.drop_speed = DROP_TIME
        self.game_over = False

    def new_shape(self):
        self.current_shape = self.next_shape
        self.current_color = self.next_color
        self.next_shape = random.choice(SHAPES)
        self.next_color = random.choice(COLORS)
        self.shape_pos = [0, COLS // 2 - len(self.current_shape[0]) // 2]

    def draw_grid(self):
        for r in range(ROWS):
            for c in range(COLS):
                color = self.board[r][c]
                pygame.draw.rect(self.screen, color, [c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE], 0 if color else 1)

    def draw_next_shape(self):
        x_offset = WIDTH + 10
        y_offset = 20
        for r, row in enumerate(self.next_shape):
            for c, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.next_color, [x_offset + c * CELL_SIZE, y_offset + r * CELL_SIZE, CELL_SIZE, CELL_SIZE])

    def draw_board(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        self.draw_grid()
        self.draw_next_shape()
        font = pygame.font.SysFont('Arial', 25, True)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        level_text = font.render(f'Level: {self.level}', True, (255, 255, 255))
        lines_text = font.render(f'Lines: {self.lines}', True, (255, 255, 255))
        self.screen.blit(score_text, (WIDTH + 10, 100))
        self.screen.blit(level_text, (WIDTH + 10, 130))
        self.screen.blit(lines_text, (WIDTH + 10, 160))
        pygame.display.flip()

    # Add methods to move, rotate, drop shapes, and check game over

def main():
    pygame.init()
    game = Tetris()
    while not game.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            # Add controls for moving and rotating shapes
        game.draw_board()
        pygame.time.wait(500)  # Delay for dropping shapes

    pygame.quit()

if __name__ == "__main__":
    main()
