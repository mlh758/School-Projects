#CS101
#Program 9 - PPMImage class
#Harris Michael
#mlh758@mail.umkc.edu
#
#Problem: Design a ppm image class that uses the pixel class to manipulate
# a .ppm image. Create various filters that can be applied to the entire image
# and a way to open and save files.
#
#Algorithm:
#1. Constructor: takes a file name for input defaulting to an empty string. 
# Sets self.Name to the value of the file name. If a file name is given, the 
# constructor calls the private Open method providing the file name as input.
#2. Open: Private method to open a PPM image and fill in the object data.  
# Receives the file name from the constructor. Attempt to open the given PPM 
# image. If the file is unable to open, catch the IOError and report that the 
# program was unable to open the file. Read the first line of the file, 
# stripping white space. If that is not equal to the P3 constant, raise a 
#TypeError. In this event, report that the file is not a PPM file. Read the 
# next line, saving the integer values of the rows and columns to variables 
# within the object. Read the next line and save the max color value to a 
# variable within the object.
# Declare an empty list for self.Image. For each row, declare an empty row 
# list. For every column in that row, read a line from the file creating a 
# list of integers out of it. Send that list to the pixel constructor and 
# append it to the row list. When the whole row has been read, append it to 
# the Image list. No matter what happens, close the file and set 
# self.UnsavedChanges to False.
#3. String: Returns a formatted string as per specifications. Representation 
# method does the same.
#4. Save: Takes a file name as input, defaulting to an empty string. If no 
# string is provided, opens the file name stored in the self.Name variable for 
# writing. Write the header information to the file. Iterate through each pixel 
# in every row. Call the writer method of that pixel and write the returned 
# value to the file. Close the file, set UnsavedChanges to False. If a file 
# name is given, open that file for writing and the rest is the same.
#5. SaveAs: Takes a file name as input defaulting to the empty string. If no 
# file name is given, raise an IOError.  Check to make sure the filename ends 
# with .ppm. If it does not, inform the user this is an invalid file name and 
# try again.
#6. Grayscale: Call the SetGray method on each pixel in the image. Set 
# UnsavedChanges to True.
#7. Negative: Call the SetNegative method on each pixel in the image. Set 
# UnsavedChanges to True.
#8. Lighten: Call the Lighten method on each pixel in the image. Set 
# UnsavedChanges to True.
#9. Darken: Call the Darken method on each pixel in the image. Set 
# UnsavedChanges to True.
#10. ReduceColorspace: Call the Reduce method on each pixel in the image. 
# Set UnsavedChanges to True.
#11. CountColors: Create a colors set. Call the Tuple method on each pixel 
# in the image and attempt to add that tuple to the colors set. Return the 
# length of the set.

import pixel

class PPMImage(object):
    def __init__(self, Filename = ''):
        '''Constructs the initial object'''
        self.Name = Filename
        if Filename:
            self.__Open(Filename)
            
    def __Open(self, Name):
        '''Opens a file and builds the PPMImage object'''
        try:
            File = open(Name)
        except IOError:
            print("Unable to open file")
            return None
        #Check the constant
        if File.readline().strip() != 'P3':
            print("This is not a PPM file.")
            File.close()
            return None
        #Store the column and row values
        self.Cols,self.Rows = File.readline().strip().split()
        self.Cols,self.Rows = int(self.Cols), int(self.Rows)
        #Store the max color value
        self.Colors = File.readline().strip()
        self.Image = list()
        for i in range(self.Rows):
            row = list()
            for j in range(self.Cols):
                row.append(pixel.pixel([int(x) for x in\
                                        File.readline().strip().split()]),)
            self.Image.append(row)
        File.close()
        self.UnsavedChanges = False
            
    def __str__(self):
        '''Provides formatting to print the object'''
        return 'PPMImage {}, {}x{}'.format(self.Name, self.Cols,self.Rows)
    
    def __repr__(self):
        '''Formates the object to be represented in the console'''
        return 'PPMImage {}, {}x{}'.format(self.Name, self.Cols,self.Rows)
    
    def Save(self, filename = ''):
        '''Saves changes to the file'''
        if filename:
            try:
                Fout = open(filename, 'w')
            except IOError:
                print("Unable to open",filename,"for saving.")
        else:
            try:
                Fout = open(self.Name, 'w')
            except IOError:
                print("Unable to open",filename,"for saving.")
        Fout.write('P3\n')
        Fout.write('{} {}\n'.format(self.Cols, self.Rows))
        Fout.write(self.Colors+'\n')
        for row in self.Image:
            for pix in row:
                Fout.write(pix.writer()+'\n')
        Fout.close()
        self.UnsavedChanges = False
        
    def SaveAs(self, filename = ''):
        '''Specifies a file to save to'''
        if not filename:
            raise ValueError
        if filename.endswith('.ppm'):
            self.Save(filename)
        else:
            raise ValueError
    
    def Grayscale(self):
        '''Converts an image to grayscale'''
        for row in self.Image:
            for pix in row:
                pix.SetGray()
        self.UnsavedChanges = True
    
    def Negative(self):
        '''Converts an image to photographic negative'''
        for row in self.Image:
            for pix in row:
                pix.SetNegative()
        self.UnsavedChanges = True
    
    def Lighten(self):
        '''Lightens an image'''
        for row in self.Image:
            for pix in row:
                pix.Lighten()
        self.UnsavedChanges = True
    
    def Darken(self):
        '''Darkens an image'''
        for row in self.Image:
            for pix in row:
                pix.Darken()
        self.UnsavedChanges = True
                
    def CountColors(self):
        '''Returns the number of distinct color values in an image'''
        colors = set()
        for row in self.Image:
            for pix in row:
                colors.add(pix.tuple())
        return len(colors)
    
    def ReduceColorspace(self):
        '''Reduces the color space of an image'''
        for row in self.Image:
            for pix in row:
                pix.Reduce()
        self.UnsavedChanges = True
        
    def Scroll(self):
        """Scrolls an image by the given number of pixels"""
        shift = int(input("Enter the number of pixels to shift the image: "))
        new_image = list()
        for row in self.Image:
            new_row = [row[(i+shift)%self.Cols] for i in range(self.Cols)]
            new_image.append(new_row)
        self.Image = new_image
        