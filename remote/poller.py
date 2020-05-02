import os
import inotify.adapters

def main():
    watch_dir = os.getenv('WATCH_DIR')
    i = inotify.adapters.Inotify()
    i.add_watch('/data/nfs/seedbox/incoming/')

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
