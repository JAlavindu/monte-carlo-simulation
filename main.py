from hits_or_miss import hit_miss
from hitting_probability import hitting_prob
from write_to_excel import excel_writer
import random

def main():
    while True:
        try:
            # Number of dart throws
            N = int(input("Enter the number of dart throws: "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer for the number of throws.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    
    total_hitting_count = 0
    total_missing_count = 0
    
    milestones = [1000, 10000, 100000, 1000000]
    history_throws = []
    history_hits = []

    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        hitting_count , missing_count= hit_miss(x, y)
        total_hitting_count += hitting_count
        total_missing_count += missing_count

        current_throws = i + 1
        if current_throws in milestones:
            history_throws.append(current_throws)
            history_hits.append(total_hitting_count)
            excel_writer(history_throws, history_hits)
        
    print(f"total hitting count: {total_hitting_count}")
    print(f"total missing count: {total_missing_count}")

    hitting_probability = hitting_prob(total_hitting_count, N)
    print(f"Hitting Probability after {N} throws: {round(hitting_probability, 2)} %")

    pi = (hitting_probability / 100) * 4
    print(f"Estimated value of Pi after {N} throws: {round(pi, 6)}")
        

if __name__ == "__main__":
    main() 