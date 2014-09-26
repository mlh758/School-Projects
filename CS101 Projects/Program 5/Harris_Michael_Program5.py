MovieRatings = open('MovieRatings.txt').readlines()
MovieRatings = [v.strip().split(',') for v in MovieRatings]
Titles = open('Prog5Titles.txt').readlines()
Titles = [v.strip() for v in Titles]
rating_dic = {int(line[0]):line[1:] for line in MovieRatings}

#Calculate the similarity of the given user to all others
def similarity(ID):
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
    simlist = simlist[0]
    return(simlist)

def findMovies(ID, simlist):
    userlist = rating_dic[ID]
    complist = rating_dic[simlist[0]]
    movielist = []
    for idx in range(30):
        if userlist[idx] == '0':
            if int(complist[idx]) >= 3:
                movielist.append(Titles[idx])
    return(movielist)

def badMovies(ID,simlist):
    userlist = rating_dic[ID]
    complist = rating_dic[simlist[0]]
    movielist = []
    for idx in range(30):
        if userlist[idx] == '0':
            if int(complist[idx]) <= -3:
                movielist.append(Titles[idx])
    return(movielist)
            
    
    


ID = int(input('What is your user number? --> '))
user_test = [int(rating) for rating in rating_dic[ID]]
if sum(user_test)==0:
    print("There are no ratings available for this user.")
else:   
    simlist = similarity(ID)
    goodmovies = findMovies(ID,simlist)
    badmovies = badMovies(ID,simlist)
    #Print the good movies
    print("You are most similar to user #", simlist[0])
    print("You should see the following films: ")
    print("*"*30)  
    for movie in goodmovies:
        print(movie)
        
    #Print the bad movies
    print("*"*30)    
    print("You should avoid the following films: ")
    for movie in badmovies:
        print(movie)