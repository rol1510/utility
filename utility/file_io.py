import os
import sys
import glob

# returns the path of the executed file
def get_dir():
    return os.path.dirname(sys.argv[0])

def get_file_paths_from_wildcard(wildcard):
    if not os.path.isabs(wildcard):
        wildcard = os.path.join(get_dir(), wildcard)
    return glob.glob(wildcard)

def get_file_names_from_wildcard(wildcard):
    paths = get_file_paths_from_wildcard(wildcard)
    return [os.path.basename(p) for p in paths]

def replace_file_name(path, newName):
    name = os.path.basename(path)

    if name == '' or name == None:
        raise ValueError('path does not contain a file name')
    else:
        return path.replace(name, newName)

def process_files(func, file_wildcard):
    files = get_file_paths_from_wildcard(file_wildcard)
    for path in files:
        func(path)
