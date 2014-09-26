def full_house(hand):
    full    = False
    pair    = False
    triples = False
    values = [hand[0][0],hand[1][0],hand[2][0],hand[3][0],hand[4][0]]
    #Check for a pair
    for num in values:
        matches = values.count(num)
        if matches == 2 and num != 'Joker':
            pair = True
            #We know there's only two of them
            values.remove(num)
            values.remove(num)
            break #Prevent it from running again and possibly removing another pair
    #If there's no regular pair, check for Joker. If it's there, create the pair
    #and remove the Joker for the 3 of a kind check
    if pair == False and 'Joker' in values:
        pair = True
        values.remove('Joker')
        
    #Evaluate for triples
    for num in values:
        matches = values.count(num)
        if matches >= 3:
            triples = True
        elif (matches == 2) and 'Joker' in values:
            triples = True
        if values.count('Jokers') == 2:
            triples = True
    if triples and pair:
        full = True
    return(full)