from flask import Flask, render_template, request, redirect, url_for, session
import requests
from key import TMDBKey, TMDBReadAccessToken, FlaskKey
from DBManager import DBManager

app = Flask(__name__)
app.secret_key = FlaskKey
db = DBManager()   


@app.route('/')
def landing():  
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDBKey}&language=it-IT'
    response = requests.get(url)
    data = response.json()
    popular_movies = data['results']
    return render_template('index.html', popular_movies=popular_movies)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/chkLogin', methods=['POST'])
def chkLogin():
    username = request.form['username']
    password = request.form['password']
    result = db.check_login(username, password)
    if result:
        session['user_id'] = result[0]
        return redirect('/')
    return redirect('/login')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/chkRegister', methods=['POST'])
def chkRegister():
    username = request.form['username']
    password = request.form['password']
    result = db.check_register(username)
    if result:
        return redirect('/register')
    db.register_user(username, password)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDBKey}&query={query}&language=it-IT'
    response = requests.get(url)
    data = response.json()
    return render_template('search_results.html', movies=data['results'])

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDBKey}&language=it-IT'
    response = requests.get(url)
    data = response.json()
    return render_template('movie.html', movie=data)

@app.route('/add_to_watchlist/<int:movie_id>', methods=['POST'])
def add_to_watchlist(movie_id):
    # guest_session_id = session.get('guest_session_id')
    # url = f'https://api.themoviedb.org/3/movie/{movie_id}/rating?api_key={TMDBKey}&guest_session_id={guest_session_id}'
    # rating = request.form['rating']
    # payload = {
    #     'value': rating
    # }
    # response = requests.post(url, json=payload)
    # return redirect(url_for('watchlist'))
    print('ciao')

@app.route('/watchlist')
def watchlist():
    # guest_session_id = session.get('guest_session_id')
    # url = f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/movies?api_key={TMDBKey}&language=it-IT'
    # response = requests.get(url)
    # data = response.json()
    # watchlist_movies = data['results']
    # return render_template('watchlist.html', movies=watchlist_movies)
    print('ciao')

if __name__ == '__main__':
    app.run(debug=True)