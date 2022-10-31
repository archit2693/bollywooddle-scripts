import requests
import re
from bs4 import BeautifulSoup
import numpy as np

baseUrl = "https://www.imdb.com/search/title/?title_type=feature&release_date=1995-01-01,2022-12-31&user_rating=6.0,10.0&num_votes=5000,1000000&countries=in&languages=hi&count=250"
movieList = []

url = baseUrl
print(url)
response = requests.get(
	url = url,
)
soup = BeautifulSoup(response.content, 'html.parser')
m = soup.find_all('h3', class_="lister-item-header")
print(m)

for h in m:
	a = h.findAll('a')
	print(a[0].find(text=True))
	movieList.append(a[0].find(text=True))

mylist = list(dict.fromkeys(movieList))
print(mylist)

np.savetxt("topMovies.csv", 
           mylist,
           delimiter =", ", 
           fmt ='% s')


# 	movies = soup.find_all('table', class_='wikitable')
# 	for movie in movies:
# 		for row in movie.find_all('tr'):
# 			cells = row.findAll('i')
# 			if len(cells) > 0:
# 				c = cells[0].find(text=True)
# 				if c != None:
# 					movieList.append(c)

# mylist = list(dict.fromkeys(movieList))
# print(mylist)
# print(len(mylist))
# np.savetxt("movies.csv", 
#            mylist,
#            delimiter =", ", 
#            fmt ='% s')

# finalList = []
# regex = re.compile("^[a-zA-Z0-9]{4}[a-zA-Z0-9]$")
# for movie in mylist:
# 	if movie != None:
# 		res = bool(re.match(regex, movie))
# 		if res == True:
# 			finalList.append(movie)


# print(finalList)
# print(len(finalList))









