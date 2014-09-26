#CS 101
#Program 2
#Michael Harris
#mlh758@mail.umkc.edu
#
#PROBLEM: Allow the user to either play a single turn of Pig using the 
#  'Hold on 20' strategy or simulate 10,000 turns of Pig using that strategy.
#   User should be given a menu choice for both of those options. If invalid
#   input is entered into the menu, an error message should be displayed and 
#   the game will continue. When the 10,000 turn simulation ends the game should
#   display the average score and the number of turns that scored 0.
#   At the end of either the simulation or a single turn the user should be 
#   prompted as to whether they would like to continue.
#ALGORITHM:
#  1. Import 'random' into program
#  2. Initialize control variable for first loop which will establish whether
#     the user wishes to continue at the end.
#  3. Create if  and elif statements for the user choices of 1 and 2 for 
#     the menu. Use an else statement to display an error message for 
#     invalid input.
#  4. Loop one in the first if statement will control the choice of playing a 
#     single turn. In this loop, repeatedly generate random numbers (1-6) 
#     and display them as 'Roll'. If that roll is not a 1 add it to a Total 
#     variable. If it is a 1, set the total to 0 and exit the loop.
#  5. Loop two will do the above process 10,000 times without displaying 
#     output for each roll. A turn_total variable will sum up each individual 
#     turn, and will need to be reset for each iteration of the loop. A Total 
#     variable will keep track of the continuing scores. The Count variable 
#     will keep track of the number of turns tested and eventually terminate 
#     the loop. Divide the Total by the Count to attain an average score, 
#     display that information, and exit the loop. On a roll of 1, increment 
#     an additional counter to keep track of the percentage of turns that 
#     scored nothing. This counter will also be divided by the Count variable.
#  6. After either of these loops terminate, prompt the user if they wish to 
#     continue.

import random

#Establish outer loop to contain menu and eventual user decision
user_interest = True
while user_interest:
    print("""Main Menu:
    1) Play 1 turn of Pig
    2) Simulate 10,000 turns""")
    
    #Prompt user for menu selection
    choice = input("Choice: ")
    
    #First operable loop playing 1 turn of Pig
    if choice == '1':
        total = 0
        
        #Loop while score is under 20
        while total < 20:
            Roll = random.randint(1,6)
            print("Roll: ",Roll)
            #If you get a 1, print a 0 score and exit the loop
            if Roll == 1:
                print("Score this turn: 0")
                break
            #Any other number, add to the total and continue
            else:
                total += Roll
        #Loop is over, print the score
        else:
            print("Score this turn: ",total)
    #Now begins loop 2
    elif choice == '2':
        #Initializing the needed variables
        turn_count = 0
        total = 0
        zero_scores = 0
        #Continue until 10,000 turns have been completed
        while turn_count < 10000:
            turn_total = 0 #Reset the counter before the turn starts again.
            
            while turn_total < 20: #A whole lot of loop 1's
                Roll = random.randint(1,6)
                if Roll == 1:
                    zero_scores +=1
                    turn_total = 0
                    break #exits the loop leaving turn_total as 0
                else:
                    turn_total += Roll
            #Add the value to the total and increment the counter
            total += turn_total
            turn_count += 1
                
        #10,000 iterations done, print the statistics    
        total_avg = total/turn_count
        print("Average score: ", total_avg)
        Null_turns = (zero_scores/turn_count)*100
        print("Percent of turns that scored nothing: ", Null_turns,"%")
            
    else:
        print("Error: Please enter a valid selection")
        continue #Menu restarts without jumping to Again? statement
    
    #Final prompt for the user. Resets the entire system.
    again = input("Again? [Y/N] ")
    if again == 'Y' or again == 'y':
        user_interest = True
    elif again == 'N' or again == 'n':
        user_interest = False
    
    else:
        print("Error: Please enter a valid selection")
        continue
else:
    #Program exits with a friendly goodbye message
    print("Goodbye")
    
            
            