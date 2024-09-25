#!/usr/bin/env python3
from task_04_flyingfish import FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()      # Should print: The flying fish is swimming!
flying_fish.fly()       # Should print: The flying fish is soaring!
flying_fish.habitat()   # Should print: The flying fish lives both in water and the sky!

# Print method resolution order (MRO)
print(FlyingFish.mro())
