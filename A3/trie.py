#!/usr/bin/env python

import string

class trienode:
    def __init__(self):
        self.array = dict()

    def assign(self, c, p):
        self.array[c] = p

    def valueof(self,c):
        return self.array[c]

    def getnew(self,c):
        self.array[c] = trienode()

    def makenull(self):
        self.array = {}

    def insert(self, x):
        i = 0
        t = self
        trie_node = 0
        while x[i] != "$": 
            new = True
            for key in t.array:
                if key == x[i]:
                    new = False
            if new == True:
                t.getnew(x[i])
                trie_node = trie_node + 1
            t = t.valueof(x[i])
            i = i+1
        t.assign("$",None)
        return trie_node


root = trienode()
trie_height = 0
trie_node = 0
print("Insert all the words from 'Alice in Wonderland.txt' to the trie, all the special characters are removed, Capital letters are considered a new character")
with open('Alice-in-Wonderland.txt', 'r') as f:
    for line in f:
        for word in line.split():
            word = ''.join(e for e in word if e.isalnum())
            trie_node = root.insert(word + "$") + trie_node
            if len(word) > trie_height:
                trie_height = len(word)
print("Trie height is the longest possible path from the root of trie to one of its leaf, same length with the longest word")
print("Trie_height = ", trie_height)
print("Total node of the trie = ", trie_node)
