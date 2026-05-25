🎬 Movie Recommendation System
A content-based movie recommendation system built with Python, Streamlit, and machine learning. Given any movie, it recommends 5 similar movies along with their posters fetched in real time from the TMDB API.

📌 Features

🔍 Content-Based Filtering — recommendations based on movie overview, genres, keywords, cast, and director
🎭 Top 5 Recommendations — select any movie and instantly get 5 similar suggestions
🖼️ Movie Posters — real-time poster images fetched from the TMDB API
⚡ Precomputed Similarity Matrix — cosine similarity calculated in advance for fast recommendations
🌐 Streamlit Web App — clean and interactive user interface


🗂️ Project Structure
Movie-Recommendation-System/
│
├── app.py                          # Streamlit web application
├── movie-recommender-system.ipynb  # Jupyter Notebook (data processing + model building)
├── movies.pkl                      # Processed movie data (serialized)
├── similarity.pkl                  # Precomputed cosine similarity matrix
├── tmdb_5000_movies.csv            # TMDB movies dataset
└── tmdb_5000_credits.csv           # TMDB credits dataset (cast & crew)

⚙️ How It Works
1. Data Preprocessing (Notebook)

tmdb_5000_movies.csv and tmdb_5000_credits.csv are merged on the movie title
Only the relevant columns are retained: movie_id, title, overview, genres, keywords, cast, crew
Genres, keywords, top 3 cast members, and the director are extracted from JSON-like strings
All features are combined into a single tags column per movie

2. Text Vectorization

Words are reduced to their root form using Porter Stemmer (NLTK)
Tags are converted to numerical vectors using CountVectorizer (max_features=5000)
A Cosine Similarity matrix is computed across all movie vectors

3. Web App (app.py)

The user selects a movie from a dropdown
The app looks up the movie's row in the similarity matrix and retrieves the top 5 closest matches
Posters for each recommended movie are fetched from the TMDB API
Titles and posters are displayed in a 5-column Streamlit layout


🛠️ Installation & Setup
Prerequisites

Python 3.8+
pip

Step 1: Clone the Repository
bashgit clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
Step 2: Install Dependencies
bashpip install streamlit pandas numpy scikit-learn nltk requests
Step 3: Run the App
bashstreamlit run app.py

Note: movies.pkl and similarity.pkl are already included. If you want to retrain the model from scratch, run the Jupyter Notebook end-to-end first.


📊 Dataset
FileDescriptiontmdb_5000_movies.csvMovie metadata — title, overview, genres, keywordstmdb_5000_credits.csvCast and crew information
Source: TMDB 5000 Movie Dataset — Kaggle

🔑 TMDB API Key
The app uses a TMDB API key to fetch movie posters. For production use, replace it with your own key:

Create an account at TMDB
Generate an API key from your account settings
Update the URL in app.py:

pythonurl = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"

📈 Model Evaluation
The notebook also includes a comparison between CountVectorizer and TF-IDF:

Recommendation quality is measured using the Precision@5 metric
Statistical significance is tested using a paired t-test
Results are visualized with a box plot


🧰 Tech Stack
TechnologyPurposePythonCore programming languagePandas & NumPyData manipulation and analysisScikit-learnVectorization and cosine similarityNLTKText stemmingStreamlitWeb application UITMDB APIFetching movie postersPickleModel serialization


📄 License
This project is open-source and available under the MIT License.

🙏 Acknowledgements

TMDB — for the movie data and poster API
Kaggle — for the dataset
Streamlit — for the web app framework
