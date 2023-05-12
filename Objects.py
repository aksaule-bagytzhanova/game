import pygame
import pathlib
import random
img_path = pathlib.Path(__file__).parent / 'img'


class Locators(object):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    screen_width = 800
    screen_height = 600

    random_speed = [1, -1]

    rect_width = 40
    rect_height = 40

    img_path = pathlib.Path(__file__).parent / 'source' / 'img'
    music_path = pathlib.Path(__file__).parent / 'source' / 'music'

    all_coordinates = []
    all_objects = pygame.sprite.Group()

    all_data_dict = {}



class Object(pygame.sprite.Sprite):
    def __init__(self, img, id, type_obj):
        """ Constructor, create the image of the block. """
        super().__init__()
        image = pygame.image.load(img)
        self.id = id
        self.type = type_obj
        self.image = pygame.transform.scale(image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.get_initial_points()
        self.add_object_to_map(self.rect.x, self.rect.y)

        self.speed_x = random.choice(Locators.random_speed)
        self.speed_y = random.choice(Locators.random_speed)

    def get_initial_points(self):
        rect_x = 0
        rect_y = 0
        is_correct = False
        while not is_correct:
            rect_x = random.randint(20, Locators.screen_width - 20)
            rect_y = random.randint(20, Locators.screen_height - 20)
            is_correct = self.check_valid_point(rect_x, rect_y)

        return rect_x, rect_y

    def check_valid_point(self, x, y):
        for i in range(y-20, y+20):
            for j in range(x-20, x+20):
                if Locators.all_coordinates[i][j] != 0:
                    return False
        return True

    def add_object_to_map(self, x, y):
        for i in range(y-20, y+20):
            for j in range(x-20, x+20):
                Locators.all_coordinates[i][j] = self.id

    def update(self):
        print(f"{self.id} {self.type} {self.image}")

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0:
            self.speed_x = abs(self.speed_x)
            return
        if self.rect.right > Locators.screen_width:
            self.speed_x = abs(self.speed_x)*(-1)
            return
        if self.rect.top < 0:
            self.speed_y = abs(self.speed_y)
            return
        if self.rect.bottom > Locators.screen_height:
            self.speed_y = abs(self.speed_y)*(-1)
            return



