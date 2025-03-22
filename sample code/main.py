import streamlit as st
import pickle
import requests
import pandas as pd

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])


    recommend_movie = []
    for i in distances[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

option = st.selectbox('How would like to be contacted?', movies['title'].values)

if st.button('recommend'):
    recommendation = recommend(option)
    for i in recommendation:
        st.write(i)

