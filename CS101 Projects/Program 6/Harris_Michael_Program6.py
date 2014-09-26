#CS 101
#Program 6
#Harris, Michael
#mlh758@mail.umkc.edu
#
#Problem: Given an image, allow a user to apply a filter to that image. Filters
#   are graycale, photographic negative, horizontal flip, and blur.
#
#Algorithm:
#1. Ask user for file name, open that file for reading and read each line as a 
#  string into a large list. Strip all the lines of extra white space such as 
#  newlines.
#2. Grayscale: Function takes the file as input. First 3 lines are immediately 
#  added to the new image list as the header. 4th line and beyond become the image
#  data for the rest of the function. For each pixel in image data convert the 
#  strings within the pixel to integers and split on white space. Average the 
#  list to find the grayscale value. Create a string consisting of that value 
#  3 times. Once this has been done for every pixel, return that new image.
#3. Negatives: Store the header and slice off the image data as in Grayscale. 
#  For each pixel, split it into a list and convert the values to integers. 
#  Subtract each value in the pixel from 255, convert back to strings, and join 
#  the list back into a pixel string. Append each pixel to the new image list and 
#  return that list.
#4. Flip image: Store the header and slice off the image data as before. Read 
#  the number of columns and rows from the header and store that information. 
#  Slice off a chunk of pixels equal to that of the number of columns from the 
#  image data. Reverse that row, and append the list to the new image list. Remove 
#  that row from image data and repeat. Return the new image.
#5. Blur: Slice off header, row, and column information like before. Read the 
#  number of columns and rows from the header and store that information. Convert 
#  each pixel into an integer and split into a list as in grayscale. Slice off 
#  column sized chunks of the file and store them as dictionary values tied to 
#  their row number. Iterate through the x and y axis adding each pixel to the 
#  surrounding pixels of the same color, then divide by the number of pixels to 
#  get an average. Do this for each color within each pixel. Return a list of 
#  pixels containing integer values.
#6. Reformat: Convert the values stored in each pixel returned by Blur into a 
#  string. Join those strings back into a complete 3 value string within the list 
#  so the format matches that of the file which was initially red. This can now be 
#  used to feed back into blur for multiple passes or sent to New Image for output. 
#  Return the new list.
#7. New Image: Function for writing regular files. Takes file name and new image 
#  as input. Open a file of the given name for writing. For each line in the image 
#  file write it to the opened file. Close the file when complete.
#8. Main program: Ask the user which filter they would like to apply. Ask user 
#  for a new file name for later writing. Send the file through the appropriate 
#  filter and write the new data to a file of the provided name using the earlier 
#  functions.

######################FUNCTIONS###########################

