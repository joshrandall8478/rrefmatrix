# import sympy 
from sympy import *

print(""" _____         _        _     ______ ______  _____ ______  ___  ___        _          _       
|  _  |       (_)      | |    | ___ \| ___ \|  ___||  ___| |  \/  |       | |        (_)      
| | | | _   _  _   ___ | | __ | |_/ /| |_/ /| |__  | |_    | .  . |  __ _ | |_  _ __  _ __  __
| | | || | | || | / __|| |/ / |    / |    / |  __| |  _|   | |\/| | / _` || __|| '__|| |\ \/ /
\ \/' /| |_| || || (__ |   <  | |\ \ | |\ \ | |___ | |     | |  | || (_| || |_ | |   | | >  < 
 \_/\_\ \__,_||_| \___||_|\_\ \_| \_|\_| \_|\____/ \_|     \_|  |_/ \__,_| \__||_|   |_|/_/\_\
                                                                                              
                                                                                              


""")
print()
print("By: Joshua Randall")

print()
while(True):

    loopMatrix = True
    matrix = []
    rowLength = 0
    data = []
    m = input("Enter numbers for the first row of the matrix: ")
    m = [*m]
    try:
        for item in m:
            data.append(int(item))
            rowLength = rowLength + 1
    except ValueError:
        print("Only input integers.")
        print()

    matrix.append(data)
    print()
    print("Row length: " + str(rowLength))
    print("=====================")
    while(loopMatrix):
        data = []
        print()
        print(matrix)
        m = input("Enter numbers for ")
