#CS101
#Program 10
#Harris Michael
#mlh758@mail.umkc.edu
#Problem: Use the previously created PPMImage and Pixel classes to design
#  an image editor program to manipulate an image in a user friendly way.
#
#Algorithm:
#1. Create a main menu for the PPMImage class. Menu begins within a 
# while loop tied to a user interest variable. Options are as follows:
# Open a file: Retrieves a file name from the user. Calls the PPMImage 
# constructor and assigns the object to a variable. Returns user to the 
# main menu.
# Save: Calls the save method of the PPMImage.
# Save As: Retrieves a new file name from the user, and calls the SaveAs 
#  method of the PPMImage.
# Filters: Brings the user to a filters sub menu where they can choose which 
#  fitlers to apply to the image.
# Quit: Exits the program. If the UnsavedChanges variable is true, prompts the 
#  user to save the image and may call Save or SaveAs methods accordingly.
#2. Filters: Function to be called within a loop tied to a variable. Provides 
# the user with the various image filters and the option to return to the main 
# menu. User can apply filters as they please. When the user chooses to return 
# to the main menu the function returns with an exit code, setting the 
# variable  controlling the loop to False sending control back to the 
# main menu.

import PPMImage
from time import sleep

####################FUNCTIONS#########################
def saver():
    '''Provides compact interface to the SaveAs method in PPMImage'''
    unnamed = True
    while unnamed:
        name = input("New file name: ")
        try:
            File.SaveAs(name)
            unnamed = False
            running = False
        except ValueError:
            print("ERROR: Please enter a valid file name.")
            continue
def filters():
    '''Provides an interface to the image filters'''
    print("""
    [1] Convert to Grayscale
    [2] Convert to Negative
    [3] Lighten Image
    [4] Darken Image
    [5] Reduce Colorspace
    [6] Scroll Image
    [0] Return to main menu""")
    choice = input("--> ")
    if choice == '1':
        File.Grayscale()
    elif choice == '2':
        File.Negative()
    elif choice == '3':
        File.Lighten()
    elif choice == '4':
        File.Darken()
    elif choice == '5':
        File.ReduceColorspace()
    elif choice == '6':
        try:
            File.Scroll()
        except ValueError:
            print("Please enter a valid shift value")
            return True
    elif choice == '0':
        #Return exit code
        return False
    else:
        print("Please make a valid selection")
        return True
    
    #Return continue code
    print("Operation Complete")
    return True
def quitter():
    if File.UnsavedChanges == True:
        savequit = input("Save changes before exit? [Y/N]: ")
        if savequit == 'n' or savequit == 'N':
            return False
        elif savequit == 'y' or savequit == 'Y':
            newfile = input("Create a new file? [Y/N]: ")
        if newfile == 'n' or newfile == 'N':
            File.Save()
            return False
        elif newfile == 'y' or newfile == 'Y':
            saver()
            return False
        else:
            print("Invalid menu selection")    

####################### MAIN PROGRAM #########################
    
File = None
running = True
while running:
    print("""
    [1] Open a PPM Image
    [2] Save Changes
    [3] Save As (Create a new file)
    [4] Filters
    [5] Color Count
    
    [0] Exit""")
    choice = input("\n -->")
    if choice == '1':
        if File:
            choice = input("Would you like to save changes before opening a new file? [Y/N]")
            if choice == 'y' or choice == 'Y':
                choice = input("Save to a new file? [Y/N]")
                if choice == 'y' or choice == 'Y':
                    saver()
                else:
                    File.save()
        name = input("File you wish to open: ")
        File = PPMImage.PPMImage(name)

    elif choice == '2':
        if File:
            File.Save()
        else:
            print("ERROR: You must open a file first")
    elif choice == '3':
        if File:
            saver()
        else:
            print("ERROR: You must open a file first")
    elif choice == '4':
        if File:
            filtering = True
            while filtering:
                #Filters returns a boolean to alter the loop
                filtering = filters()
        else:
            print("ERROR: You must open a file first")
    elif choice == '5':
        if File:
            colors = File.CountColors()
            print("This image contains",colors,"colors")
        else:
            print("ERROR: You must open a file first")

    
    elif choice == '0':
        if File == None:
            running = False
            print("Have a nice day...")
        else:
            if File.UnsavedChanges == True:
                savequit = input("Save changes before exit? [Y/N]: ")
                if savequit == 'n' or savequit == 'N':
                    running = False
                elif savequit == 'y' or savequit == 'Y':
                    newfile = input("Create a new file? [Y/N]: ")
                    if newfile == 'n' or newfile == 'N':
                        File.Save()
                        running = False
                    elif newfile == 'y' or newfile == 'Y':
                        saver()
                        running = False
                    else:
                        print("Invalid menu selection")  
    else:
        print("Please make a valid menu selection.")
print("Have a nice day.")