import argparse
import os
from . import data

def parse_args():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)

    hash_object_parser = commands.add_parser('hash-object')
    hash_object_parser.set_defaults(func=hash_object)
    hash_object_parser.add_argument('file')

    return parser.parse_args()

def main():
    args = parse_args()
    args.func(args)

def init(args):
    data.init()
    print(f'Initialized empty iget repository in {os.getcwd()}/{data.VCS_DIR}')

def hash_object (args):
    with open(args.file, 'rb') as f:
        print(data.hash_object (f.read()))
