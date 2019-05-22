import math  

def calculateRadius(x1, y1, x2, y2):
    radius = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
    return radius