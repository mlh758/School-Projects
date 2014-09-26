#CS101
#Program 9 - Pixel class
#Harris Michael
#mlh758@mail.umkc.edu
#Problem: Create a pixel class to help interface with the pixels in a ppm
#  image in a clear and logical way.
#
#Algorithm:
#1. Constructor: Takes a tuple of integers representing Red, Green, and Blue. 
# Iterate through tuple, if an item is not an integer raise a type error and if 
# the item is >255 or <0 raise a value error. Otherwise assign the items in 
# order to self.Red, self.Green, and self.Blue.
#2. String function: Returns a string with the R/G/B values. Representation 
# function does the same.
#3. Writer: Public method returns a string of R/G/B values for use in writing 
# output to a file.
#4. Tuple: Method returns a tuple of the R/G/B values.
#5. SetGray: calls Tuple method, finds the average of the tuple truncating the 
# decimal using integer division and assigns that average value to the self.Red, 
# self.Green, and self.Blue values
#6. SetNegative: Subtracts the RGB values from 255 and saves them back to the 
# self.Red/Green/Blue variables.
#7. Lighten: Adds 50 to the RGB values. If the value exceeds 255, sets the 
# value to 255.
#8. Darken: Subtracts 50 from the RGB values. If the value falls below 0, sets 
# the value to 0.
#9. Reduce: Calls the Tuple method and assigns it to a variable. Create a new 
# list. For each value in the retrieved tuple, if that value is <= 50 
# append  25 to the new list. If the value is between 51 and 100 inclusive 
# append the value 75 to the new list. If the value is between 101 and 150 
# inclusive append the value 125 to the new list. If the value is between 
# 151 and 200 inclusive append the value 175 to the new list. Otherwise 
# append the value 225 to the new list. The self.R/G/B values get assigned the 
# corresponding numbers from the new list.

class pixel(object):
    def __init__(self, vals = (0,0,0)):
        '''Builds the object'''
        for item in vals:
            if type(item) != int:
                raise TypeError
            elif item > 255 or item <0:
                raise ValueError
        self.Red = vals[0]
        self.Green = vals[1]
        self.Blue = vals[2]
        
    def __str__(self):
        '''Formats a string to represent the pixel for printing'''
        return '{} {} {}'.format(self.Red,self.Green,self.Blue)
    
    def __repr__(self):
        '''Represents the object for the console'''
        return '({}, {}, {})'.format(self.Red,self.Green,self.Blue)
    
    def writer(self):
        '''Returns a string of the pixel for use in writing'''
        return '{} {} {}'.format(self.Red,self.Green,self.Blue)
    
    def tuple(self):
        '''Provides a tuple containing the RGB values'''
        return (self.Red,self.Green,self.Blue)
    
    def SetGray(self):
        '''Grays out a pixel'''
        vals = self.tuple()
        gray = sum(vals)//3
        self.Red = self.Green = self.Blue = gray
        
    def SetNegative(self):
        '''Turns a pixel into it's photographic negative'''
        self.Red   = 255 - self.Red
        self.Green = 255 - self.Green
        self.Blue  = 255 - self.Blue
    
    def Lighten(self):
        '''Lightens a pixel'''
        self.Red += 50
        if self.Red > 255:
            self.Red = 255
        self.Green += 50
        if self.Green > 255:
            self.Green = 255
        self.Blue += 50
        if self.Blue > 255:
            self.Blue = 255
    
    def Darken(self):
        '''Darkens a pixel'''
        self.Red -= 50
        if self.Red < 0:
            self.Red = 0
        self.Green -= 50
        if self.Green < 0:
            self.Green = 0
        self.Blue -= 50
        if self.Blue < 0:
            self.Blue = 0
    
    def Reduce(self):
        '''Reduces the color space of a pixel'''
        #Vals is ordered by color
        vals = self.tuple()
        new_vals = list()
        #Loop will assign colors to new list in the same order
        for C in vals:
            if C <= 50:
                new_vals.append(25)
            elif 51 <= C <= 100:
                new_vals.append(75)
            elif 101 <= C <= 150:
                new_vals.append(125)
            elif 151 <= C <= 200:
                new_vals.append(175)
            else:
                new_vals.append(225)
        #Set the colors to their new values
        self.Red   = new_vals[0]
        self.Green = new_vals[1]
        self.Blue  = new_vals[2]
    