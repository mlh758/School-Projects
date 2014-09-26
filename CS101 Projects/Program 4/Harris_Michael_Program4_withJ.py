#CS 101
#Program 4
#Michael Harris
#mlh758@mail.umkc.edu
#
#Problem: Model a poker game. Generate and shuffle a deck of cards, deal them,
#   and determine the value of each hand. Rank the hands and announce a winner.
#   Jokers will be included.
#
#Algorithm:
#1. Finding a pair: Unpack the card values from the hand into a values list. 
#   Count the occurrences of each value in the list. If it occurs more than 
#   once, you have a pair.
#2. Finding two pairs: Unpack the card values from the hand into a values list. 
#   Begin counting each of the values in the list. If one of those is two 
#   or greater, increment a counter and remove all occurrences of that value 
#   from the list. Begin counting the values again. If a second pair is found, 
#   increment the counter. Once the counter reaches 2 set the value of two 
#   pairs to True and exit the loop.
#3. Three of a kind: Unpack the card values from the hand into a values list. 
#   Count the occurrences of each value in the list. If it occurs at least 3 
#   times you have 3 of a kind.
#4. Straight: Unpack the card values from the hand into a values list. Convert 
#   the list into the numerical values for each card for sorting and comparison. 
#   Create two lists, one for each Aces being high and low. Sort one of the 
#   lists. Iterate through the list, checking to see if the difference between 
#   the current card and the next card is 1. If this is true through the whole 
#   list, you have a straight. If this is not true, try this again on the other 
#   list. If the comparison holds on this list, you have a straight. Otherwise 
#   you do not.
#5. Flush: Unpack the suit values from the hand into a suits list. Count the 
#   occurrences of each suit. If it occurs five times you have a flush.
#6. Full House: Unpack your card values from the hand into a values list. Begin 
#   checking the number of occurrences of each value. If one of the values is 
#   exactly 2, the pair portion is true. Remove those values from the list. 
#   Evaluate the values again, if you have 3 of a kind you now have a full 
#   house.
#7. Four of a kind: Unpack the card values from the hand into a values list. 
#   Count the occurrences of each value in the list. If a value occurs 4 times 
#   you have four of a kind.
#8. Call the functions used to check for both a straight and a flush and assign 
#   them to variables. If both are true, you have a Straight Flush.
#9. Royal Flush: Unpack the card values into a values list. Check each value 
#   against the list of cards needed to have a royal flush. If all five cards 
#   exist your hand is royal. Call the flush function to check if it is a flush. 
#   If both are true, you have a Royal Flush.
#10. Ranking a hand: Call all of the above functions in descending order of 
#   value. Assign each a numerical value that will be assigned to the hand rank 
#   if a function yields True. If a hand has more than one of the above values, 
#   calling the functions in descending order will mean only the highest valued 
#   hand rank will be returned from the function.
#11. Generate a deck: Create a list of card values (A, 2-9, J, Q, K) and a list 
#   of suits (C, H, S, D). Combine all the values with each of the suits using 
#   nested loops and append each new card to a new list. Shuffle that list in 
#   place and return this list.
#12. Players: Retrieve the 5 player names from the user and split them up at 
#   the white space between names. Verify there were 5 names entered. Create 5 
#   lists, one for each player and assign each name to their respective player 
#   number. Add these players to a Player List which will contain all of the 
#   players for later ranking.
#13. Use slicing to assign a card to each player's hand from the deck. 
#   Increment a counter after each card to ensure no cards are repeated.
#14. Call the ranking function to rank each hand and assign that rank to each 
#   player's list. Find the maximum hand rank within the player list and assign 
#   that to a variable representing the winning rank. Print all the players and 
#   their hands. Announce the winners by printing every player's name who had 
#   the winning rank and the hand type associated with that rank as defined 
#   in a dictionary.
#15. Determine if the user wishes to play again.
# 
# Error handling: There is very little user interaction with this program so
#   error handling is minimal. A Try / Except clause is used to ensure exactly
#   5 player names are entered.
#
# Other comments: My program incorporates Jokers in the evaluations.




import random

#Turn an unpacked value list into numerical values for sorting. Aces high.
def acesHigh(values):
    ace_high_dict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14, 'JJ': 99}
    new_list = []
    for num in values:
        if num.isdigit():
            new_list += int(num),
        elif num in ace_high_dict:
            new_list += ace_high_dict[num],
    return(new_list)

#Turn an unpacked value list into numerical values for sorting. Aces low.
def acesLow(values):
    ace_high_dict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 1, 'JJ': 99}
    new_list = []
    for num in values:
        if num.isdigit():
            new_list += int(num),
        elif num in ace_high_dict:
            new_list += ace_high_dict[num],
    return(new_list)

