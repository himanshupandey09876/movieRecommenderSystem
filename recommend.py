import pickle 
import pandas as pd
import requests
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


def fetchposter(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZjI5MWU4ZTMzODI0YzQxMDU1ZjczYWQ4NjJjM2YwNCIsInN1YiI6IjY2NmViNTRlMGViM2EyOWFkZDgzMGIyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BX3NPNPGWSvrSGQC2pZkhKQozdPyygsfzt2DEiKODYU"
        }

    response = requests.get(url, headers=headers)
    data=response.json()

    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
    


def recommend(movie):
    recommended_movies=[]
    recommended_movies_posters=[]
    
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for eachmovie in movies_list:
        # each movie in list is its id and similarity score;
        # fetch movie poster from tmdb 
        movie_id=movies.iloc[eachmovie[0]]['movie_id']
        recommended_movies_posters.append(fetchposter(movie_id))
        # 
        recommended_movies.append(movies.iloc[eachmovie[0]].title)

    return recommended_movies,recommended_movies_posters