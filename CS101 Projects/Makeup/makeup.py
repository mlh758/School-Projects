speech = open('debate.txt')
speech = [line.strip().split() for line in speech if line != '\n']
stopwords = open('stop.txt').readlines()
stopwords = [line.strip() for line in stopwords]
titles = 'Crowley', 'Romney', 'Obama', 'President', 'Governor',  'Candy', 'Mr.'
for word in titles: stopwords.append(word)
stopwords = [word.lower() for word in stopwords]

speakers = {'CROWLEY:':list(), 'ROMNEY:':list(), 'OBAMA:':list()}

for line in speech:
    if line[0] in speakers:
        current = line[0]
        for word in line: word = word.lower().strip('?.",!()')
        if word not in stopwords and word not in \
           [person.lower() for person in speakers] and word.isalpha():
            speakers[current].append(word)    
            
Obama = {word:speakers['OBAMA:'].count(word) for word in \
         set(speakers['OBAMA:']) if word != ''}
Romney = {word:speakers['ROMNEY:'].count(word) for word in \
          set(speakers['ROMNEY:']) if word != ''}
obama_top = sorted(Obama, key = Obama.get, reverse = True)[:30]
romney_top = sorted(Romney, key = Romney.get, reverse = True)[:30]