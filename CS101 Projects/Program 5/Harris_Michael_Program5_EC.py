#CS 101
#Program 4
#Michael Harris
#mlh758@mail.umkc.edu
#
# Algorithm:
#1. Read the ratings file, strip it of newlines, and split on commas. Create a 
#   dictionary of ratings by assigning the first item in the ensuing lists 
#   (the user ID) to be the key and the rest of each list as its associated 
#   value.
#2. Create a list of the movie titles stripping the newline characters.
#3. Ask the user for an ID number
#4. Finding similarity: We must multiply each rating within the ID number's 
#   value with another key's associated values in the dictionary. All the 
#   pairs of ratings should be summed up, this sum stored along with it's key. 
#   Iterate through all the keys doing this. Sort this new list in descending 
#   order by the sum. Once sorted, slice off the keys of the top 5 most similar 
#   users.
#5. Finding movies: Iterate through the ID'd user's list of recommendations. 
#   If you find a 0, look at the associated rating on the list of similar users. 
#   Average out those ratings. If that rating is 3 or greater, add the movie at 
#   that index to a list. Return that list.
#6. Avoiding movies: Iterate through the ID'd user's list. If you find a 0, 
#   look at the associated rating on the most similar user's rating list. If 
#   that rating is lower than -3 add that movie to the list.
#7. Print the movies in both lists using for loops.
#
# Problem: Given a CSV file with user ID numbers and their associated movie
#   ratings; find the users with similar taste and recommend movies to a 
#   specific user based on the ratings of the users most similar to them. The
#   movies are stored in a file as well so that must also be read into a list.
#
# Error handling: My program checks for valid ID numbers before starting
#   to search through the dictionary and make comparisons.
#
# Other comments: I attempted both extra credit assignments in this program.

#########Build lists/dictionaries and define the needed functions############
#Read the rating file and create a dictionary
MovieRatings = open('MovieRatings.txt').readlines()
MovieRatings = [v.strip().split(',') for v in MovieRatings]
rating_dic = {int(line[0]):line[1:] for line in MovieRatings}
#Read the title file and create a list
Titles = open('Prog5Titles.txt').readlines()
Titles = [v.strip() for v in Titles]

#Calculate the similarity of the given user to all others
def similarity(ID):
    """[User ID] - Finds a list of users similar to that of the provided ID"""
    simlist = []
    for key in rating_dic:
        quotient = 0
        IDsum = 0
        if key == ID:
            continue
        userlist = rating_dic[ID]
        complist = rating_dic[key]
        for idx in range(30):
            quotient = int(userlist[idx])*int(complist[idx])
            IDsum += quotient
        simlist.append((key, IDsum))
    simlist.sort(reverse=True, key=lambda rating: rating[1])
    simlist = [rater[0] for rater in simlist]
    return(simlist[:5])

#Find good movies
def findMovies(ID, simlist):
    """[User ID],[List of similar users] - Searches for movies to recommend"""
    userlist  = rating_dic[ID]
    complists = [rating_dic[user] for user in simlist]
    goodlist = []
    for idx in range(30):
        raters_seen = 0
        rater_sum = 0
        if userlist[idx] == '0':
            for rater in complists:
                if int(rater[idx]) != 0: #Rater has seen.
                    raters_seen += 1
                    rater_sum += int(rater[idx])
            rater_avg = rater_sum/raters_seen
            if raters_seen >=2 and rater_avg >= 3.0:
                goodlist.append(Titles[idx])
    return(goodlist)

#Find lame movies
def badMovies(ID,simlist):
    """[User ID],[List of similar users] - Searches for movies to avoid"""
    userlist = rating_dic[ID]
    complist = rating_dic[simlist[0]]
    movielist = []
    for idx in range(30):
        if userlist[idx] == '0':
            if int(complist[idx]) <= -3:
                movielist.append(Titles[idx])
    return(movielist)

##########################Program Begins##############################
interest = True
while interest:
    unnamed = True
    while unnamed:
        try:
            ID = int(input('What is your user number? --> '))
            user_test = [int(rating) for rating in rating_dic[ID]]
            unnamed = False
        except ValueError: #Enters a non digit
            print("Please enter a valid ID number.")
        except KeyError: #User not in the dictionary
            print("No such user exists.")
            
    no_ratings = True
    for rating in user_test:
        if rating != 0:
            no_ratings = False
    
    if no_ratings: #User has no ratings to check against
        print("There are no ratings available for this user.")
    else:   
        simlist = similarity(ID)
        goodmovies = findMovies(ID,simlist)
        badmovies = badMovies(ID,simlist)
       
        #Print the good movies
        print("You are most similar to user #", simlist[0])
        print("\nYou should see the following films: ")
        print("*"*30)  
        for movie in goodmovies:
            if movie in badmovies: #If the other lists suggests they avoid it
                continue #Don't print this one, save it for the bad list            
            print(movie)
            
        #Print the bad movies
        if badmovies:
            print("\nYou should avoid the following films: ")
            print("*"*30)
            for movie in badmovies:
                print(movie)
        else:
            print("*"*30)
            print("There are currently no movies you should avoid.")
            
    #Check to see if the user would like to continue
    print("*"*30)    
    print("Would you like to check a different user?")
    query = input("[Y/N]--> ")
    if query == 'y' or query == 'Y':
        interest = True
    else:
        interest = False
        
print("This has been a Michael Harris production.")