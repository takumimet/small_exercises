import os
import hashlib
from sys import argv

script, path = argv

def dir_hash(path):
    return {file: file_md5(os.path.join(path, file)) for file in os.listdir(path)}

def file_md5(filename):
    hashed = hashlib.md5()
    # We use the option rb, since the function works with bytes
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            hashed.update(chunk)
    # This method allows to see the result, otherwise just a generator
    return hashed.hexdigest()

print(dir_hash(path))
