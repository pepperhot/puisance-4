import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Puissance 4")

jeton_rouge = pygame.image.load("image/jeton rouge.png").convert_alpha()
jeton_rouge = pygame.transform.scale(jeton_rouge, (200, 200))
jeton_jaune = pygame.image.load("image/jeton_jaune.png").convert_alpha()
jeton_jaune = pygame.transform.scale(jeton_jaune, (200, 200))

clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

jetons = []

target = pygame.Rect(0, 500, 800, 100)

running = True
while running:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (200, 200, 200), target)

    for i, (img, x, y, vy) in enumerate(jetons):
        vy += 500 * (clock.get_time() / 1000) 
        y += vy * (clock.get_time() / 1000)

        if y + img.get_height() >= target.top:
            y = target.top - img.get_height()
            vy = 0 

        jetons[i] = (img, x, y, vy)
        screen.blit(img, (x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            img = jeton_jaune if len(jetons) % 2 == 0 else jeton_rouge
            jetons.append((img, pos[0] - img.get_width() // 2, 0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
