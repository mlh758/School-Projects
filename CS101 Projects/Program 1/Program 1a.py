#CS 101
#Program 1
#Michael Harris
#mlh758@mail.umkc.edu
#Problem: Given a 3 digit number, output a simple number puzzle
#in the format of - 
#                  I am a three-digit number.
#         My tens digit is 5 more than my ones digit.
#        My hundreds digit is 8 less than my tens digit.
#                       What number am I?
#ALGORITHM:
#   1. Receive the number N from user and convert to an integer
#   2. Break that number down into hundreds, tens, and ones by
#      dividing first the whole number by 100. Continue by dividing the
#      remainder of that first quotient by 10. The final remainder is
#      your ones variable.
#   4. Compare these new variables to the 'tens' value via subtraction
#   5. Output the results in the form of the puzzle.
#Error Handling: None

#Ask the user for a number N and store it as an integer.
print("Please enter a 3 digit number with the tens digit at least \n\
as large as the other two.")

N = int(input("Please enter a 3 digit number: "))

#Break that number down into hundreds, tens, and ones.
#Use remainders of each step to build the next.
hundreds = N // 100
r_hundreds = N % 100

tens = r_hundreds // 10
r_tens = r_hundreds % 10

ones = r_tens

#Compare the digits and establish differences.
my_Ten = tens - ones
my_Hundreds = tens - hundreds

#Print those comparisons in the form of the puzzle.
print("\n")
print("I am a three-digit number.")
print("My tens digit is",my_Ten, "more than my ones digit.")
print("My hundreds digit is",my_Hundreds, "less than my ones digit.")
print("What number am I?")
