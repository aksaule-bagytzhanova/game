import time
import pygame
from Objects import Locators
import util

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((Locators.screen_width, Locators.screen_height))
pygame.display.set_caption("Rock Paper Scissors")

pygame.mixer.init()
pygame.mixer.music.load(f"{Locators.music_path}\\back.mp3")
pygame.mixer.music.play(-1,0.0)

Locators.all_coordinates = [[0 for j in range(Locators.screen_width)] for i in
                                              range(Locators.screen_height)]

all_img = [f"{Locators.img_path}\\rock.png",
           f"{Locators.img_path}\\scissors.png",
           f"{Locators.img_path}\\paper.png"]

type_list = ["rock", "scissors", "paper"]

for img_index in range(3):
    util.add_objects(all_img[img_index], img_index+1, type_list[img_index])

print(Locators.all_coordinates)

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(Locators.WHITE)

    # Update and draw rectangles
    Locators.all_objects.update()
    Locators.all_objects.draw(screen)

    # Update the display
    pygame.display.update()
    Locators.all_coordinates_x = []
    Locators.all_coordinates_y = []

    time.sleep(0.005)

# Quit the game
pygame.quit()