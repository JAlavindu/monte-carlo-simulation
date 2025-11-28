from hits_or_miss import hit_miss
from hitting_probability import hitting_prob
import random

def main():
    while True:
        # Number of dart throws
        try:
            N = int(input("Enter the number of dart throws: "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer for the number of throws.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    
    total_hitting_count = 0
    total_missing_count = 0
    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        hittinG_count , missing_count= hit_miss(x, y)
        total_hitting_count += hittinG_count
        total_missing_count += missing_count
        
    print(f"total hitting count: {total_hitting_count}")
    print(f"total missing count: {total_missing_count}")

    hitting_probability = hitting_prob(total_hitting_count, N)
    print(f"Hitting Probability after {N} throws: {round(hitting_probability, 2)} %")
        

if __name__ == "__main__":
    main() 