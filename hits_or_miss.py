def hit_miss(x, y):
    radius = (x**2 + y**2)**0.5
    hittinG_count = 0
    missing_count = 0
    if radius <= 1:
        hittinG_count += 1
        
    else:
        missing_count += 1
       
    
    return hittinG_count, missing_count
    
    