# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success)

A web-based Movie Recommendation Engine built with Python and Streamlit. This application suggests movies to users based on their selected preferences using machine learning techniques (Content-Based Filtering).

## 📸 Demo
![App Screenshot](screenshots/app_interface.png)
*(Note: If the screenshot doesn't load, please run the app locally to view the interface.)*

## ✨ Features
* **Interactive Search:** Search for any movie from the database.
* **Smart Recommendations:** Get the top 5/10 similar movies based on content (genres, overview, cast, etc.).
* **Visual Interface:** Displays movie posters and titles dynamically.
* **Responsive Design:** Clean and simple UI powered by Streamlit.

## 🛠️ Tech Stack
* **Language:** Python
* **Frontend:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Cosine Similarity)
* **API:** TMDB API (for fetching movie posters)

## 📂 Project Structure
```bash
movie-recommender-system/
├── data/                   # Dataset files (csv)
├── models/                 # Pre-trained models (.pkl files)
├── screenshots/            # Images for README
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
