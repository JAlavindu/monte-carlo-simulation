def hit_miss(x, y):
    radius = (x**2 + y**2)**0.5
    if radius <= 1:
        return "Hitting inside the dartboard"
    else:
        return "Missing the dartboard"