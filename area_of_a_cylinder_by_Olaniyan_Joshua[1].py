"""
This program calculates the area of a cylinder
r is the radius of the cylinder
h is the height of the cylinder
"""
r=float(input("Enter the value of r:"))
h=float(input("Enter the value of h:"))
π=22/7
area=2*π*(r**2)+2*π*r*h
print("The area of the cylinder is",area)