def grayscale(image):
    """[Image] - Converts an image to grayscale"""
    image_data = image[3:]
    new_image = image[:3]
    for pixel_str in image_data:
        pixel_ints = [int(item) for item in pixel_str.split()]
        new_pixel = str(sum(pixel_ints)//3)
        new_list = new_pixel+' '+new_pixel+' '+new_pixel
        new_image.append(new_list)
    return new_image

def makenegative(image):
    """[Image] - Converts an image to it's photographic negative"""
    image_data = image [3:]
    new_image = image[:3]
    for pixel_str in image_data:
        pixel_ints = [int(item) for item in pixel_str.split()]
        new_pixels = [255-pixel for pixel in pixel_ints]
        new_pixels = [str(item) for item in new_pixels]
        new_image.append(' '.join(new_pixels))
    return new_image

def flipimage(image):
    """[Image] - Flips an image horizontally"""
    image_data = image[3:]
    new_image = image[:3]
    columns = int(image[1].split()[0])
    rows = int(image[1].split()[1])
    for row in range(rows):
        revcolumn = image_data[:columns]
        revcolumn = revcolumn[::-1]
        new_image+=revcolumn
        image_data = image_data[columns:]
    return new_image

def reformat(new_image):
    '''[blurimage] Reformats the output of blur for writing or multiple passes'''
    for x in range(3,len(new_image)):
        for i in range(3):
            new_image[x][i] = str(new_image[x][i])
    new_image[3:] = [' '.join(item) for item in new_image[3:]]
    print("Pass Complete")
    return new_image

def blurimage(image):
    '''[Image] - Builds a dictionary of rows, and applies a blur'''
    image_data = image[3:]
    columns = int(image[1].split()[0])
    rows = int(image[1].split()[1])
    #Convert image data to integers
    for i in range(len(image_data)):
        image_data[i]=[int(item) for item in image_data[i].split()]
    #Turn image data into list of rows
    RD = dict()
    for row in range(rows):
        RD[row] = image_data[:columns]
        image_data = image_data[columns:]
        #RD is now our matrix of columns and rows, keyed by row
        #Name shortened for brevity
    new_image = image[:3]   
    for y in range(rows): #Keys of RD being the y axis or rows
        if y == 0: #Top row, won't be performing y-1 operation
            for x in range(columns):
                new_pix = []
                if x==0: #First column, won't perform x-1
                    for i in range(3): #Index through each pixel
                        new_pix += (RD[y][x][i] + RD[y+1][x][i] + RD[y][x+1][i])//3,
                elif x==max(range(columns)): #Last column, won't perform x+1
                    for i in range(3):
                        new_pix += (RD[y][x][i] + RD[y+1][x][i] + RD[y][x-1][i])//3,
                else:
                    for i in range(3):
                        new_pix += (RD[y][x][i] + RD[y+1][x][i] + RD[y][x+1][i]\
                                    + RD[y][x-1][i])//4,
                new_image.append(new_pix)
        elif y == max(range(rows)): #Last row, won't perform y+1 operation
            for x in range(columns):
                new_pix = []
                if x==0: #First column, won't perform x-1
                    for i in range(3): #Index through each pixel
                        new_pix += (RD[y][x][i] + RD[y-1][x][i] + RD[y][x+1][i])//3,
                elif x==max(range(columns)): #Last column, won't perform x+1
                    for i in range(3):
                        new_pix += (RD[y][x][i] + RD[y-1][x][i] + RD[y][x-1][i])//3,
                else:
                    for i in range(3):
                        new_pix += (RD[y][x][i] + RD[y-1][x][i] + RD[y][x+1][i]\
                                    + RD[y][x-1][i])//4,
                new_image.append(new_pix)
        else: #All other rows
            for x in range(columns):
                new_pix = []
                if x==0: #First column, won't perform x-1
                    for i in range(3): #Index through each pixel
                        new_pix += (RD[y][x][i] + RD[y-1][x][i] + RD[y+1][x][i]\
                                    + RD[y][x+1][i])//4,
                elif x==max(range(columns)): #Last column, won't perform x+1
                    for i in range(3):
                        new_pix += (RD[y][x][i] + RD[y-1][x][i] + RD[y+1][x][i]\
                                    + RD[y][x-1][i])//4,
                else:
                    for i in range(3):
                        new_pix += (RD[y][x][i] + RD[y-1][x][i] + RD[y+1][x][i]\
                                    + RD[y][x+1][i] + RD[y][x-1][i])//5,
                new_image.append(new_pix)

    return reformat(new_image)
        
def newImage(filename, imagefile):
    """[Desired name],[Image being modified] - Will create a new .PPM file
    Does not return a value"""
    if not filename.lower().endswith('.ppm'): #Ensure file name ends with .ppm
        filename = filename+'.ppm'    
    new_image = open(filename, 'w')
    for line in imagefile:
        new_image.write(line+'\n')
    new_image.close()
    return None
    
#############Program Begins###########################
Filed = False
while not Filed:
    try: #Attempt to open the designated file, provide an error if that fails
        Name = input("Please enter the name of the file you wish to modify: ")
        #Read lines into list, strip ending white space
        File = open(Name).readlines()
        File = [line.strip() for line in File]
        Filed = True
    except IOError: #In case file does not exist
        print("Please enter a valid file name.")
        continue

print("What would you like to do?")
print("[1] Convert image to Grayscale")
print("[2] Convert image to a photographic negative")
print("[3] Flip an image horizontally")
print("[4] Apply a blur filter to an image")
selection = input("--> ")
if selection == '1': #Grayscale processing
    new_name = input("Name of new file: ")
    newImage(new_name,grayscale(File))
elif selection == '2': #Negative processing
    new_name = input("Name of new file: ")  
    newImage(new_name,makenegative(File))
elif selection == '3': #Image Flipper
    new_name = input("Name of the new file: ")
    newImage(new_name, flipimage(File))
elif selection == '4': #Blur Filter
    new_name = input("Name of the new file: ")
    print("* This program can perform multiple passes of the blur filter.")
    print("* 1 Pass is very faint, but multiple passes can be time consuming!")
    print("* More than 5 passes and you may want to put the kettle on.")
    #Get the number of passes, verify input is an integer
    iterations = False
    while not iterations:
        try:
            passes = int(input("Enter the number of passes for blurring: "))
        except ValueError:
            print("Please enter an integer")
            continue
        if passes > 7: #A watched pot never boils
            print("Your mother was a hamster, and your father smelled\
of elderberries!")
        iterations = True
    new_image = blurimage(File)
    if passes > 1:
        for x in range(passes-1):
            new_image = blurimage(new_image)
    newImage(new_name, new_image)
    