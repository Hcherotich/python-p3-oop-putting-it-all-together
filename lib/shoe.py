#!/usr/bin/env python3

# In lib/shoe.py

class Shoe:
    '''Shoe class representing a shoe'''

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    
    def set_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
            return
        self.size = size
