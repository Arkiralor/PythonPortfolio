import matplotlib.pyplot as plt
import math as m
import random as ra
import gc
import numpy as np

def axes3d(num):
    #import matplotlib.pyplot as plt
    import math as ma

    num = ma.floor(num)
    xorig = []
    yorig = []
    zorig = []
    null_list_1 = []
    null_list_2 = []


    for j in range((0 - num), (0 + num + 1), 1):
        xorig.append(j)
        yorig.append(j)
        zorig.append(j)
        null_list_1.append(0)
        null_list_2.append(0)

    ##Drawing X-Axis:
    plt.plot(xorig, null_list_1, null_list_2, color='#c41818', linewidth=1, marker=',', markerfacecolor='#c41818',markersize=0, label='X-Axis')
    ##Drawing Y-Axis:
    plt.plot(null_list_1, yorig, null_list_2, color='#18c431', linewidth=1, marker=',', markerfacecolor='#18c431',markersize=0, label='Y-Axis')
    ##Drawing Z-Axis:
    plt.plot(null_list_1, null_list_2, zorig, color ='#185ac4', linewidth=1, marker =',', markerfacecolor = 'blue',markersize=0, label='Z-Axis')


def maxmin(ls):
    high = -35000000000
    low = 35000000000
    for i in range(len(ls)):
        if ls[i] > high:
            high = ls[i]
        if ls[i] < low:
            low = ls[i]
    res = [high, low]
    return res

def projectile3D(height):
    x_cor = []
    y_cor = []
    z_cor = []

    ra.seed()
    g = 9.81
    phi = m.radians(ra.randrange(0,361,1)) #PHI is the angle the path makes on the XY-plane with the x-axis.
    theta = m.radians(ra.randrange(0,91,1)) #Theta is the initial angle of projection.
    int_v = ra.randrange(1,101)

    u_h = int_v*m.cos(theta)
    u_v = int_v*m.sin(theta)
    u_x = u_h*m.cos(phi)
    u_y = u_h*m.sin(phi)
    u_z = u_v

    time_of_flight = (2 * int_v * m.sin(theta)) / g
    ##floor_range = ((int_v ** 2) * m.sin(2 * theta)) / g

    t = 0
    x = 0
    y = 0
    z = 0

    while z+height >= 0 or t <= time_of_flight:
        x = u_x * t
        y = u_y * t
        z = (u_z * t) - (g * (t ** 2)) * 0.5
        x_cor.append(x)
        y_cor.append(y)
        z_cor.append(height+z)
        t = t + 0.01

    max_x = maxmin(x_cor)
    max_y = maxmin(y_cor)
    max_z = maxmin(z_cor)
    max_of_all = maxmin([abs(max_x[0]), abs(max_x[1]), abs(max_y[0]), abs(max_y[1]), abs(max_z[0]), abs(max_z[1])])

    plt.plot(x_cor, y_cor, z_cor, linewidth=1, label=f'θ = {format(m.degrees(theta), "0.1f")}deg; U = {int_v}m/s; h = {height}m.')

    return max_of_all[0]




#num = 0
max_all = []
plt.axes(projection="3d")

try:
    num_of_projections = int(input("Enter the number of projections you require: "))
    height = int(input("Enter the height (along vertical axis) of the projection(s): "))
except Exception as e:
    print(e)
    exit()

for i in range(num_of_projections):
    max_all.append(projectile3D(height))

absolute = max(max_all)
axes3d(absolute)
#plt.legend()
plt.tight_layout()
plt.show()
gc.collect()
