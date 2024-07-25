#!/usr/bin/env python3
import os
import json
import glob

def songs2json():
    # EN
    txts = glob.glob('songs/*.txt')
    songs = [ { 'lang':'en','name':os.path.basename(x).replace('.txt','').split('-'), 'path':x } for x in sorted(txts) ]

    # FR
    txts = glob.glob('songs_fr/*.txt')
    songs += [ { 'lang':'fr','name':os.path.basename(x).replace('.txt','').split('-'), 'path':x } for x in sorted(txts) ]

    with open('songs.json','wt') as f:
        json.dump(songs,f)

if __name__ == '__main__':
    songs2json()