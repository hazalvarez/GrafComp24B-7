import random as rand
import numpy as np
import matplotlib.pyplot as plt

def turn_right():
    array =[coord_points[0], coord_points[1]]
    for i in range(2, len(coord_points)):
        array.append(coord_points[i])
        while len(array) > 2 and np.linalg.det([array[-3], array[-2], array[-1]])>0:
            array.pop(-2)
    return array

def convex_hull():
    coord_points.sort()
    l_upper = turn_right()
    coord_points.reverse()
    l_lower = turn_right()
    l = l_upper + l_lower
    return l

def graph(convex_pol, coord_points):
    x_points = [i[0] for i in coord_points]
    y_points = [i[1] for i in coord_points]

    x_polygon = [i[0] for i in convex_pol]
    y_polygon = [i[1] for i in convex_pol]

    xlim_der = max(x_points) + 5
    ylim_sup = max(y_points) + 5
    xlim_izq = min(x_points) - 5
    ylim_inf = min(y_points) - 5

    plt.xlim(xlim_izq, xlim_der)
    plt.ylim(ylim_inf, ylim_sup)

    plt.title("Problema: Convex Hull")
    
    plt.xlabel("Eje de las abscisas")
    plt.ylabel("Eje de las ordenadas")
    plt.plot(x_points, y_points, "ko")
    plt.plot(x_polygon, y_polygon, "g-", linewidth = 3.0)
    plt.show()

num_points = 8
coord_points = []
for i in range(num_points): coord_points.append([rand.uniform(0,50),rand.uniform(0,100),1.0])
convex_pol = convex_hull()
graph(convex_pol, coord_points)

num_points = 30
coord_points = []
for i in range(num_points): coord_points.append([rand.uniform(0,50),rand.uniform(0,100),1.0])
convex_pol = convex_hull()
graph(convex_pol, coord_points)