'''
Created on Apr 7, 2018

@author: burust
'''
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()

mc.add_file('lyrics.txt')

lyric = mc.generate_text()
lyric = ' '.join(lyric)

print '(Accompanied by soft guitar riffs, Ed Sheeran sings,)'
print ' '
print '"... ' + lyric + ' ..."'
