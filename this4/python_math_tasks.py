import math

# Write a Python program to convert degree to radian.
def degToRad(deg):
    return deg / 180 * math.pi

# deg = float(input("Input Degree: "))
# print(f"Output radian: {degToRad(deg)}")

# Write a Python program to calculate the area of a trapezoid.
def trapezoidArea(height, baseA, baseB):
    return (baseA + baseB) / 2 * height


#h = float(input("Height: "))
#a = float(input("Base, first value: "))
#b = float(input("Base, second value: "))

#print(trapezoidArea(h, a, b))

# Write a Python program to calculate the area of regular polygon.

def polygonArea(num_sides, side_length):
    angle_deg = 360 / (2 * num_sides)
    angle_rad = angle_deg/180 * math.pi
    apoth = side_length / 2 * (1 / math.tan(angle_rad))
    perim = num_sides * side_length
    print(apoth)
    return apoth * perim / 2

# num = int(input("Input number of sides: "))
# length = float(input("Input the length of a side: "))
# print(f"The area of the polygon is: {polygonArea(num, length)}")

# Write a Python program to calculate the area of a parallelogram.

def areaParallelogram(base, height):
    return base * height

# b = float(input("Length of base: "))
# h = float(input("Height of parallelogram: "))
# print(f"Expected Output: {areaParallelogram(b, h)}")