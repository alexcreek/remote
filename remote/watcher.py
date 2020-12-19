import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

import os
import sys
import sqlite3
import dotenv
import inotify.adapters
import dotenv
from tmdbv3api import Movie
import remote.db

WATCH_DIR = os.getenv('WATCH_DIR', '/data/nfs/seedbox/incoming')

def main():
    db = remote.db.Db()
    i = inotify.adapters.Inotify()
    i.add_watch(WATCH_DIR)

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        if 'IN_CREATE' in type_names:
            logging.info('Found %s', filename)
            t = parse_title(filename)
            if t:
                r = search_tmdb(t)
                if r:
                    title = r[0].title
                    year = r[0].release_date
                    overview = r[0].overview
                    poster_url = 'https://image.tmdb.org/t/p/original{}'.format(r[0].poster_path)

                    logging.info('TMDB thinks this is %s', title)

                    try:
                        db.insert('INSERT INTO movie (name, year, overview, filename, poster_url) VALUES (?, ?, ?, ?, ?);',
                                  title, year, overview, filename, poster_url)
                    except sqlite3.IntegrityError as e:
                        logging.error('Adding %s failed - %s ', title, e)
                        continue

                    logging.info('Added %s', filename)
                else:
                    logging.error('No info found for %s', t)
            
            
        if 'IN_DELETE' in type_names:
            logging.info('Lost %s', filename)
            try:
                db.delete('DELETE FROM movie WHERE filename=?;', filename)
            except sqlite3.IntegrityError as e:
                logging.error('Deleting %s failed - %s ', filename, e)

def parse_title(title):
    a = title.lower().split('.')
    b = None
    try:
        if a.index('1080p'):
            b = a.index('1080p')
        if a.index('720p'):
            b = a.index('720p')
    except ValueError:
        pass
    if not b:
        logging.error('unable to parse title')
        return b
    return(' '.join(a[:b-1]))

def search_tmdb(movie):
    m = Movie()
    return m.search(movie)
    

if __name__ == '__main__':
    dotenv.load_dotenv()
    main()
