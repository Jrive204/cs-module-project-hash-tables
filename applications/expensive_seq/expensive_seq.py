# Your code here


cache = {}
def expensive_seq(x, y, z):
    # follow example function
     if x <= 0:
         return y + z
     if x >  0: 
        # using method from lookup, check to see if value (tuple this time) has been added to cache
        if (x, y, z) not in cache:
            # if not add it cache with it's math
            cache[(x, y, z)] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
            return cache[(x, y, z)]
        return cache[(x, y, z)]
        # return the value from cache




if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
