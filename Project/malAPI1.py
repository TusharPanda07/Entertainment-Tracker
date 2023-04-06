from mal import AnimeSearch
from mal import Anime
from mal import *




'''n=input("enter the anime name")
search = AnimeSearch(n)  # Search for "cowboy bebop"
i=0
while(True):
    i=i+1
    print(search.results[i].title)
    if(search.results[i].title==None):
        break'''
    
'''anime = Anime(i)  # Cowboy Bebop
    print(anime.score)  # prints 8.82
    anime.reload()  # reload object
'''
#x=Anime.get_anime_id("one piece")
#print(x)
anime = Anime(1)
# Cowboy Bebop
print(anime.rating("naruto"))


#print(anime.score)  # prints 8.82

#anime.reload()  # reload object

#print(anime.score("one piece"))  # p





   
 # Get title of first result


#print(anime.score)  # prints 8.81
