#!/usr/bin/env python
import os
import re
import json
import requests
from bs4 import BeautifulSoup
from songs2json import songs2json

def parse_url(url, output_dir, overwrite=False):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    for div in soup.body.find_all('div'):
        content = div.get('data-content')
        if content is None:
            continue

    content = json.loads(content)
    store = content['store']
    page = store['page']
    data = page['data']
    tab = data['tab']

    song_name = tab['song_name']
    artist_name = tab['artist_name']

    tab_view = data['tab_view']
    wiki_tab = tab_view['wiki_tab']
    txt = wiki_tab['content']

    txt = re.sub(r'\[ch\](\S*)\[\/ch\]', r'\1', txt)

    txt = re.sub(r'\[tab\]', r'', txt)
    txt = re.sub(r'\[\/tab\]', r'', txt)

    fname = f'{args.output_dir}/{artist_name.replace(" ","_")}-{song_name.replace(" ","_")}.txt'
    
    if os.path.isfile(fname) and not overwrite:
        return

    with open(fname,'wt') as f:
        #f.write(f'{artist_name} - {song_name}\n\n')
        f.write(f'{txt}\n')
    
    print(f'- {artist_name} - {song_name}')
    #print(txt)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir','-o',default='songs')
    parser.add_argument('--overwrite',default=False,action='store_true')
    parser.add_argument('urls')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    with open(args.urls) as f:
        urls = [ x.strip() for x in f.readlines() ]

    for url in urls:
        #print(f'PARSE: {url}')
        parse_url(url, output_dir=args.output_dir, overwrite=args.overwrite)

    # update json
    songs2json()