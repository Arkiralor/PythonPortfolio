import matplotlib.pyplot as plt
import random as ra

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

    else:
        exit()

    print(f'X-Axis: {xcoor}')
    print(f'Y-Axis: {ycoor}')
    plt.plot(xcoor, ycoor, color = 'black', linewidth = 1, marker = 'o', markerfacecolor = 'red', markersize = 3)
    plt.title('Random 4-Directional Unary Walk')
    plt.show()
    displacement = ((xcoor[len(xcoor)-1]**2) + (ycoor[len(ycoor)-1]**2))**0.5
    print(f'Net Displacement: {format(displacement, "0.2f")} units.')





