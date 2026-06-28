"""Level 1: Modules, packages, and virtual environments."""

import math
import random
from helpers.calculator import add, multiply

print("Pi:", math.pi)
print("Random number:", random.randint(1, 10))
print("Addition:", add(5, 3))
print("Multiplication:", multiply(4, 6))

print("Tip: create a venv with 'python -m venv .venv' and activate it before installing packages.")
