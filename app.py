import pickle
import streamlit as st
import pandas as pd

st.title('🎬 Movie Recommendation System')
st.write("Select a movie you like, and we’ll recommend other similar movies for you!")

# Load the pre-trained data
movies = pickle.load(open('/Users/diptarupchakravorty/movie-recommender-system-tmdb-dataset/movie_list.pkl', 'rb'))
similarity = pickle.load(open('/Users/diptarupchakravorty/movie-recommender-system-tmdb-dataset/similarity.pkl', 'rb'))

# Convert movies to DataFrame if not already
movies = pd.DataFrame(movies)

def recommend(movie_title):
    """Recommends movies based on the selected movie title"""
    try:
        index = movies[movies['title'] == movie_title].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]  # Top 5 recommendations

        recommended_movie_names = [movies.iloc[i[0]].title for i in distances]
        return recommended_movie_names

    except IndexError:
        st.error("Sorry, we couldn't find any recommendations for this movie.")
        return []

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Recommendation button
if st.button('Show Recommendations'):
    recommended_movie_names = recommend(selected_movie)

    if recommended_movie_names:
        st.write(f"### Recommended Movies Similar to **{selected_movie}**:")

        # Display recommendations in a list
        for movie in recommended_movie_names:
            st.write(movie)
    else:
        st.write("No recommendations found. Try a different movie!")





