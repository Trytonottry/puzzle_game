import random
import time
import pygame

# --- Графический интерфейс (Pygame) ---
def init_pygame(size=(300, 300)):
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Пятнашки")
    return screen

def draw_board(screen, board, cell_size=100):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            color = (255, 255, 255) if cell == '0' else (200, 200, 200)
            rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, color, rect)
            if cell != '0':
                font = pygame.font.Font(None, 50)
                text = font.render(cell, True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.flip()

# --- Остальной код игры ---
def display_board_text(board):
    for row in board:
        print(" ".join(row))

def find_empty(board):
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == '0':
                return i, j

def move(board, row, col, new_row, new_col):
    if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
        board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
        return True
    return False

def shuffle_board(board, steps=100):
    empty_row, empty_col = find_empty(board)
    for _ in range(steps):
        possible_moves = [(empty_row - 1, empty_col), (empty_row + 1, empty_col),
                          (empty_row, empty_col - 1), (empty_row, empty_col + 1)]
        random.shuffle(possible_moves)
        for new_row, new_col in possible_moves:
            if move(board, empty_row, empty_col, new_row, new_col):
                empty_row, empty_col = new_row, new_col
                break

def is_solved(board):
    flat_board = [item for sublist in board for item in sublist]
    return flat_board == ['1', '2', '3', '4', '5', '6', '7', '8', '0']

def play_game_text():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    shuffle_board(board)
    display_board_text(board)
    moves = 0
    start_time = time.time()

    while True:
        empty_row, empty_col = find_empty(board)
        move_str = input("Введите направление (w-верх, s-низ, a-лево, d-право, q-выйти): ").lower()

        # ... (остаток функции play_game_text аналогичен предыдущей версии) ...

def play_game_gui():
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']]
    shuffle_board(board)
    screen = init_pygame()
    moves = 0
    start_time = time.time()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                empty_row, empty_col = find_empty(board)
                new_row, new_col = empty_row, empty_col
                if event.key == pygame.K_w:
                    new_row -= 1
                elif event.key == pygame.K_s:
                    new_row += 1
                elif event.key == pygame.K_a:
                    new_col -= 1
                elif event.key == pygame.K_d:
                    new_col += 1
                else:
                    continue
                if move(board, empty_row, empty_col, new_row, new_col):
                    moves += 1
                    draw_board(screen, board)
                    if is_solved(board):
                        print(f"Поздравляю! Вы выиграли! Ходы: {moves}, Время: {time.time() - start_time:.2f} сек.")
                        running = False


if __name__ == "__main__":
    # Выберите режим игры:
    # play_game_text()  # Текстовый режим
    play_game_gui()  # Графический режим (требуется Pygame)

pygame.quit()
