import streamlit as st  # Streamlit for building interactive web app
import pickle  # For loading serialized data objects
import pandas as pd  # Data manipulation library
import requests  # HTTP requests to fetch data from APIs

# Fetch movie poster URL from TMDB API using movie ID
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=936d5e17566f84daf6d48930e7c6855f&language=en-US"
    response = requests.get(url)
    data = response.json()

    poster_path = data.get('poster_path')
    if poster_path:
        # Construct full poster image URL
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        # Return placeholder image if no poster found
        return "https://via.placeholder.com/500x750?text=No+Poster+Found"

# Load movie metadata and similarity matrix from pickle files
movies = pickle.load(open('movies.pkl', 'rb'))  # DataFrame containing movie info
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Precomputed similarity matrix

# Recommend top 5 movies similar to the selected movie
def recommend(movie):
    filtered_movies = movies[movies['title'] == movie]

    if filtered_movies.empty:
        st.error(f"No movie found with title: {movie}")
        return [], []

    movie_index = filtered_movies.index[0]
    distances = similarity[movie_index]
    # Sort movies by similarity score, excluding the movie itself
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_indices:
        movie_id = movies.iloc[i[0]].movie_id  # Retrieve TMDB movie ID
        recommended_movies.append(movies.iloc[i[0]].title)  # Append movie title
        recommended_posters.append(fetch_poster(movie_id))  # Fetch and append poster URL

    return recommended_movies, recommended_posters

# Streamlit UI setup
st.title('🎬 Movie Recommender System')

# Dropdown for selecting movie title
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# Display recommendations on button click
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    if names and posters:
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.markdown(f"**{names[idx]}**")  # Show recommended movie title
                st.image(posters[idx], use_container_width=True)  # Show corresponding movie poster
