import os
import hashlib

VCS_DIR='.iget'
def init():
    os.makedirs(VCS_DIR)
    os.makedirs(f'{VCS_DIR}/objects')

def hash_object(data):
    object_id = hashlib.sha1(data).hexdigest()
    with open(f'{VCS_DIR}/objects/{object_id}', 'wb') as out:
        out.write(data)
    return object_id

def get_object(object_id):
    with open(f'{VCS_DIR}/objects/{object_id}', 'rb') as f:
        return f.read()