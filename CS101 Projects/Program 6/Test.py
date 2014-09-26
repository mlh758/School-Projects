image = open('hogwarts.ppm').readlines()
image = [line.strip() for line in image]
image_data = image[3:]
columns = int(image[1].split()[0])
rows = int(image[1].split()[1])
image_data = [line.split() for line in image_data]
L = list()
for row in range(rows):
    temp = [int(item[i]) for item in image_data[:columns] for i in range(3)]
    L.append(temp)
    image_data = image_data[columns:]
new_L = list()        
for y in range(rows):
    for x in range(2400):
        try:
            if x < 3 and y == 0:
                pix = (L[y][x]+L[y][x+3]+L[y+1][x])//3
            elif x > max(range(2400))-3 and y ==0:
                pix = (L[y][x]+L[y][x-3]+L[y+1][x])//3
            elif y ==0 and (x!=0 or x > max(range(2400))-3):
                pix = (L[y][x]+L[y][x-3]+L[y][x+3]+L[y+1][x])//4
            elif x < 3 and y == max(range(rows)):
                pix = (L[y][x]+L[y][x+3]+L[y-1][x])//3
            elif x > max(range(2400))-3 and y == max(range(rows)):
                pix = (L[y][x]+L[y][x-3]+L[y-1][x])//3
            elif y == max(range(rows)) and (x!=0 or x > max(range(2400))-3):
                pix = (L[y][x]+L[y][x-3]+L[y][x+3]+L[y-1][x])//4
            else:
                pix = (L[y][x]+L[y][x-3]+L[y][x+3]+L[y-1][x]+L[y+1][x])//5
            new_L.append(pix)
        except IndexError:
            continue
                      