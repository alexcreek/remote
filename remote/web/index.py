from flask import Blueprint, render_template, current_app
import remote.db

bp = Blueprint('index', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    db = remote.db.Db()
    movies = []
    movies = db.query('SELECT * FROM movie ORDER BY id DESC;')
    return render_template('index.html', movies=movies)
