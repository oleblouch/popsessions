#!/usr/bin/env python3
import os

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('urls')
    args = parser.parse_args()

    with open(args.urls) as f:
        urls = [ x.strip() for x in f.readlines() ]

    for url in urls:
        arr = url.split('/')
        artist = ' '.join([ x.capitalize() for x in  arr[-2].split('-') ])
        title = ' '.join(arr[-1].split('-')[:-2]).capitalize()
        print(f'{artist} - {title} - {url}')