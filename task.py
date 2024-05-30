# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_square(points, point):
    fig, Axes = plt.subplots()
    square = patches.Polygon(points, closed=True, facecolor='none')
    Axes.add_patch(square)
    
    x_points, y_points = zip(*points)
    Axes.plot(x_points, y_points, 'ro') 

    zx, zy = point 
    Axes.scatter(zx, zy, color='b')

    Axes.set_xlim(min(x_points) - 5, max(x_points) + 5)
    Axes.set_ylim(min(y_points) - 5, max(y_points) + 5)
    
    plt.show()  

#1
def is_point_inside_square_1(square_points, point):
    x1, y1 = square_points[0]
    x2, y2 = square_points[1]
    x3, y3 = square_points[2]
    x4, y4 = square_points[3]

    zx, zy = point

    def formula(x1, y1, x2, y2, zx, zy):
        return (zx - x2) * (y1 - y2) - (zy - y2) * (x1 - x2)
    
    b1 = formula(x1, y1, x2, y2, zx, zy) < 0.0
    b2 = formula(x2, y2, x3, y3, zx, zy) < 0.0
    b3 = formula(x3, y3, x4, y4, zx, zy) < 0.0
    b4 = formula(x4, y4, x1, y1, zx, zy) < 0.0

    if ((b1 == b2) and (b2 == b3) and (b3 == b4)):
        print(True)
    else:
        print(False)


#2 
def is_point_inside_square_2(square_points, point):
    x1, y1 = square_points[0]
    x2, y2 = square_points[1]
    x3, y3 = square_points[2]
    x4, y4 = square_points[3]

    x, y = point

    if x1 <= x <= x2 and y1 <= y <= y3:
        print(True)
    else:
        print(False)



square_points = [(1, 1), (5, 1), (5, 5), (1, 5)]
point = (7, 6)


draw_square(square_points,point)

is_point_inside_square_1(square_points, point)
is_point_inside_square_2(square_points, point)