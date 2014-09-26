#Calculate the area and circumference of a circle

#Importing a library
import math

#Receive user input and store that input in a variable
radius_str = input("Enter the radius of your circle: ")
radius_int = int(radius_str)

#Process that information
#math.pi is Pi in case you forget
circumference = 2*math.pi*radius_int
area = math.pi*(radius_int**2)


print ("The circumference is:",circumference, \
       ", and the area is:",area)
