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


def parse_contents_index(file_name, number_of_packages):
    print('Parsing', file_name)

    with gzip.open(file_name, 'rb') as file:
        package_list = []
        for line in file:
            package_list.extend(line.decode().split()[-1].split(','))

    package_stats = {}
    for package in package_list:
        if package in package_stats:
            package_stats[package] += 1
        else:
            package_stats[package] = 1

    package_stats = sorted(package_stats.items(), key=lambda x: x[1], reverse=True)

    print()
    for (order, package) in enumerate(package_stats[:number_of_packages], start=1):
        print(f"{str(order) + '. ' + package[0]:<45} {package[1]}")


if __name__ == '__main__':
    arch = parse_arguments().arch
    file_name = 'Contents-' + arch + '.gz'
    get_contents_index(arch, file_name)
    parse_contents_index(file_name, 10)
    silent_remove_file(file_name)

