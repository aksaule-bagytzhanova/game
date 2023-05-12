import random
from Objects import Locators
from Objects import Object


def add_objects(img, id, type):
    num_obj = random.randint(1, 10)
    for n in range(num_obj):
        obj = Object(img, int(f"{id}{n}"), type)
        Locators.all_objects.add(obj)
        Locators.all_data_dict[obj.id] = obj
