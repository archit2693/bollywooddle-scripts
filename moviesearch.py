import imdb
import csv
import time
from movieTest import saveMovieInDB

with open('topMovies.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

failedMovies = []
ia = imdb.Cinemagoer()

def searchMovie(name, retry):
	search = ia.search_movie(name)
	if retry > 4:
		failedMovies.append(name)
		return []
	if len(search) > 0:
		return search
	time.sleep(1)
	return searchMovie(name, retry+1)


succesfulStoredCount = 0;

for movie in data:
	name = movie[0]
	search = searchMovie(name, 1)
	if len(search) > 0:
		saveMovieInDB(search[0].movieID)
		succesfulStoredCount = succesfulStoredCount+1


print(failedMovies)