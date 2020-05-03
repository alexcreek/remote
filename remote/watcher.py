import os
import sys
import dotenv
import inotify.adapters

def main():
    dotenv.load_dotenv()
    try:
        WATCH_DIR = os.environ['WATCH_DIR']
    except KeyError:
        print('Error: WATCH_DIR environment variable not found')
        sys.exit(1)
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
