import pygame
import random

# Inicializácia Pygame
pygame.init()

# Rozmery obrazovky
screen_width = 900
screen_height = 600

# Vytvorenie okna bez okrajov a pozadia
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
pygame.display.set_caption('DVD Logo')

# Nastavenie transparentnej farby pozadia
transparent_color = (0, 0, 0)
screen.set_colorkey(transparent_color)

# Načítanie obrázku DVD loga s transparentnou farbou
logo = pygame.image.load('dvd_logo.png')
original_logo_rect = logo.get_rect()
logo = pygame.transform.scale(logo, (300, 150))

# Počiatočné pozície a rýchlosť loga
x = random.randint(0, screen_width - logo.get_width())
y = random.randint(0, screen_height - logo.get_height())
dx = 1
dy = 1

# Hlavná slučka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualizácia pozície loga
    x += dx
    y += dy

    # Odbíjanie od stien obrazovky
    if x <= 0 or x >= screen_width - logo.get_width():
        dx = -dx
    if y <= 0 or y >= screen_height - logo.get_height():
        dy = -dy

    # Vymazanie predchádzajúceho snímku
    screen.fill(transparent_color)

    # Zobrazenie loga na aktuálnej pozícii
    screen.blit(logo, (x, y))

    # Aktualizácia obrazovky
    pygame.display.update()

    # Malá prestávka na simuláciu pohybu
    pygame.time.delay(10)

# Ukončenie Pygame
pygame.quit()
