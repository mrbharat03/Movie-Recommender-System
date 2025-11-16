import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663ea168da84d2e8&language=en-US')
    data = response.json

def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = similarity[idx]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]
    l = []
    for i in movies_list:
        movie_id = i[0]
        l.append(movies.iloc[i[0]].title)
    return l
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(pickle.load(open('movie_dict.pkl', 'rb')))
movies_list = movies['title'].values
st.title('Movie Recommender System')
option = st.selectbox('How would you like to be contacted', movies['title'].values)
if st.button('Recommend'):
    recommendation = recommend(option)
    for i in recommendation:
        st.text(i)