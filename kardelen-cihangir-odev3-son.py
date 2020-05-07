import numpy as np
import math, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



#calistirirken oncelikle seceneklerden islemi secip ardindan 4'u secerek deger girmek gerekiyor.


first_values = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

def plott(values):
    
    A = values
   
    figure = plt.figure()
    ax = figure.add_subplot(111, projection='3d')
    ax.scatter3D(A[:, 0], A[:, 1], A[:, 2])

    vertices = [[A[0],A[1],A[2],A[3]], [A[4],A[5],A[6],A[7]], [A[0],A[1],A[5],A[4]], [A[2],A[3],A[7],A[6]], [A[1],A[2],A[6],A[5]],[A[4],A[7],A[3],A[0]]]


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.add_collection3d(Poly3DCollection(vertices,facecolors='blue', linewidths=2, edgecolors='r', alpha=.50))


    plt.show()
    
    
    
    
def translation(values):
    count = int(values.size/3)
    result = np.zeros((count,3))
    x_val = float( input("Translation for X: "))
    y_val = float( input("Translation for Y: "))
    z_val = float( input("Translation for Z: "))

    for i in range (count):
        result[i][0] = values[i][0] + x_val
        result[i][1] = values[i][1] + y_val
        result[i][2] = values[i][2] + z_val
    return result




def rotation(values):
    count = int(values.size/3)
    result = np.zeros((count,3))
    u = float(input("Rotation value: "))
    which_axis = str(input("Which axis? Only x,y,z allowed: "))
    if which_axis.lower() == "x":
        for i in range(count):
            result[i][0] = values[i][0]
            result[i][1] = (values[i][1]*math.cos(u)) - (values[i][2]*math.sin(u))
            result[i][2] = (values[i][1]*math.sin(u)) + (values[i][2]*math.cos(u))
        return result

    elif which_axis.lower() == "y":
        for i in range(count):
            result[i][0] = (values[i][2]*math.sin(u)) + (values[i][0]*math.cos(u))
            result[i][1] = values[i][1]
            result[i][2] = (values[i][2]*math.cos(u)) - (values[i][0]*math.sin(u))
        return result

    elif which_axis.lower() == "z":
        for i in range(count):
            result[i][0] = (values[i][0]*math.cos(u)) - (values[i][1]*math.sin(u))
            result[i][1] = (values[i][0]*math.sin(u)) + (values[i][1]*math.cos(u))
            result[i][2] = values[i][2]
        return result

    else:
        print("Wrong axis!")

    return values
    

def scaling(values):
    count = int(values.size/3)
    result = np.zeros((count,3))
    x_val = float( input("Scaling value for x-axis: "))
    y_val = float( input("Scaling value for y-axis: "))
    z_val = float( input("Scaling value for z-axis: "))

    for i in range (count):
        result[i][0] = values[i][0] * x_val
        result[i][1] = values[i][1] * y_val
        result[i][2] = values[i][2] * z_val
    return result
    
    
if __name__ == "__main__":
    command_list = []
    
    selection = 1

    while selection == 1:
        print("*********************************************************")
        print("0 to Exit")
        print("1 for Main Figure.")
        print("2 to Apply Some Transformations.")
        print("*********************************************************")
        selection = int( input("Selection : "))
        if selection == 1:
            plott(first_values)
        elif selection == 0:
            print("Exiting program...")
            exit()

    
    if selection == 2:
        while 1:
            print("*********************************************************")
            print("0 to Exit.")
            print("1 for Translation.")
            print("2 for Rotation.")
            print("3 for Scaling.")
            print("4 to Apply Transformations.")
            print("*********************************************************")
            if len(command_list):
                print("Enter 4 if you don't want any other tranformation.")
            selection = int( input("Selection : "))
            if selection == 0:
                print("Exiting program...")
                exit()
            elif selection == 4:
                break
            elif (0 < selection < 4) == 0:
                print("Wrong input! Exiting program...")
                exit()
            command_list.append(selection)
        
        temp_values = first_values
        for i in command_list:
            if i == 1:
                temp_values = translation(temp_values)
            elif i == 2:
                temp_values = rotation(temp_values)
            elif i == 3:
                temp_values = scaling(temp_values)

        plott(temp_values)

        


    













