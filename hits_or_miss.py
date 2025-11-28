def hit_miss(x, y):
    distance_squared = x**2 + y**2
    hittinG_count = 0
    missing_count = 0
    if distance_squared <= 1:
        hittinG_count += 1
        
    else:
        missing_count += 1
       
    
    return hittinG_count, missing_count
    
    