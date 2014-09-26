image = open('hogwarts.ppm').readlines()
image = [line.strip() for line in image]

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

new_image = []   
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










































#CD = dict()
##Build a dictionary for comparing values
#for key in range(rows):
    ##Split the data into rows by slicing off chunks based on columns
    #temp = image_data[:columns]
    ##Turn each row into one long list of integers, maintaining the order
    #temp = [int(pixel.split()[i]) for pixel in temp for i in range(3)]
    ##Now that each pixel is an integer, store it in a dictionary
    #CD[key] = temp
    ##Remove that row from the image data
    #image_data = image_data[columns:]
    #new_dict = dict()
#for row in range(rows):
    #new_row = []
    #if row > 0 and row !=max(range(rows)): #For all rows but first and last
        #for i in range(columns):
            #if i == 0: #Don't go back a pixel for first column
                #newI = (CD[row][i]+CD[row][i+3]+CD[row-1][i]+CD[row+1][i])//4
            #elif i == max(range(columns)): #Don't go forward for last column
                #newI = (CD[row][i]+CD[row][i-3]+CD[row-1][i]+CD[row+1][i])//4
            #else:
                #newI = (CD[row][i]+CD[row][i+3]+CD[row][i-3]+CD[row-1][i]\
                                    #+CD[row+1][i])//5
            #new_row.append(newI)
    #elif row == 0: #For first row
        ##Won't be moving up a row for averages
        #for i in range(columns):
            #if i == 0:
                #newI = (CD[row][i]+CD[row][i+3]+CD[row+1][i])//3
            #elif i == max(range(columns)):
                #newI = (CD[row][i]+CD[row][i-3]+CD[row+1][i])//3
            #else:
                #newI = (CD[row][i]+CD[row][i+3]+CD[row][i-3]+CD[row+1][i])//4
            #new_row.append(newI)
    #elif row == max(range(rows)): #Final row
        ##Won't be moving down a row for averages
        #for i in range(columns):
            #if i == 0:
                #newI = (CD[row][i]+CD[row][i+3]+CD[row-1][i])//3
            #elif i == max(range(columns)):
                #newI = (CD[row][i]+CD[row][i-3]+CD[row-1][i])//3
            #else:
                #newI = (CD[row][i]+CD[row][i+3]+CD[row][i-3]+CD[row-1][i])//4
            #new_row.append(newI)
    
    #new_dict[row]=new_row