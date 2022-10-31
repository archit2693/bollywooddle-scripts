import requests
import csv
import json
import urllib.request

class Movie:
  def __init__(self, imdbid, title, ratingCount, rating, genre, actors, director, year, contentType, plot, image):
    self.imdbID = imdbid
    self.title = title
    self.ratingCount = ratingCount
    self.rating = rating
    self.genre = genre
    self.actors = actors
    self.director = director
    self.year = year
    self.contentType = contentType
    self.plot = plot
    self.image = image

# with open('movie_id.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)
# print(data)

baseUrl = "https://imdb-api.tprojects.workers.dev/title/tt"
headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
saveUrl = "http://localhost:8080/api/v1/movie"
basePathForImages = "./topimages/"

# for row in data:
# 	movieId = row[1]
# 	url = baseUrl+movieId
# 	response = requests.get(url)
# 	print(response.json())
# 	j = json.loads(response.content)
# 	movie = Movie(j['id'], j['title'], j['rating']['count'], j['rating']['star'], j['genre'], j['actors'], j['directors'], j['year'], j['contentType'], j['plot'], j['image'])
# 	saveResp = requests.post(saveUrl, data=json.dumps(movie.__dict__), headers=headers)
# 	print(saveResp.json())

def saveMovieInDB(movieId):
	url = baseUrl+movieId
	print(url)
	response = requests.get(url)
	j = json.loads(response.content)
	if not j.get('image') is None:
		movie = Movie(j['id'], j['title'], j['rating']['count'], j['rating']['star'], j['genre'], j['actors'], j['directors'], j['year'], j['contentType'], j['plot'], j['image'])
		saveResp = requests.post(saveUrl, data=json.dumps(movie.__dict__), headers=headers)
		saveImage(j['image'], j['title'])


def saveImage(url, movie):
	full_path = basePathForImages + movie + ".jpg"
	urllib.request.urlretrieve(url, full_path)





