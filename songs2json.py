#!/usr/bin/env python3
import os
import json
import glob

txts = glob.glob('songs/*.txt')

songs = [ { 'name':os.path.basename(x).replace('.txt','').split('-'), 'path':x } for x in txts ]

with open('songs.json','wt') as f:
    json.dump(songs,f)
