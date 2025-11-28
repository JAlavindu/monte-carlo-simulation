from hits_or_miss import hit_miss

def main():
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    result  = hit_miss(x, y)
    print(result)


if __name__ == "__main__":
    main() 