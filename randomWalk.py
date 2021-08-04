import matplotlib.pyplot as plt
import random as ra

def axes(num):
    import matplotlib.pyplot as plt

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
    plt.plot(xorig, null_list_1, color='#c41818', linewidth=1, marker=',', markerfacecolor='blue', markersize=0, label='X-Axis')
    ##Drawing Y-Axis:
    plt.plot(null_list_1, yorig, color='#18c431', linewidth=1, marker=',', markerfacecolor='blue', markersize=0, label='Y-Axis')

def abs1(num):
    if num >= 0:
        return num
    elif num < 0:
        return num*(0-1)

def maxmin(ls):
    high = -35000000
    low = 35000000
    for i in range(len(ls)):
        if ls[i] > high:
            high = ls[i]
        if ls[i] < low:
            low = ls[i]
    res = [high, low]
    return res



def rand():
    ra.seed()
    dire = ra.randrange(1, 5)
    if dire == 1:
        dire = 'e'
    elif dire == 2:
        dire = 'n'
    elif dire == 3:
        dire = 'w'
    elif dire == 4:
        dire = 's'
    else:
        dire = None
        return 0
    return dire

sd = 'N'
while 1:
    sd = str(input("Generate Random Walk? [Y/N]: "))
    if sd == 'Y' or sd == 'y':
        ls1 = []
        xcoor = []
        ycoor = []
        xcoor.append(0)
        ycoor.append(0)
        ra.seed()

        n = int(input("Enter the number of steps: "))

        while n > 0:
            direction = rand()
            ls1.append(direction)
            n = n-1
        print(ls1)
        i = 0
        while i < len(ls1):
            ra.seed()
            if ls1[i] == 'e':
                xcoor.append(xcoor[i] + 1)
                ycoor.append(ycoor[i] + 0)
            elif ls1[i] == 'n':
                xcoor.append(xcoor[i] + 0)
                ycoor.append(ycoor[i] + 1)
            elif ls1[i] == 'w':
                xcoor.append(xcoor[i] - 1)
                ycoor.append(ycoor[i] + 0)
            elif ls1[i] == 's':
                xcoor.append(xcoor[i] + 0)
                ycoor.append(ycoor[i] - 1)
            i = i+1

        max_x = maxmin(xcoor)
        max_y = maxmin(ycoor)
        max_2ax = maxmin([abs1(max_x[0]), abs1(max_x[1]), abs1(max_y[0]), abs1(max_y[1])])
        axes(max_2ax[0])

    else:
        exit()

    print(f'X-Axis: {xcoor}')
    print(f'Y-Axis: {ycoor}')
    plt.plot(xcoor, ycoor, color = 'black', linewidth = 1, marker = 'o', markerfacecolor = 'red', markersize = 3)
    plt.title('Random 4-Directional Unary Walk')
    plt.show()
    displacement = ((xcoor[len(xcoor)-1]**2) + (ycoor[len(ycoor)-1]**2))**0.5
    print(f'Net Displacement: {format(displacement, "0.2f")} units.')





