from feed import Feed
import random

class Breed:
    counter = 0
    breeds = []
    def __init__(self, name, feed):
        type(self).counter += 1
        self.breeds.append(self)
        self.feed = feed
        self.name = name