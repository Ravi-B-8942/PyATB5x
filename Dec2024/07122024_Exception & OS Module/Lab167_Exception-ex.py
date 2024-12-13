import math
from logging import exception

try:
    math.exp(1000)
except Exception as e:
    print(e)
