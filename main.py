from hits_or_miss import hit_miss
from hitting_probability import hitting_prob
import random

def main():
    # Number of dart throws
    N = int(input("Enter the number of dart throws: "))
    hittinG_count = 0
    for _ in range(N):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        
        hittinG_count += hit_miss(x, y, N)
        print(f"hittinG_count: {hittinG_count}")

        hitting_probability = hitting_prob(hittinG_count, N)
        print(f"Hitting Probability after {_ + 1} throws: {hitting_probability}")
        

if __name__ == "__main__":
    main() 