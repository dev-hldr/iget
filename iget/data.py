import os
import hashlib

VCS_DIR='.iget'
def init():
    os.makedirs(VCS_DIR)
    os.makedirs(f'{VCS_DIR}/objects')

def set_HEAD(obj_id):
    with open(f'{VCS_DIR}/HEAD', 'w') as f:
        f.write(obj_id)

def get_HEAD():
    if os.path.isfile(f'{VCS_DIR}/HEAD'):
        with open(f'{VCS_DIR}/HEAD') as f:
            return f.read().strip()

def hash_object(data, type_='blob'):
    obj = type_.encode() + b'\x00' + data
    obj_id = hashlib.sha1(obj).hexdigest()
    with open(f'{VCS_DIR}/objects/{obj_id}', 'wb') as out:
        out.write(obj)
    return obj_id

def get_object(obj_id, expected='blob'):
    with open(f'{VCS_DIR}/objects/{obj_id}', 'rb') as f:
        obj = f.read()

    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()

    if expected is not None:
        assert type_ == expected, f'Expected {expected}, got {type_}'
    return content