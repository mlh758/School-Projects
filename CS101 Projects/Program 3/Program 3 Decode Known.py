#Get a file to open and read that file
Name = input("What is the file name? ")
input_str = open(Name).read()
shift_value = int(input("What is the cipher value? "))
new_str = ''

#decode that file
for letter in input_str:
    if (ord(letter) > 90) or (ord(letter) < 65):
        new_str += letter
    else:
        unicode_value = ord(letter)
        #shift it
        unicode_value -= shift_value
        #make it a letter again
        new_letter = chr(unicode_value)
        new_str += new_letter
print(new_str)