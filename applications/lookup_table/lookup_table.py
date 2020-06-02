# Your code here
import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y,cache = {}):
    v = math.pow(x,y)
    # if we havent already done so
    if v not in cache:
    
        # save factorial in cache
        cache[v] = math.factorial(v)
        cache[v] //= (x + y)
        cache[v] %= 982451653
        v = cache[v]
    else: # we have factorial in cache
        v = cache[v]
    return v




# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
