
# Algorithm:
#1. Ask user for name of input file. Read lines of file stripping extra white 
#  space and splitting on commas.
#2. Each line becomes an entry in a movie dictionary. The first item in the 
#  line – the movie title – is the key while the rest of the line 
#  becomes the value.
#3. The aggregated values in the dictionary are placed in a set to create a 
#  collection of actors without duplicates. George Clooney is excluded and used 
#  to create a new list of tuples. Each tuple is an actor with their associated 
#  Clooney number. Clooney himself gets a 0 when placed in the list.
#4. Iterate through the dictionary. For each movie Clooney is in, all the actors
#  in that movie are added to the Cloonies list with a number of 1 while being
#  removed from the actor set. That key is added to a key deletion list.
#5. Clooneytize: Function takes n (Clooney number to be rated) as input. For 
#  every actor in the Cloonies list with n-1 Clooney number, find every movie 
#  they appear in and give all the actors in that movie a Clooney number of n 
#  in the Cloonies list while removing them from the actor set. That 
#  key is added to the deletion list.
#6. Repeat the iteration until there are no keys in the deletion list. 
#  After each iteration delete the listed keys and increment n. Empty the 
#  list before starting 
#  the Clooneytize function again.
#7. Actors.txt: Create a function that iterates through a sorted Cloonies list 
#  and writes each actor along with their Clooney number.
#8. Numbers.txt: Create a function that iterates based on a range of n through a 
#  sorted Cloonies list.  Each actor with a Clooney number n is written under the 
#  appropriate header based on n. All actors with None are written before the range 
#  n based loop begins, still in a sorted Cloonies list.

def clooneytize(n):
    '''[Current Clooney #] - Generates Clooney numbers'''
    for actor in cloonies:
        if actor[1] == n-1:
            for k in d_movies.keys():
                if actor[0] in d_movies[k]:
                    delete_keys.add(k)
                    for person in d_movies[k]:
                        if person in actors:
                            cloonies.append((person, n))
                            actors.remove(person)

#Ask the user for the input file, check it for erros
unnamed = True
while unnamed:
    try:
        filename = input("Enter the name of the input file: ")
        unnamed = False
    except IOError:
        print("Error: File not found.")
        continue
#Open the file, strip whitespace and split on commas
File = open(filename).readlines()
File = [line.strip().split(',') for line in File]

#Build the dictionary of movies:actors along with a set of just actors
d_movies = {line[0]:line[1:] for line in File}
actors = {actor for actor_L in d_movies.values() for actor in actor_L if actor \
          != 'George Clooney'}
#Start a Clooney Number list
cloonies = [('George Clooney', 0)]

#Initialize Delete Keys so loop will enter the first time
delete_keys = {1,2,3}
#Now iterate through the rest of the movies and actors to assign numbers
n=1
while delete_keys:
    delete_keys = set()
    clooneytize(n)
    for movie in delete_keys:
        del d_movies[movie]
    n += 1
#Stick the remaining actors into the Clooney list with 'None'
for actor in actors:
    cloonies.append((actor, 'None'))

#Write actors.txt file
Fout_act = open('actors.txt', 'w')
for x in sorted(cloonies):
    Fout_act.write('{:20}\t{}'.format(x[0],x[1])+'\n')
Fout_act.close()

#Write numbers.txt file
Fout_num = open('numbers.txt', 'w')
Fout_num.write('The following actors do not have a Clooney Number: \n')
for x in sorted(cloonies):
    if x[1] == 'None':
        Fout_num.write('    {:20}'.format(x[0])+'\n')
for num in range(n):
    Fout_num.write('The following actors have a Clooney Number of {}:'\
                   .format(num)+'\n')
    for x in sorted(cloonies):
        if x[1] == num:
            Fout_num.write('    {:20}'.format(x[0])+'\n')
Fout_num.close()