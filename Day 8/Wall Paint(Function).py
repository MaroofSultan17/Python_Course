import math

def paint_cal(width, height, coverage):
    result = (width*height)/coverage
    print(f"You'll need {math.ceil(result)} cans of paint")

wall_h = int(input('Please enter the Height of a Wal'))
wall_w = int(input('Please enter the Width of a Wal'))
coverage = 5
paint_cal(wall_w, wall_h, coverage)