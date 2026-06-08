from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pickle
import pandas as pd

app = Flask(__name__)

app.secret_key = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

# Database Model

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )
    
    # Movie Model Loading

movies_dict = pickle.load(
    open('model/movie_dict.pkl', 'rb')
)

similarity = pickle.load(
    open('model/similarity.pkl', 'rb')
)

movies = pd.DataFrame(movies_dict)

# Recommendation Logic

def recommend(movie):

    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in distances[1:6]:
        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations

# Register

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(
            username=username
        ).first()

        if user:
            flash("Username already exists")
            return redirect('/register')

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration Successful")

        return redirect('/login')

    return render_template('register.html')

# Login

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(
            username=username
        ).first()

        if user and check_password_hash(
            user.password,
            password
        ):

            session['user_id'] = user.id
            session['username'] = user.username

            return redirect('/')

        flash("Invalid Credentials")

    return render_template('login.html')

# Logout

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')

# Home

@app.route('/', methods=['GET', 'POST'])
def home():

    if 'user_id' not in session:
        return redirect('/login')

    recommendations = []

    if request.method == 'POST':

        movie = request.form['movie']

        recommendations = recommend(movie)

    return render_template(
        'home.html',
        username=session['username'],
        movies=movies['title'].values,
        recommendations=recommendations
    )


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)