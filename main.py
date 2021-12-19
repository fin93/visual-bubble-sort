import pygame, random
pygame.init()

WIDTH, HEIGHT = 610, 600
BG_COLOUR = (217, 217, 217)
line_colour = (100, 100, 100)

sort_list = []
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("sorter")
CLOCK = pygame.time.Clock()
screen.fill(BG_COLOUR)

pygame.display.update()


def reset_write():
    global sort_list
    sort_list.clear()
    for lk in range(100):
        sort_list.append(random.randint(1, 100) / 10)


def print_to_screen(lis):
    for i in range(len(lis)):
        pygame.draw.line(screen, line_colour,
                         (((i + 1) * 6), HEIGHT - 50), (((i + 1) * 6), (550 - lis[i] * 50)), 2)


def bubble_sort(lis):
    n = len(lis)
    for i in range(n - 1):
        for j in range(n - i - 1):
            CLOCK.tick(240)
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
            screen.fill(BG_COLOUR)
            print_to_screen(lis)
            pygame.display.update()


def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_write()
                    bubble_sort(sort_list)
                if event.key == pygame.K_q:
                    quit()

        screen.fill(BG_COLOUR)
        pygame.display.update()


if __name__ == '__main__':
    main()
