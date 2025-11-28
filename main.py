from hits_or_miss import hit_miss
import random

def main():
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    result  = hit_miss(x, y)
    print(result)


if __name__ == "__main__":
    main() 