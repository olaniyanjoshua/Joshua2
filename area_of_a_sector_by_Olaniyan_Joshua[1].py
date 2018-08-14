"""
This program calculates the area of a sector
"""
r=float(input("Enter the value of r:"))
θ=float(input("Enter the value of θ:"))
π=22/7
area=π*(r**2)*θ/360
print("The area of the sector is:", area)