#Check for one pair
def one_pair(hand):
    is_pair = False
    #Unpack the values from the hand
    values = [ t[0] for t in hand if t != 'JJ']+[t for t in hand if t == 'JJ']
    for num in values:
        matches = values.count(num)
        #Verifying at least a pair
        if matches >= 2:
            is_pair = True
    if 'JJ' in values:
        is_pair = True
    return(is_pair)

#Check for two pairs
def two_pair(hand):
    is_two = False
    pair_count = 0
    values = [ t[0] for t in hand if t != 'JJ']+[t for t in hand if t == 'JJ']
    for num in values:
        matches = values.count(num)
        if (matches >= 2) and (num != 'JJ'):
            pair_count += 1
            #Remove all occurances of this value so we can find a second pair
            #We can only do this here because we are only checking for 2 pairs.
            try:
                #Attempt it four times, there can only be 4 of them in the deck
                values.remove(num)
                values.remove(num)
                values.remove(num)
                values.remove(num)
            #Once it errors, stop trying and move on
            except ValueError:
                pass
    if 'JJ' in values:
        pair_count += 1 #If we have a Joker, guaranteed pair
    elif values.count('JJ')==2:
        pair_count += 1 #If there's two of them, there's definitely 2 pairs
        
    if pair_count >= 2: #>= In case we have 2 pairs and a Joker
                        #That would be a full house but 2 pair is also true
        is_two = True
    return(is_two)

#Check for three of a kind
def three_kind(hand):
    triples = False
    values = [ t[0] for t in hand if t != 'JJ']+[t for t in hand if t == 'JJ']
    for num in values:
        matches = values.count(num)
        #Verifying 3 of a kind
        if matches >= 3:
            triples = True
        elif (matches == 2) and 'JJ' in values:
            triples = True
    if values.count('Jokers') == 2:
        triples = True
    return(triples)

#Check for a straight
def straight(hand):
    is_straight = False
    diff = 0
    values = [ t[0] for t in hand if t != 'JJ']+[t for t in hand if t == 'JJ']
    aces_high = acesHigh(values)
    aces_high.sort()
    for index in range(4): #Stop at index 3 to prevent going outside the range
        diff = aces_high[index+1]-aces_high[index]
        if diff != 1:
            if 'JJ' in values:
                values.remove('JJ') #Joker substitutes missing card is
                continue               #removed, and evaluation continues
            else: #If there's no Jokers in the hand and not in sequence
                is_straight = False
                break
        else:
            is_straight = True
    #Only check second list if we don't already have a straight
    if is_straight == False:
        aces_low = acesLow(values)
        aces_low.sort()
        for index in range(4):
            diff = aces_low[index+1]-aces_low[index]
            if diff != 1:
                if 'JJ' in values:
                    values.remove('JJ')
                    continue 
                else:
                    is_straight = False
                    break                 
            else:
                is_straight = True
    return(is_straight)

#Check for a flush
def flush(hand):
    is_flush = False
    #Unpack the suits from the hand
    suits = [ t[1] for t in hand if t != 'JJ']+[t for t in hand if t == 'JJ']
    for i in suits:
        matches = suits.count(i)
        #Check to see if all the suits match
        if matches == 5:
            is_flush=True
        elif (matches == 4) and ('JJ' in suits):
            is_flush=True
        elif (matches == 3) and (suits.count('JJ') == 2):
            is_flush=True
    return(is_flush)

#Check for a full house
def full_house(hand):
    full    = False
    pair    = False
    triples = False
    values = [ t[0] for t in hand if t != 'JJ']+[t for t in hand if t == 'JJ']
    #Check for a pair
    for num in values:
        matches = values.count(num)
        if matches == 2 and num != 'JJ':
            pair = True
            #We know there's only two of them
            values.remove(num)
            values.remove(num)
            break #Prevent it from running again and possibly removing another pair
    #If there's no regular pair, check for Joker. If it's there, create the pair
    #and remove the Joker for the 3 of a kind check
    if pair == False and 'JJ' in values:
        pair = True
        values.remove('JJ')       
    #Evaluate for triples
    for num in values:
        matches = values.count(num)
        if matches >= 3:
            triples = True
        elif (matches == 2) and 'JJ' in values:
            triples = True
        if values.count('Jokers') == 2:
            triples = True
    if triples and pair:
        full = True
    return(full)

#Check for 4 of a kind
def four_kind(hand):
    is_four = False
    values = [ t[0] for t in hand if t != 'JJ']+[t for t in hand if t == 'JJ']
    for num in values:
        matches = values.count(num)
        #If 4 of the cards match it's 4 of a kind
        if matches == 4:
            is_four = True
        elif (matches == 3) and (num != 'JJ') and ('JJ' in values):
            is_four = True
        elif (matches == 2) and (num != 'JJ') and (values.count('JJ') == 2):
            is_four = True
    return(is_four)

