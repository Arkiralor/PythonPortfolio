import matplotlib.pyplot as plt
import math as m
import random as ra
import gc
import numpy as np

def axes(num):
    #import matplotlib.pyplot as plt
    import math as ma

    num = ma.floor(num)
    xorig = []
    yorig = []
    null_list_1 = []

    for j in range((0 - num), (0 + num + 1), 1):
        xorig.append(j)
        yorig.append(j)
        null_list_1.append(0)

    ##Drawing X-Axis:
    plt.plot(xorig, null_list_1, color='#c41818', linewidth=1, marker=',', markerfacecolor='#c41818',markersize=0, label='X-Axis')
    ##Drawing Y-Axis:
    plt.plot(null_list_1, yorig, color='#18c431', linewidth=1, marker=',', markerfacecolor='#18c431',markersize=0, label='Y-Axis')


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

def projectile():
    x_cor = []
    y_cor = []

    height = ra.randrange(0, 200)
    ra.seed()
    g = 9.81
    phi = ra.randrange(10, 91)
    # phi = 45
    ang = m.radians(phi)
    int_v = ra.randrange(1, 30)

    x_u = int_v * m.cos(ang)
    y_u = int_v * m.sin(ang)
    time_of_flight = (2 * int_v * m.sin(ang)) / g

    x_range = ((int_v ** 2) * m.sin(2 * ang)) / g
    t = 0
    x = 0
    y = 0


    while y + height >= 0 or t <= time_of_flight:
        x = x_u * t
        y = (y_u * t) - (g * (t ** 2)) * 0.5
        x_cor.append(x)
        y_cor.append(height + y)
        t = t + 0.01

    max_x = maxmin(x_cor)
    max_y = maxmin(y_cor)
    max_of_all = maxmin([abs(max_x[0]), abs(max_x[1]), abs(max_y[0]), abs(max_y[1])])
    min_of_all = maxmin([max_x[0], max_x[1], max_y[0], max_y[1]])

    plt.plot(x_cor, y_cor, linewidth=1, label=f'θ = {phi}deg; U = {int_v}m/s; h = {height}m.')
    plt.plot(x_cor[0], y_cor[0], color='red', marker='o', markerfacecolor='red', markersize=2)
    plt.plot(x_cor[len(x_cor)-1], y_cor[len(y_cor)-1], color = 'red', marker = 'o', markerfacecolor = 'red', markersize = 2)
    return max_of_all[0]

try:
    num = int(input("Enter the number of simulations: "))

except Exception as e:
    print(f'Error code: {e}; Aborting execution.')
    exit()

max_of_all = []
for i in range(num):
    max_of_all.append(projectile())
absolute = maxmin(max_of_all)
axes(absolute[0])




interval = (absolute[0]-0)/10
plt.xticks(np.arange(0, absolute[0], interval))
plt.yticks(np.arange(0, absolute[0], interval))

plt.xlabel("Horizontal Range -->")
plt.ylabel("Altitude -->")
plt.legend()
plt.grid(True)
#plt.tight_layout()

plt.show()
gc.collect()
