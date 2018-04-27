'''
Created on Apr 7, 2018

@author: burust
'''

import requests
from bs4 import BeautifulSoup


#list of URLs containing lyrics to Ed Sheeran songs
team_urls = ['http://www.lyricsfreak.com/e/ed+sheeran/thinking+out+loud_21083784.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/photograph_21058341.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/a+team_20983411.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/i+see+fire_21071421.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/perfect_21113253.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/castle+on+the+hill_21112527.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/supermarket+flowers_21113249.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/lego+house_20983415.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/even+my+dad+does+sometimes_21085123.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/kiss+me_20983414.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/shape+of+you_21113143.html',
            'http://www.lyricsfreak.com/e/ed+sheeran/i+see+fire_21071421.html'
]

found = ' '

#scrape lyrics from sites and compile them under one variable
for url in team_urls:
    page = requests.get(url)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.select_one('#content_h')

    for e in soup.find_all('br'):
        e.replace_with('\n')
    found += div.text
    
# Save data in a file
string = ''
for word in found:
    string += word
    string = string.encode('ascii', 'ignore').decode('ascii')

# Open a file
f = open("lyrics.txt", "w")

f.write(string)

# Close open file
f.close()