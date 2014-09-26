#Example Program
#Lead is safe?
#1. Take the number of points one team is ahead
#2. Subtract 3
#3. Add a half point if the team that is ahead has the ball
#   and subtract if the other team has the ball
#4. Square that
#5. If the result is greater than the number of seconds remaining, lead is safe

#Testing possiblity of repeatable program
user_interest = 1
while user_interest == 1:

 #Input number of lead points, decrement by three
 lead_float = float(input("Enter the number of points the lead team is ahead \
 by: "))

 lead_float -= 3

 #Status of the ball
 ball_status = input("Does the lead team have the ball? ")

 #Add or subtract .5 based on results
 if ball_status == 'Yes' or ball_status =='yes' or ball_status == 'y':
    lead_float += .5
 else:
    lead_float -= .5

 #Now square that monkey
 lead_float = lead_float ** 2

 #Input time remaining and compare for safety results
 time_remaining = int(input("How many seconds remain in the game? "))
 if lead_float > time_remaining:
    print("The lead is safe!")
 else:
    print("The lead is not safe, try harder dick bag!")
 
 
#Ask user if they would like to continue and adjust interest variable
#accordingly
 user_request = input("Continue? ")
 if user_request == 'Yes' or user_request =='yes' or user_request == 'y':
    user_interest = 1
 else:
    user_interest = 0

#End game
print ("Good game")