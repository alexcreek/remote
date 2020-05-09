import time
import sys
from threading import Thread
from subprocess import run
from flask import Blueprint, render_template, current_app, jsonify
from plexapi.server import PlexServer

bp = Blueprint('backend', __name__)

src = '/watch'
dst = '/movies'

@bp.route('/copy/<filename>')
def copy(filename):
    t = Thread(target=copy_file, args=(filename,))
    t.start()
    return jsonify(filename)

@bp.route('/delete/<filename>')
def delete(filename):
    t = Thread(target=delete_file, args=(filename,))
    t.start()
    return jsonify(filename)

def copy_file(filename):
    path = '{}/{}'.format(src, filename)
    run(['cp', '-ar', path, dst])
    update_plex()

def delete_file(filename):
    path = '{}/{}'.format(dst, filename)
    run(['rm', '-rf', path])
    update_plex()

def update_plex():
    baseurl = 'http://192.168.1.10:32400'
    token = ''
    plex = PlexServer(baseurl, token)
    movies = plex.library.section('Movies')
    movies.update()
