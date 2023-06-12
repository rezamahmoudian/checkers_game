import pygame
from checkers.constrant import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')


# گرفتن سطر و ستون مهره با استفاده از نصطه ی کلیک موس
def get_row_col_from_mouse(mouse_pos):
    x, y = mouse_pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    piece = board.get_piece(0, 1)
    # board.move(piece, 4, 3)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # انتخاب مهره با کلیک روی آن
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(mouse_pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)

        board.draw(screen)
        pygame.display.update()

    pygame.quit()

main()
