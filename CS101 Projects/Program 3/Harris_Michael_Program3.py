#CS 101
#Program 3
#Michael Harris
#mlh758@mail.umkc.edu
#
#Problem: Provide the user with a menu and either encode or decode a message
#   using the Caesar cipher. Create at least 3. One will encode a message, the
#   second will decode a message from a text file using a known shift value,
#   and a third will attempt to determine the shift value from a text file with
#   an unknown cipher. 
#
# Algorithm:
#   1. Convert plain-text to cypher-text. Create a function that will take
#      a string and an integer, convert it to its UTF-8 numerical values, and
#      add the integer to the character value. If you extend beyond Z, restart 
#      at A by subtracting 26 from the value. The function should also convert
#      all text to upper-case to handle invalid input. Ignore all non-letters.
#      Return the cypher-text.
#   2. Decoding cypher-text. Take a string and an integer value for input to
#      a function. Convert the string to UTF-8 values, subtract the integer
#      and ignore all non-letter characters. If you extend outside the A-Z range
#      then reset by adding 26 to the character value. Convert back to letters
#      and return a string.
#   3. Cracking cypher-text. Use only a string for input. Strip all non-letter
#      characters from the string, then determine the 3 most common characters.
#      Assume these are E, T, and A respectively. Determine their shift from
#      their assumed plain-text values on the UTF-8 table. If 2 of the 3 match,
#      use that value for the shift. If none match, assume the single most
#      common character is E and use that shift value. Return a shift value to
#      be used in the second function for decoding.
#   4. Create a user interface to allow interaction with the user. If the user 
#      wishes to decode messages from a file, read that file into a string for
#      use in the second and third functions. Print all output to the screen.
#   5. Provide the user with a choice to continue or not.
#
# Error Handling: All text will be converted to upper-case before processing
#   to ensure smooth handling in the functions. Invalid menu selections will
#   return an error message. Entering a character outside the range of 1-25
#   for a shift value will return an error message and restart.
#
# Other comments: I used collections.Counter(string).most_common(N) to determine
#   the most common characters in the decoded strings. This is a method from
#   the collections library that I found was the easiest way to count
#   characters. It returns the N most common characters from a string in the
#   format [(char1, # of occurences) , (char2, # of occurences), ...]
#   In the program I break that up into individual lists and then slice out
#   just the characters themselves for use in the program.
#
#   I also separated the character counting from cracking the shift value for
#   the sake of simplicity and readability. It made troubleshooting the
#   actual process of determining the shift value easier to manage as well.

import collections #Need this for counting later
#Convert plain text to cyphertext with a given cypher
def encode (input_str, shift_value):
    input_str = input_str.upper() #Turn the input into uppercase
    new_str = ''
    #Encoding a Message
    for letter in input_str:
        if letter.isalpha(): #Only shift for letters
            #Change the character to its unicode value and shift
            unicode_value = ord(letter)
            unicode_value += shift_value
            #Cycle back to the start of the alphabet if we go over
            if unicode_value > 90:
                unicode_value -= 26
            new_char = chr(unicode_value)
            new_str += new_char
        else: #All non-letters stay the same
            new_str += letter
    #Behold, our output!
    return(new_str)

#Decoding cyphertext with a known cypher
def decodeKnown (input_str, shift_value):
    input_str = input_str.upper() #Turn the input into uppercase
    new_str = ''
    for letter in input_str:
        if letter.isalpha(): #Only shift for letters
            #Change the character to its unicode value and shift
            unicode_value = ord(letter)
            unicode_value -= shift_value
            #Cycle back to the start of the alphabet if we go over
            if unicode_value < 65:
                unicode_value += 26
            new_char = chr(unicode_value)
            new_str += new_char
        else: #All non-letters stay the same
            new_str += letter
    #Behold, our output!
    return(new_str)

