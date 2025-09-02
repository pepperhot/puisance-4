import pygame

pygame.init()

width, height = 675, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Puissance 4")

jeton_rouge = pygame.image.load("image/jeton rouge.png").convert_alpha()
jeton_rouge = pygame.transform.scale(jeton_rouge, (50, 50))
jeton_jaune = pygame.image.load("image/jeton jaune.png").convert_alpha()
jeton_jaune = pygame.transform.scale(jeton_jaune, (50, 50))

clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

jetons = []
target = pygame.Rect(0, 530, 800, 100)

cell_size = 80
cols, rows = 7, 6 
position = [50, 130, 210, 290, 370, 450, 530]
grid = [[pygame.Rect(col * cell_size + 50, row * cell_size + 50, cell_size, cell_size) for row in range(rows)] for col in range(cols)]

running = True
while running:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (200, 200, 200), target)

    for i, (img, x, y, vy) in enumerate(jetons):
        vy += 0.5 * clock.get_time()
        y += vy * (clock.get_time() / 1000)

        if y + img.get_height() >= target.top:
            y = target.top - img.get_height()
            vy = 0 
        if any(jetons[j][1] == x and jetons[j][2] > y for j in range(i)):
            target.top -= img.get_height()

        jetons[i] = (img, x, y, vy)
        screen.blit(img, (x, y))

    for col in range(cols):
        for row in range(rows):
            pygame.draw.rect(screen, (150, 150, 150), grid[col][row], 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pos = [i + 40 for i in position if i < pos[0] < i + 80]
            img = jeton_jaune if len(jetons) % 2 == 0 else jeton_rouge
            jetons.append((img, pos[0] - img.get_width() // 2, 0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()