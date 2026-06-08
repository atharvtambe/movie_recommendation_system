# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Machine Learning** and **Flask**. The application recommends movies similar to a selected movie by analyzing movie metadata such as genres, keywords, cast, crew, and overview.

## 🚀 Features

* User Registration & Login Authentication
* Content-Based Movie Recommendation
* Modern Flask Web Interface
* Responsive Design
* Movie Similarity Search
* Secure Password Hashing
* Ready for TMDB Poster Integration

---

## 🛠️ Tech Stack

* Python
* Flask
* Pandas
* NumPy
* Scikit-Learn
* NLTK
* SQLite
* HTML
* CSS
* JavaScript

---

## 📊 Dataset

The dataset used in this project was obtained from **Kaggle** and contains movie metadata including:

* Movie Title
* Genres
* Keywords
* Cast
* Crew
* Overview

---

## ⚙️ Machine Learning Workflow

### 1. Data Preprocessing

* Removed missing values
* Merged relevant movie features
* Created a combined `tags` column
* Converted text into lowercase format

### 2. Text Processing

Applied stemming using NLTK's Porter Stemmer:

```python
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
```

This helps reduce words to their root forms and improves recommendation quality.

### 3. Vectorization

Used CountVectorizer to convert textual data into numerical vectors:

```python
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000, stop_words='english')
```

### 4. Similarity Calculation

Computed cosine similarity between movie vectors to find movies with similar content.

---

## 📂 Project Structure

```text
movie_recommendation_system_flask/
│
├── app.py
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── home.html
│
├── instance/
│   └── users.db
│
└── README.md
```

---

## ⚠️ Model Files Not Included

The trained model files:

```text
movie_dict.pkl
similarity.pkl
```

are **not included in this repository**.

### Why?

GitHub has a file size limit of **100 MB**, while the generated similarity matrix is significantly larger than this limit.

To keep the repository lightweight and GitHub-friendly, these files have been excluded using `.gitignore`.

If you want to run the project locally, you can:

1. Generate the model files by running the notebook/script used for preprocessing and training.
2. Or download the model files from a shared Google Drive link (if provided).

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/atharvtambe/movie_recommendation_system.git
```

### Navigate to Project

```bash
cd movie_recommendation_system
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🎯 Future Improvements

* TMDB API Integration
* Movie Posters & Ratings
* Recommendation History
* User Favorites
* Personalized Recommendations
* Deploy on Render/Railway

---

## 👨‍💻 Author

**Atharv Tambe**

GitHub: https://github.com/atharvtambe

If you found this project interesting, consider giving it a ⭐ on GitHub.