#Check for straight flush
def straight_flush(hand):
    is_SF = False
    is_flush = flush(hand)
    is_straight = straight(hand)
    if is_straight and is_flush:
        is_SF = True
    return(is_SF)

#Check for Royal Flush
def royal_flush(hand):
    is_RF = False
    is_royal = False
    RF_count = 0
    values = [ t[0] for t in hand if t != 'JJ']+[t for t in hand if t == 'JJ']
    #Check for a flush
    is_flush = flush(hand)
    #Cards that must be present in a Royal Flush
    RF_list = ['A', 'K', 'Q', 'J', 'T', 'JJ']    
    #Check if you have all 5 required values for a Royal Flush    
    for num in values:
        if num in RF_list:
            RF_count += 1
    if RF_count == 5:
        is_royal = True
    #If you have both of those things, you have a Royal Flush
    if is_royal and is_flush:
        is_RF = True
    return(is_RF)


#Hand ranking function
def h_rank(hand):
    hand_value = 0
    #Test each possible hand in descending order in case there's multiple hits
    #If true, assign that hands rank to hand_value
    if royal_flush(hand):
        hand_value = 9
    elif straight_flush(hand):
        hand_value = 8
    elif four_kind(hand):
        hand_value = 7
    elif full_house(hand):
        hand_value = 6
    elif flush(hand):
        hand_value = 5
    elif straight(hand):
        hand_value = 4
    elif three_kind(hand):
        hand_value = 3
    elif two_pair(hand):
        hand_value = 2
    elif one_pair(hand):
        hand_value = 1
    
    return(hand_value)

#Create a shuffled deck of cards
def genDeck():
    #Lists of suits and ranks
    suit = ['S','H','C','D']
    rank = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    deck = [Vrank+Vsuit for Vrank in rank for Vsuit in suit]
    deck.append('JJ')
    deck.append('JJ')
    random.shuffle(deck) #Shuffle the deck of cards
    return(deck)

#Get names and create a freshly shuffled deck of cards
unnamed = True
while unnamed:
    try: #Validate that user is entering 5 names for the rest of the program.
        all_names = input("Enter names of 5 players, separated by whitespace: ")
        name1,name2,name3,name4,name5 = all_names.split(' ')
        unnamed = False
    except ValueError:
        print("ERROR: Please enter exactly 5 names separated by white space. \n")
        continue
user_interest = True
while user_interest:    
    #Create lists for each name and eventual rank
    Player1, Player2, Player3, Player4, Player5 = [],[],[],[],[]
    Player1.append(name1)
    Player2.append(name2)
    Player3.append(name3)
    Player4.append(name4)
    Player5.append(name5)
    playerList = [Player1,Player2,Player3,Player4,Player5]
    
   
    #Deal the cards
    deck = genDeck()
    card = 0
    hand1,hand2,hand3,hand4,hand5 = [],[],[],[],[]
    while card <= 20:
        hand1.append(deck[card])
        card +=1
        hand2.append(deck[card])
        card +=1
        hand3.append(deck[card])
        card +=1
        hand4.append(deck[card])
        card +=1
        hand5.append(deck[card])
        card +=1

    
    #Rank the hands
    Player1.append(h_rank(hand1))
    Player2.append(h_rank(hand2))
    Player3.append(h_rank(hand3))
    Player4.append(h_rank(hand4))
    Player5.append(h_rank(hand5))
    
    #Dictionary of winning values
    win_dict = {0: 'Nothing', 1: 'a Pair', 2: 'Two Pairs', 3: 'Three of a kind',
                4: 'a Straight', 5: 'a Flush', 6: 'a Full House', 
                7: 'Four of a kind', 8: 'a Straight Flush', 9: 'a Royal Flush'}    
    #Determine the winning rank
    winRank = max([player[1] for player in playerList])
    print("{:7}: {}".format(Player1[0], hand1))
    print("{:7}: {}".format(Player2[0], hand2))
    print("{:7}: {}".format(Player3[0], hand3))
    print("{:7}: {}".format(Player4[0], hand4))
    print("{:7}: {}".format(Player5[0], hand5))
    for player in playerList:
        if player[1] == winRank:
            print('{:7} wins with {}!'.format(player[0], win_dict[winRank]))
    
    
    #Decide if the user wants to play again
    print("Deal again?")
    again = input("[Y/N] -->")
    if (again == 'Y') or (again == 'y'):
        user_interest = True
    elif (again == 'N') or (again == 'n'):
        user_interest = False
    else:
        print("Error: Please enter a valid menu selection value")
        continue

print('This has been a Michael Harris production.')
