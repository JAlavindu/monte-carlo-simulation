def hit_miss(x, y , N):
    radius = (x**2 + y**2)**0.5
    hittinG_count = 0
    if radius <= 1:
        hittinG_count += 1
        print("Hitting inside the dartboard")
    else:
        print("Missing the dartboard")
    
    return hittinG_count
    
    