import os
import sys
import dotenv
import inotify.adapters

def main():
    WATCH_DIR = os.getenv('WATCH_DIR', '/data/nfs/seedbox/incoming')
    i = inotify.adapters.Inotify()
    i.add_watch(WATCH_DIR)

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event
        if 'IN_DELETE' in type_names:
            print('{}{}'.format(path, filename))
            # get info from the db

        if 'IN_CREATE' in type_names:
            print('{}{}'.format(path, filename))
            # get info from tmdb and add it to db

if __name__ == '__main__':
    main()
