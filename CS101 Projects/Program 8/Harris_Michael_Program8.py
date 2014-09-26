#CS 101
#Program 8
#Harris Michael
#mlh758@mail.umkc.edu
#
#Problem: Create a movie class and use it to process files of movie ratings.
#  Report highest, lowest rated and the most/least seen movies. Store the
#  information in a data file when complete so that it can be retreived later.
#
#Algorithm:
#1. Create a movie.py file where the Movie class will be defined.
#2. The Movie constructor will initialize a title variable which stores the 
#  title of the movie (defaulting to the empty string), an average variable which 
#  will store the average rating of the movie, a ratings list to store ratings, 
#  and a rate counter to keep track of the number of ratings. These are all 
#  defined as zero or empty until member functions change them or in the case of 
#  title if the user provides input.
#3. The string and represent functions will provide a formatted string 
#  containing the necessary data. __repr__ Will return the movie title __str__ 
#  Will call the AvgRating method to ensure it represents an accurate average 
#  in the output.
#4. AddRating takes a potential rating as a parameter. The type is checked, if 
#  it is a string representation of a digit that string is converted to an 
#  integer. Integers are checked against a list of valid ratings, if the integer 
#  is in the valid rating list that integer is appended to the rating list of the 
#  calling object. The rate counter is incremented. All other input is ignored.
#5. AvgRating checks the rating list. If the list has ratings, the function 
#  finds the average of that list. The average is returned. To prevent errors 
#  with the __str__ method, the average variable is declared with the constructor 
#  as 0.0 so if there are no ratings, 0.0 will be returned by default.
#6. The main program reads the titles.txt file and uses the movie titles to 
#  create a list of Movie objects containing each title. The program then reads 
#  the ratings file, removing user ID's, and adds each rating to the appropriate 
# movie. The objects now have their ratings, rate counts, and titles.
#7. MostRated: Function checks the rate counters of all the objects in the 
#   movie list. The movie or movies with the greatest count are returned in a list.
#8. LeastRated: Function checks the rate counters of all the objects in the 
#  movie list. The movie or movies with the lowest count are returned in a list.
#9. HighestRated: Function calls the AvgRating method on every object in the 
#  movie list. The movie or movies with the highest average rating are returned 
#  in a list.
#10. LowestRated: Function calls the AvgRating method on every object in the 
#  movie list. The movie or movies with the lowest average rating are returned 
#  in a list. Calling AvgRating again is redundant but to prevent errors during 
#  testing in the console it will be called.
#11. Print the results of each of the main program functions to the console.
#12. Dump the movie list into a data file using pickle. Close the file.

import movie
import pickle
def mostRatings(movies):
    '''[Movie List] Finds the most rated movie'''
    biggest = -1
    topmovies = list()
    for movie in movies:
        if movie.rate_count > biggest:
            biggest = movie.rate_count
            topmovies = [movie]
        elif movie.rate_count == biggest:
            topmovies.append(movie)
    return topmovies
def leastRatings(movies):
    '''[Movie List] finds the least rated movie'''
    smallest = 999999
    leastmovies = list()
    for movie in movies:
        if movie.rate_count < smallest:
            smallest = movie.rate_count
            leastmovies = [movie]
        elif movie.rate_count == smallest:
            leastmovies.append(movie)
    return leastmovies
def highestRated(movies):
    '''[Movies List] finds the highest rated movie'''
    rating = -20
    topmovies = list()
    for movie in movies:
        if movie.AvgRating() > rating:
            rating = movie.avg
            topmovies = [movie]
        elif movie.avg == rating:
            topmovies.append(movie)
    return topmovies
def lowestRated(movies):
    '''[Movies List] finds the highest rated movie'''
    rating = 99999
    badmovies = list()
    for movie in movies:
        if movie.AvgRating() < rating:
            rating = movie.avg
            badmovies = [movie]
        elif movie.avg == rating:
            badmovies.append(movie)
    return badmovies
    
ratings = open('Ratings.txt').readlines()
ratings = [line.strip().split(',') for line in ratings]
ratings = [line[1:] for line in ratings]
titles = open('Titles.txt').readlines()
titles = [line.strip() for line in titles]

#Populate the movie list and fill the objects with rating data
MovieList = [movie.Movie(title) for title in titles]
for user in ratings:
    for i in range(len(titles)):
        MovieList[i].AddRating(int(user[i]))
#Movie with most ratings
most_rated = mostRatings(MovieList)
print("The most seen film(s) in this class, with {} reviews:"\
      .format(most_rated[0].rate_count))
for movie in most_rated:
    print(movie.title)
#Movie with fewest ratings
least_rated = leastRatings(MovieList)
print("The least seen film(s) in this class, with {} reviews:"\
      .format(least_rated[0].rate_count))
for movie in least_rated:
    print(movie.title)
#Highest Rated
highest_rated = highestRated(MovieList)
print("The best-reviewed film(s) in this class, with a rating of {:.2f}:"\
      .format(highest_rated[0].avg))
for movie in highest_rated:
    print(movie.title)
#Lowest rated
lowest_rated = lowestRated(MovieList)
print("The worst-reviewed film(s) in this class, with a rating of {:.2f}"\
      .format(lowest_rated[0].avg))
for movie in lowest_rated:
    print(movie.title)

#Pickle that sucker
dumpfile = open('MovieList.dat', 'wb')
pickle.dump(MovieList, dumpfile)
dumpfile.close()
print('\nCreating data file.... Done')