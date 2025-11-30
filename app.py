import pickle
import streamlit as st
import requests

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# 2. Custom CSS to improve UI appearance
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border-radius: 5px;
        font-weight: bold;
    }
    .movie-title {
        font-weight: 600;
        font-size: 14px;
        text-align: center;
        margin-top: 5px;
        height: 50px; /* Fixed height for alignment */
        display: flex;
        align-items: center;
        justify-content: center;
    }
    img {
        border-radius: 10px; /* Rounded corners for posters */
        transition: transform .2s; /* Smooth hover effect */
    }
    img:hover {
        transform: scale(1.05); /* Zoom effect on hover */
    }
</style>
""", unsafe_allow_html=True)

# --- Functions ---

def fetch_poster(movie_id):
    # Your existing API logic
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=9549b2abb56a7c0c6c0710daf7d00d58&language=en-US"
    try:
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except:
        # Fallback image if API fails or no poster exists
        return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie_title):
    movie_index = movie[movie['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in movies_list:
        movie_id = movie.iloc[i[0]].movie_id
        recommended_movie_names.append(movie.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movie_names, recommended_movie_posters

# --- Data Loading (Cached for Performance) ---

@st.cache_resource
def load_data():
    movie_data = pickle.load(open('./artifacts/movies.pkl', 'rb'))
    similarity_data = pickle.load(open('./artifacts/similarity.pkl', 'rb'))
    return movie_data, similarity_data

try:
    movie, similarity = load_data()
except FileNotFoundError:
    st.error("Error: Pickle files not found. Please check your './artifacts/' directory.")
    st.stop()

movie_list = movie['title'].values

# --- Main UI Structure ---

st.title("🎬 Movie Recommender System")
st.markdown("### Discover your next favorite film")

# Create a container for the selection to center it or add background if needed
with st.container():
    selected_movie = st.selectbox(
        "Select a movie you like:",
        movie_list
    )

st.write("") # Spacer

if st.button("Show Recommendations"):
    # Add a spinner while fetching data
    with st.spinner('Finding best matches...'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        
        st.write("---") # Divider line
        st.subheader(f"Because you watched *{selected_movie}*:")
        st.write("") # Spacer

        # create 5 columns
        cols = st.columns(5)
        
        # Loop through results to display them cleanly
        for i in range(5):
            with cols[i]:
                # Display Image
                st.image(recommended_movie_posters[i], use_container_width=True)
                # Display Title with custom CSS class for consistent height/alignment
                st.markdown(f"<div class='movie-title'>{recommended_movie_names[i]}</div>", unsafe_allow_html=True)