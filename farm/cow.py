from store import store
from pen import Pen
import random

class Cow:  
    cows = []
    def __init__(self, name, pen, breed):
        self.cows.append(self)
        self.id = len(self.cows)
        self.name = name
        self.pen = pen
        self.breed = breed
        self.milk_units = random.randrange(10, 20)
        self.feed_units = random.randrange(5, 10)
        self.gas_units = random.randrange(2, 7)
        self.gas = random.randrange(2, 5)
        store['cows'].append(self)
        self.cows.append(self)
