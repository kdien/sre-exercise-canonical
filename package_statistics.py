#!/usr/bin/env python3

import argparse
import gzip
import os
import requests


def parse_arguments():
    parser = argparse.ArgumentParser(description='Obtain package statistics from a Debian repository to determine which packages have the most files')
    parser.add_argument('arch', help='Architecture representing the packages')
    return parser.parse_args()


def get_contents_index(arch, file_name):
    base_url = 'http://ftp.uk.debian.org/debian/dists/stable/main/'
    dest_url = base_url + file_name

    print('Downloading Contents index for', arch)
    try:
        response = requests.get(dest_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        silent_remove_file(file_name)
        raise SystemExit(err)

    with open(file_name, 'wb') as file:
        file.write(response.content)

    print('Successfully downloaded', file_name)


def silent_remove_file(path):
    try:
        os.remove(path)
    except OSError:
        pass


def parse_contents_index(file_name):
    print('Parsing', file_name)
    with gzip.open(file_name, 'rb') as file:
        print(file.read())


if __name__ == '__main__':
    arch = parse_arguments().arch
    file_name = 'Contents-' + arch + '.gz'
    get_contents_index(arch, file_name)
    parse_contents_index(file_name)
    silent_remove_file(file_name)

