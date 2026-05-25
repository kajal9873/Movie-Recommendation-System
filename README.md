🎬 Movie Recommendation System
A content-based movie recommendation system built with Python, Streamlit, and machine learning. Yeh system kisi bhi movie select karne par usse milti-julti 5 movies recommend karta hai — posters ke saath.

📌 Features

🔍 Content-Based Filtering — movie ke overview, genres, keywords, cast aur director ke basis par recommendation
🎭 Top 5 Recommendations — ek movie chunne par 5 similar movies milti hain
🖼️ Movie Posters — TMDB API se real-time posters fetch hote hain
⚡ Precomputed Similarity Matrix — fast recommendation ke liye cosine similarity pehle se calculate ki gayi hai
🌐 Streamlit Web App — simple aur interactive user interface


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

tmdb_5000_movies.csv aur tmdb_5000_credits.csv ko merge kiya jaata hai
Relevant columns rakhe jaate hain: movie_id, title, overview, genres, keywords, cast, crew
Genres, keywords, cast (top 3), aur director extract kiye jaate hain
Sab features ek tags column mein combine hote hain

2. Text Vectorization

Porter Stemmer se words ko root form mein convert kiya jaata hai
CountVectorizer (max_features=5000) se text ko numerical vectors mein convert kiya jaata hai
Cosine Similarity se movies ke beech similarity score calculate hoti hai

3. Web App (app.py)

User ek movie select karta hai dropdown se
System similarity matrix se top 5 similar movies dhundhta hai
Har recommended movie ka poster TMDB API se fetch hota hai
Posters aur titles Streamlit UI mein display hote hain


🛠️ Installation & Setup
Prerequisites

Python 3.8+
pip

Step 1: Repository Clone Karein
bashgit clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
Step 2: Dependencies Install Karein
bashpip install streamlit pandas numpy scikit-learn nltk requests
Step 3: App Run Karein
bashstreamlit run app.py

Note: movies.pkl aur similarity.pkl files pehle se included hain. Agar aap model dobara train karna chahte hain, toh Jupyter Notebook run karein.


📊 Dataset
FileDescriptiontmdb_5000_movies.csvMovie metadata — title, overview, genres, keywordstmdb_5000_credits.csvCast aur crew information
Source: TMDB 5000 Movie Dataset — Kaggle

🔑 TMDB API Key
App mein TMDB API key hardcoded hai posters fetch karne ke liye. Production use ke liye apni key use karein:

TMDB par account banayein
API key generate karein
app.py mein URL update karein:

pythonurl = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"

📈 Model Evaluation
Notebook mein CountVectorizer vs TF-IDF ka comparison bhi kiya gaya hai:

Precision@5 metric se recommendations ki quality measure ki gayi
Paired t-test se statistical significance check kiya gaya
Box plot visualization ke through results compare kiye gaye


🧰 Tech Stack
TechnologyUsePythonCore programming languagePandas & NumPyData manipulationScikit-learnVectorization & cosine similarityNLTKText stemmingStreamlitWeb app UITMDB APIMovie poster fetchPickleModel serialization


📄 License
This project is open-source and available under the MIT License.

🙏 Acknowledgements

TMDB — movie data aur poster API ke liye
Kaggle — dataset ke liye
Streamlit — easy web app framework ke liye
