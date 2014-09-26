class Movie(object):
    def __init__(self, name=''):
        self.title = name
        self.avg = 0.0
        self.ratings = []
        self.rate_count = 0
    def __str__(self):
        self.avg = self.AvgRating()
        return '{} rated {:.2f} based on {} ratings.'.format(\
            self.title, self.avg, self.rate_count)
    def __repr__(self):
        return self.title+'\n'+','.join([str(x) for x in self.ratings])
    def AddRating(self, x):
        '''[Rating] Adds ratings to a movie object'''
        valid_ratings = [-5,-3,1,3,5]
        if type(x) == str and x.isdigit():
            x=int(x)
        if type(x) == int and x in valid_ratings:
            self.ratings.append(x)
            self.rate_count += 1
    def AvgRating(self):
        '''Updates an object with it's average rating'''
        if self.ratings:
            self.avg = sum(self.ratings)/self.rate_count
        return self.avg