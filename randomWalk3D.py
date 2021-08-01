import matplotlib.pyplot as plt
import random as ra

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
    dire = ra.randrange(1, 7)
    if dire == 1:
        dire = 'e'
    elif dire == 2:
        dire = 'n'
    elif dire == 3:
        dire = 'w'
    elif dire == 4:
        dire = 's'
    elif dire == 5:
        dire = 'u'
    elif dire == 6:
        dire = 'd'
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
        zcoor = []



        xcoor.append(0)
        ycoor.append(0)
        zcoor.append(0)
        ra.seed()

        n = int(input("Enter the number of steps: "))

        while n > 0:
            direction = rand()
            ls1.append(direction)
            n = n-1
        print(f'Directions Taken: {ls1}')
        i = 0
        while i < len(ls1):
            if ls1[i] == 'e':
                xcoor.append(xcoor[i] + 1)
                ycoor.append(ycoor[i] + 0)
                zcoor.append(zcoor[i] + 0)
            elif ls1[i] == 'n':
                xcoor.append(xcoor[i] + 0)
                ycoor.append(ycoor[i] + 1)
                zcoor.append(zcoor[i] + 0)
            elif ls1[i] == 'w':
                xcoor.append(xcoor[i] - 1)
                ycoor.append(ycoor[i] + 0)
                zcoor.append(zcoor[i] + 0)
            elif ls1[i] == 's':
                xcoor.append(xcoor[i] + 0)
                ycoor.append(ycoor[i] - 1)
                zcoor.append(zcoor[i] + 0)
            elif ls1[i] == 'u':
                xcoor.append(xcoor[i] + 0)
                ycoor.append(ycoor[i] + 0)
                zcoor.append(zcoor[i] + 1)
            elif ls1[i] == 'd':
                xcoor.append(xcoor[i] + 0)
                ycoor.append(ycoor[i] + 0)
                zcoor.append(zcoor[i] - 1)
            i = i+1

        xorig = []
        yorig = []
        zorig = []
        null_list_1 = []
        null_list_2 = []

        ##Checking max. values of coordinate range.
        resx = maxmin(xcoor)
        resy = maxmin(ycoor)
        resz = maxmin(zcoor)
        res_all = maxmin([abs1(resx[0]), abs1(resx[1]), abs1(resy[0]), abs1(resy[1]), abs1(resz[0]), abs1(resz[1])])
        high = res_all[0]

        ##Constructing coordinate set for origins of all axes.
        for j in range((0-high), (0+high+1), 1):
            xorig.append(j)
            yorig.append(j)
            zorig.append(j)
            null_list_1.append(0)
            null_list_2.append(0)
    elif sd == 'N' or sd == 'n':
        print(f'"{sd}" chosen; exiting application.')
        exit()
    else:
        print(f'Invalid input: "{sd}"; exiting application.')
        exit()

    print(f'Highest coordinate value: {high}')
    print(f'X-Axis Graduation: {xorig}')
    print(f'Y-Axis Graduation: {yorig}')
    print(f'Z-Axis Graduation: {zorig}')
    print(f'X-Axis Coordinates: {xcoor}')
    print(f'Y-Axis Coordinates: {ycoor}')
    print(f'Z-Axis Coordinates: {zcoor}')
    ax = plt.axes(projection="3d")

    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")

    ##Drawing Origin
    plt.plot(0, 0, 0, color = 'blue', linewidth = 0, marker = 'o', markerfacecolor = 'blue', markersize = 3)
    ##Drawing X-Axis:
    plt.plot(xorig, null_list_1, null_list_2, color = 'blue', linewidth = 1, marker = ',', markerfacecolor = 'blue', markersize = 0)

    ##Drawing Y-Axis:
    plt.plot(null_list_1, yorig, null_list_2, color = 'blue', linewidth = 1, marker = ',', markerfacecolor = 'blue', markersize = 0)

    ##Drawing Z-Axis:
    plt.plot(null_list_1, null_list_2, zorig, color = 'blue', linewidth = 1, marker = ',', markerfacecolor = 'blue', markersize = 0)

    ##Drawing random walk in three dimensions:
    plt.plot(xcoor, ycoor, zcoor, color = 'black', linewidth = 1, marker = 'o', markerfacecolor = 'red', markersize = 3)
    plt.title('Random 6-Directional Unary Walk')
    plt.show()

    ##Calculation of net displacement of particle after 'n' steps.
    displacement = ((xcoor[len(xcoor)-1]**2) + (ycoor[len(ycoor)-1]**2) + (zcoor[len(zcoor)-1]**2))**0.5
    print(f'Net Displacement: {format(displacement, "0.2f")} units.')





