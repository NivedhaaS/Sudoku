import pygame
import sudoku_generator
from sudoku_generator import SudokuGenerator

width = 1028
height = 960
FPS = 30
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")
font = pygame.font.Font(None, 30)


def create_button_surface(text, width, height, row, col, color):
    button_surface = pygame.Surface((width, height))
    button_surface.fill((255, 255, 255))
    border_rect = pygame.Rect((0, 0, width, height))
    pygame.draw.rect(button_surface, color, border_rect, 1)
    if row % 3 == 0 and row > 0:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, width, 1 * 3), 0)
    if col % 3 == 0 and col > 0:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 1 * 3, height), 0)

    text_render = font.render(str(text), True, (200, 200, 100))
    text_rect = text_render.get_rect(center=(button_surface.get_width() / 2, button_surface.get_height() / 2))
    button_surface.blit(text_render, text_rect.topleft)
    return button_surface, button_surface.get_rect()


def win_menu():
    win_text = font.render("You Win!", True, (255, 255, 255))
    win_rect = win_text.get_rect(center=(width / 2, height / 2 - 100))
    button_surface_exit, button_rect_exit = create_button_surface("Exit", 100, 50, 0, 0, (200, 200, 200))
    button_rect_exit.topleft = (width / 2 - 50, height / 2)
    running = True
    while running:
        screen.fill((125, 125, 125))
        screen.blit(win_text, win_rect)
        screen.blit(button_surface_exit, button_rect_exit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect_exit.collidepoint(event.pos):
                    exit()
        clock.tick(FPS)
        pygame.display.update()

def lose_menu():
    win_text = font.render("You Lose", True, (255, 255, 255))
    win_rect = win_text.get_rect(center=(width / 2, height / 2 - 100))
    button_surface_restart, button_rect_restart = create_button_surface("Restart", 100, 50, 0, 0, (200, 200, 200))
    button_rect_restart.topleft = (width / 2 - 50, height / 2)
    running = True
    while running:
        screen.fill((125, 125, 125))
        screen.blit(win_text, win_rect)
        screen.blit(button_surface_restart, button_rect_restart)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect_restart.collidepoint(event.pos):
                    running = False
                    main()
        clock.tick(FPS)
        pygame.display.update()

def main():
    start = True

    button_surface_easy, button_rect_easy = create_button_surface("Easy", 100, 50, 0, 0, (200, 200, 200))
    button_rect_easy.topleft = (width / 2 - 150, height / 2)

    button_surface_medium, button_rect_medium = create_button_surface("Medium", 100, 50, 0, 0, (200, 200, 200))
    button_rect_medium.topleft = (width / 2 - 50, height / 2)

    button_surface_hard, button_rect_hard = create_button_surface("Hard", 100, 50, 0, 0, (200, 200, 200))
    button_rect_hard.topleft = (width / 2 + 50, height / 2)

    difficulty_text = font.render("Choose a Difficulty", True, (255, 255, 255))
    difficulty_rect = difficulty_text.get_rect(center=(width / 2, height / 2 - 100))

    text = font.render("Welcome to Sudoku", True, (255, 255, 255))
    text_rect = text.get_rect(center=(width / 2, height / 2 - 200))

    while start:
        clock.tick(FPS)
        screen.fill((125, 125, 125))
        screen.blit(text, text_rect)
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(button_surface_easy, button_rect_easy)
        screen.blit(button_surface_medium, button_rect_medium)
        screen.blit(button_surface_hard, button_rect_hard)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect_easy.collidepoint(event.pos):
                    print("Easy selected")
                    start = False
                    removed = 30
                    sudoku = SudokuGenerator(9, removed)
                    sudoku.fill_values()
                    solved = sudoku.get_board()
                    solved_board = [row[:] for row in solved]
                    sudoku.remove_cells()
                    board = sudoku.get_board()
                    initial_board = [row[:] for row in board]
                    sudoku_screen('Easy', sudoku, board, solved_board, initial_board)
                elif button_rect_medium.collidepoint(event.pos):
                    print("Medium selected")
                    start = False
                    removed = 40
                    sudoku = SudokuGenerator(9, removed)
                    sudoku.fill_values()
                    solved = sudoku.get_board()
                    solved_board = [row[:] for row in solved]
                    sudoku.remove_cells()
                    board = sudoku.get_board()
                    initial_board = [row[:] for row in board]
                    sudoku_screen('Medium', sudoku, board, solved_board, initial_board)
                elif button_rect_hard.collidepoint(event.pos):
                    print("Hard Selected")
                    start = False
                    removed = 50
                    sudoku = SudokuGenerator(9, removed)
                    sudoku.fill_values()
                    solved = sudoku.get_board()
                    solved_board = [row[:] for row in solved]
                    sudoku.remove_cells()
                    board = sudoku.get_board()
                    initial_board = [row[:] for row in board]
                    sudoku_screen('Hard', sudoku, board, solved_board, initial_board)


def sudoku_screen(difficulty, sudoku, board_data, solved_board, initial_board):
    running = True
    buttons = [[None] * 9 for _ in range(9)]
    screen.fill((125, 125, 125))
    surfaces = [[None] * 9 for _ in range(9)]
    selected_difficulty_text = font.render('Difficulty: ' + (str(difficulty)), True, (255, 255, 255))
    selected_difficulty_rect = selected_difficulty_text.get_rect(center=(width / 2, height / 2 - 300))
    board_full = False
    selected_row = 0
    selected_col = 0

    button_surface_reset, button_rect_reset = create_button_surface("Reset", 100, 50, 0, 0, (200, 200, 200))
    button_rect_reset.topleft = (width / 2 + 60, height / 1.3)

    button_surface_restart, button_rect_restart = create_button_surface("Restart", 100, 50, 0, 0, (200, 200, 200))
    button_rect_restart.topleft = (width / 2 - 60, height / 1.3)

    button_surface_exit, button_rect_exit = create_button_surface("Exit", 100, 50, 0, 0, (200, 200, 200))
    button_rect_exit.topleft = (width / 2 - 180, height / 1.3)

    def update_display(selected, selected_row, selected_col):
        for row in range(9):
            for col in range(9):
                value = board_data[row][col]
                if value is None:
                    value = ''
                elif value == 0:
                    value = ''
                else:
                    value = int(value)

                button_surface, button_rect = create_button_surface(value, 50, 50, row, col, (200, 200, 200))
                button_rect.topleft = ((width / 4) + col * (50), (height / 3.5) + row * (50))
                screen.blit(button_surface, button_rect)
                buttons[row][col] = button_rect
                surfaces[row][col] = button_surface
                if selected and row == selected_row and col == selected_col:
                    border_rect = pygame.Rect(((width / 4) + col * (50), (height / 3.5) + row * (50), 50, 50))
                    pygame.draw.rect(screen, (255, 0, 0), border_rect, 2)

    update_display(False, None, None)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for row in range(9):
                    for col in range(9):
                        if buttons[row][col].collidepoint(event.pos):
                            selected_row = row
                            selected_col = col
                            update_display(True, selected_row, selected_col)
                if button_rect_exit.collidepoint(event.pos):
                    exit()
                if button_rect_restart.collidepoint(event.pos):
                    running = False
                    main()
                if button_rect_reset.collidepoint(event.pos):
                    board_data = [row[:] for row in initial_board]
                    update_display(False, None, None)
            elif event.type == pygame.KEYDOWN and (selected_row, selected_col) is not None:
                if event.key in range(pygame.K_1, pygame.K_9 + 1):
                    if initial_board[selected_row][selected_col] == 0 and board_data[selected_row][selected_col] == 0:
                        value = event.key - pygame.K_0
                        board_data[selected_row][selected_col] = value
                        update_display(True, selected_row, selected_col)
                    elif initial_board[selected_row][selected_col] != 0:
                        continue
                    elif board_data[selected_row][selected_col] != 0 or board_data[selected_row][selected_col] == 0:
                        value = event.key - pygame.K_0
                        board_data[selected_row][selected_col] = value
                        update_display(True, selected_row, selected_col)
                    print('SOLVED', solved_board)
                    print('BOARD', board_data)
                elif event.key == pygame.K_RETURN:
                    initial_board = [row[:] for row in board_data]
                    if any(0 in row for row in board_data):
                        board_full = False
                    else:
                        board_full = True
                    if board_data == solved_board and board_full:
                        running = False
                        win_menu()
                    if board_data != solved_board and board_full:
                        running = False
                        lose_menu()
                elif event.key == pygame.K_LEFT and selected_col > 0:
                    selected_col -= 1
                    update_display(True, selected_row, selected_col)
                elif event.key == pygame.K_RIGHT and selected_col < 8:
                    selected_col += 1
                    update_display(True, selected_row, selected_col)
                elif event.key == pygame.K_UP and selected_row > 0:
                    selected_row -= 1
                    update_display(True, selected_row, selected_col)
                elif event.key == pygame.K_DOWN and selected_row < 8:
                    selected_row += 1
                    update_display(True, selected_row, selected_col)
        screen.blit(selected_difficulty_text, selected_difficulty_rect)
        screen.blit(button_surface_restart, button_rect_restart)
        screen.blit(button_surface_reset, button_rect_reset)
        screen.blit(button_surface_exit, button_rect_exit)
        clock.tick(FPS)
        pygame.display.update()


main()