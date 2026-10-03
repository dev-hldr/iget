import os
import hashlib

VCS_DIR='.iget'
def init():
    os.makedirs(VCS_DIR)
    os.makedirs(f'{VCS_DIR}/objects')

def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open(f'{VCS_DIR}/objects/{oid}', 'wb') as out:
        out.write(data)
    return oid
