from flask import Flask, render_template, request, redirect, url_for, session
import requests
from key import TMDBKey, TMDBReadAccessToken, FlaskKey
from DBManager import DBManager

app = Flask(__name__)
app.secret_key = FlaskKey
db = DBManager()


@app.route('/')
def landing():
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={
        TMDBKey}&language=it-IT'
    response = requests.get(url)
    data = response.json()
    popular_movies = data['results']
    session["watchlist_filter"] = 0
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
    url = f'https://api.themoviedb.org/3/search/movie?api_key={
        TMDBKey}&query={query}&language=it-IT'
    response = requests.get(url)
    data = response.json()
    return render_template('search_results.html', movies=data['results'])


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{
        movie_id}?api_key={TMDBKey}&language=it-IT'
    response = requests.get(url)
    infoMovie = response.json()
    tipi = db.get_tipi()
    return render_template('movie.html', movie=infoMovie, tipi=tipi)


@app.route('/watchlist')
def watchlist():
    # guest_session_id = session.get('guest_session_id')
    # url = f'https://api.themoviedb.org/3/guest_session/{guest_session_id}/rated/movies?api_key={TMDBKey}&language=it-IT'
    # response = requests.get(url)
    # data = response.json()
    # watchlist_movies = data['results']
    # return render_template('watchlist.html', movies=watchlist_movies)
    watchlist = db.get_watchlist(session['user_id'], session['watchlist_filter'])
    tipi = db.get_tipi()
    filtro = session["watchlist_filter"]
    return render_template('watchlist.html', movies=watchlist, tipi=tipi, filtro=filtro)


@app.route('/add_to_watchlist', methods=['POST'])
def add_to_watchlist():
    # guest_session_id = session.get('guest_session_id')
    # url = f'https://api.themoviedb.org/3/movie/{movie_id}/rating?api_key={TMDBKey}&guest_session_id={guest_session_id}'
    # rating = request.form['rating']
    # payload = {
    #     'value': rating
    # }
    # response = requests.post(url, json=payload)
    # return redirect(url_for('watchlist'))
    movie_id = request.form['movie_id']
    movie_name = request.form['movie_name']
    watchlist_type = request.form['watchlist_type']
    db.add_to_watchlist(session['user_id'], movie_id,
                        movie_name, watchlist_type)
    session["watchlist_filter"] = 0
    return redirect('/watchlist')


@app.route('/remove_from_watchlist/<int:movie_id>')
def remove_from_watchlist(movie_id):
    db.remove_from_watchlist(session['user_id'], movie_id)
    session["watchlist_filter"] = 0
    return redirect('/watchlist')


@app.route("/change_watchlist_type", methods=['POST'])
def change_Watchlist_type():
    watchlist_type = request.form['watchlist_type']
    session['watchlist_filter'] = int(watchlist_type)
    return redirect("/watchlist")

if __name__ == '__main__':
    app.run(debug=True)
