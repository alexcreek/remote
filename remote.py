from flask import Flask, render_template
import os
import time

app = Flask(__name__)
movie_dir = '/data/rutorrent/incoming'

@app.route('/')
def index():
    movies = [x for x in sorted(os.listdir('/data/rutorrent/incoming'))]

    foo = [(x[0], time.ctime(x[1].st_ctime)) for x in sorted([(fn, os.stat(movie_dir + '/' + fn)) for fn in movies], key = lambda x: x[1].st_ctime, reverse=True)]
    bar = [x[0] for x in foo]

    return render_template('index.html', movies=bar)

