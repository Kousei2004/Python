import pygame
import numpy as np
from collections import 
# Khởi tạo Pygame
pygame.init()

# Các hằng số
TILE_SIZE = 40
PLAYER = '@'
BOX = '$'
TARGET = '.'
WALL = '#'
FLOOR = ' '
BOX_ON_TARGET = '*'
PLAYER_ON_TARGET = '+'

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)

class SokobanGame:
    def __init__(self):
        # Mẫu level đơn giản
        self.level = [
            "########",
            "#      #",
            "# $@.  #",
            "#      #",
            "########"
        ]
        self.rows = len(self.level)
        self.cols = len(self.level[0])
        self.screen = pygame.display.set_mode((self.cols * TILE_SIZE, self.rows * TILE_SIZE))
        pygame.display.set_caption('Sokoban with AI Solver')
        
        # Chuyển đổi level từ string sang matrix
        self.state = []
        self.player_pos = None
        self.targets = []
        self.parse_level()

    def parse_level(self):
        self.state = []
        for i, row in enumerate(self.level):
            state_row = []
            for j, cell in enumerate(row):
                if cell == PLAYER or cell == PLAYER_ON_TARGET:
                    self.player_pos = (i, j)
                if cell == TARGET or cell == PLAYER_ON_TARGET or cell == BOX_ON_TARGET:
                    self.targets.append((i, j))
                state_row.append(cell)
            self.state.append(state_row)

    def draw(self):
        self.screen.fill(WHITE)
        for i in range(self.rows):
            for j in range(self.cols):
                rect = pygame.Rect(j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if self.state[i][j] == WALL:
                    pygame.draw.rect(self.screen, BLACK, rect)
                elif self.state[i][j] == TARGET or self.state[i][j] == PLAYER_ON_TARGET:
                    pygame.draw.rect(self.screen, GREEN, rect, 2)
                if self.state[i][j] == PLAYER or self.state[i][j] == PLAYER_ON_TARGET:
                    pygame.draw.circle(self.screen, BLUE, 
                                    (j * TILE_SIZE + TILE_SIZE//2, 
                                     i * TILE_SIZE + TILE_SIZE//2), 
                                    TILE_SIZE//3)
                elif self.state[i][j] == BOX or self.state[i][j] == BOX_ON_TARGET:
                    pygame.draw.rect(self.screen, BROWN,
                                  (j * TILE_SIZE + 5, i * TILE_SIZE + 5,
                                   TILE_SIZE - 10, TILE_SIZE - 10))
        pygame.display.flip()

    def is_valid_move(self, row, col):
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.state[row][col] != WALL)

    def move(self, d_row, d_col):
        row, col = self.player_pos
        new_row, new_col = row + d_row, col + d_col
        
        if not self.is_valid_move(new_row, new_col):
            return False

        # Kiểm tra nếu có hộp
        if self.state[new_row][new_col] in [BOX, BOX_ON_TARGET]:
            box_new_row, box_new_col = new_row + d_row, new_col + d_col
            if not self.is_valid_move(box_new_row, box_new_col):
                return False
            if self.state[box_new_row][box_new_col] in [BOX, BOX_ON_TARGET, WALL]:
                return False
                
            # Di chuyển hộp
            if (box_new_row, box_new_col) in self.targets:
                self.state[box_new_row][box_new_col] = BOX_ON_TARGET
            else:
                self.state[box_new_row][box_new_col] = BOX

        # Di chuyển người chơi
        if (new_row, new_col) in self.targets:
            self.state[new_row][new_col] = PLAYER_ON_TARGET
        else:
            self.state[new_row][new_col] = PLAYER

        # Xóa vị trí cũ của người chơi
        if (row, col) in self.targets:
            self.state[row][col] = TARGET
        else:
            self.state[row][col] = FLOOR

        self.player_pos = (new_row, new_col)
        return True

    def is_solved(self):
        for target in self.targets:
            i, j = target
            if self.state[i][j] not in [BOX_ON_TARGET, PLAYER_ON_TARGET]:
                return False
        return True

class SokobanSolver:
    def __init__(self, game):
        self.game = game
        
    def get_state_string(self, state):
        return ''.join([''.join(row) for row in state])
    
    def solve_bfs(self):
        initial_state = copy.deepcopy(self.game.state)
        initial_pos = self.game.player_pos
        
        queue = deque([(initial_state, initial_pos, [])])
        visited = set()
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        move_names = ['RIGHT', 'LEFT', 'DOWN', 'UP']
        
        while queue:
            current_state, current_pos, path = queue.popleft()
            state_string = self.get_state_string(current_state)
            
            if state_string in visited:
                continue
                
            visited.add(state_string)
            
            # Kiểm tra xem đã giải được chưa
            temp_game = SokobanGame()
            temp_game.state = copy.deepcopy(current_state)
            temp_game.player_pos = current_pos
            if temp_game.is_solved():
                return path
            
            # Thử mọi bước đi có thể
            for (d_row, d_col), move_name in zip(moves, move_names):
                temp_game = SokobanGame()
                temp_game.state = copy.deepcopy(current_state)
                temp_game.player_pos = current_pos
                
                if temp_game.move(d_row, d_col):
                    queue.append((temp_game.state, temp_game.player_pos, path + [move_name]))
        
        return None

def main():
    game = SokobanGame()
    solver = SokobanSolver(game)
    running = True
    solution = None
    solution_index = 0
    
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Tìm giải pháp khi nhấn space
                    print("Finding solution...")
                    solution = solver.solve_bfs()
                    if solution:
                        print("Solution found:", solution)
                        solution_index = 0
                    else:
                        print("No solution found!")
                elif event.key == pygame.K_r:
                    # Reset game
                    game = SokobanGame()
                    solver = SokobanSolver(game)
                    solution = None
                elif event.key == pygame.K_RIGHT:
                    game.move(0, 1)
                elif event.key == pygame.K_LEFT:
                    game.move(0, -1)
                elif event.key == pygame.K_DOWN:
                    game.move(1, 0)
                elif event.key == pygame.K_UP:
                    game.move(-1, 0)
        
        # Thực hiện các bước trong giải pháp
        if solution and solution_index < len(solution):
            move = solution[solution_index]
            if move == 'RIGHT':
                game.move(0, 1)
            elif move == 'LEFT':
                game.move(0, -1)
            elif move == 'DOWN':
                game.move(1, 0)
            elif move == 'UP':
                game.move(-1, 0)
            solution_index += 1
            pygame.time.wait(500)  # Đợi 500ms giữa các bước
        
        game.draw()
        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()