import argparse
import os
from . import data

def parse_args():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest='command')
    commands.required = True
    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)
    return parser.parse_args()

def main():
    args = parse_args()
    args.func(args)

def init(args):
    data.init ()
    print (f'Initialized empty iget repository in {os.getcwd()}/{data.VCS_DIR}')