#Function to find the 3 most common characters
def commonCharacters (input_str):
    input_str = input_str.upper() #Turn the input into uppercase
    #Strip away everything but letters
    new_string = ''
    for letter in input_str:
        if letter.isalpha():
            new_string += letter
        else:
            continue
    #Find top three most common characters
    top_3 = collections.Counter(new_string).most_common(3)
    #Now slice out the characters
    first_char = top_3[0][0]
    second_char = top_3[1][0]
    third_char = top_3[2][0]
    #Create a list
    char_list = [first_char,second_char,third_char]
    return(char_list)

#Function to determine the shift in cypher-text
def ophcrack (char_list): 
    shift_value = 0
    #Turn the list into 3 useable variables
    first_char = char_list[0]
    second_char = char_list[1]
    third_char = char_list[2]
    #Calculate displacement in the alphabet
    E = ord(first_char) - 69 #69 is the value of E in UTF-8
    T = ord(second_char) - 84 #84 is the value of T in UTF-8
    A = ord(third_char) - 65 #65 is the value of A in UTF-8
    #Compensate for negative shift values
    if E < 0:
        E = 26 + E
    if T < 0:
        T = 26 + T
    if A < 0:
        A = 26 + A
    #If two out of three shift values match, that is our shift
    if (E==T) or (E==A):
        shift_value = E
    elif T==A:
        shift_value = T
    else:
        shift_value = E #If all else fails, try it for just the E's
    
    return(shift_value) #This can be fed into decodeKnown


#User interface to the program begins below
user_interest = True
while user_interest == True:
    print("Hello, and welcome to the Caesar Taclane Service")
    first_selection = input("""
    What would you like to do today?
    [1] Encode a message
    [2] Decode a file
    -->""")
    
    
    #Encoding a message
    if first_selection == '1':
        input_str = input("Please enter the text to be encoded: \n")
        print('')
        shift_str = input("Please enter a shift of 1 to 25: ")
        #Verify valid user input
        if shift_str.isdigit(): #.isdigit() verifies input is numerical
            shift_value = int(shift_str)
        else:
            print("Error: Please enter a valid shift value")
            continue
        if 1 <= shift_value <= 25:
            pass #If the input is valid, continue on
        else:
            print("Error: Please enter a valid shift value")
            continue #Otherwise start them over
        cypher_text = encode(input_str, shift_value)
        print(cypher_text,"\n")
    
    
    #Decoding a file
    elif first_selection == '2':
        no_file = True
        while no_file:
            try:
                Name = input("What is the file name? \n -->")
                #Open and read the user's file into a string variable
                input_str = open(Name).read()
                no_file = False
            except IOError:
                print("ERROR: Please enter a valid file name")
                
        
        print("Do you know the cypher of the file?")
        dec_query = input("[Y/N] -->")
        
        if (dec_query == 'Y') or (dec_query == 'y'):
            shift_str = input("Please enter a shift of 1 to 25: ")
            #Verify valid user input
            if shift_str.isdigit():
                shift_value = int(shift_str)
            else:
                print("Error: Please enter a valid shift value")
                continue
            if 1 <= shift_value <= 25:
                pass #If the input is valid, continue on
            else:
                print("Error: Please enter a valid shift value")
                continue #Otherwise start them over
            plain_text = decodeKnown(input_str, shift_value)
            print(plain_text,"\n")
        
        #If they don't know the shift, use the other functions to find it
        elif (dec_query == 'N') or (dec_query == 'n'):
            char_list = commonCharacters(input_str)
            shift_value = ophcrack(char_list)
            plain_text = decodeKnown(input_str, shift_value)
            print(plain_text, "\n")
        
        #Error handling for the [Y/N] input above
        else:
            print("Error: Please enter a valid menu selection value")
            continue            
    
    #Error handling for the main menu
    else:
        print("Error: Please enter a valid menu selection value")
        continue
    
    #Determine if the user would like to go again
    print("Would you like to continue?")
    again = input("[Y/N] -->")
    if (again == 'Y') or (again == 'y'):
        user_interest = True
    elif (again == 'N') or (again == 'n'):
        user_interest = False
    else:
        print("Error: Please enter a valid menu selection value")
        continue

#Exiting the program
print("This has been a Michael Harris production. Goodbye.")
            
        