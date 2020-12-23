import os
import sys
import glob

def get_dir():
    return os.path.dirname(sys.argv[0])

def get_script_dir():
    return os.path.dirname(__file__)

def get_file_paths_from_wildcard(wildcard):
    if not os.path.isabs(wildcard):
        wildcard = os.path.join(get_dir(), wildcard)
    return glob.glob(wildcard)

def get_file_names_from_wildcard(wildcard):
    paths = get_file_paths_from_wildcard(wildcard)
    return [os.path.basename(p) for p in paths]


