from flask import Flask, render_template, request, redirect, url_for, session
import requests
from key import TMDBKey
from key import FlaskKey

app = Flask(__name__)
app.secret_key = FlaskKey


@app.route('/')
def landing():
    if 'guest_session_id' not in session:
        url = f'https://api.themoviedb.org/3/authentication/guest_session/new?api_key={TMDBKey}'
        response = requests.get(url)
        data = response.json()
        session['guest_session_id'] = data['guest_session_id']
    
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDBKey}&language=it-IT'
    response = requests.get(url)
    data = response.json()
    popular_movies = data['results']
    return render_template('index.html', popular_movies=popular_movies)

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
    guest_session_id = session.get('guest_session_id')
    url = f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/watchlist?api_key={TMDBKey}&language=it-IT'
    payload = {
        "media_type": "movie",
        "media_id": movie_id,
        "watchlist": True
    }
    headers = {
        "Content-Type": "application/json;charset=utf-8"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        return redirect(url_for('movie_details', movie_id=movie_id))
    else:
        return "Errore nell'aggiunta alla watchlist", 400

@app.route('/watchlist')
def watchlist():
    guest_session_id = session.get('guest_session_id')
    url = f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/movies?api_key={TMDBKey}&language=it-IT'
    response = requests.get(url)
    data = response.json()
    watchlist_movies = data['results']
    return render_template('watchlist.html', movies=watchlist_movies)

if __name__ == '__main__':
    app.run(debug=True)