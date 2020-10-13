#!/usr/bin/python

from __future__ import print_function
import sys
import random
import collections


class Marker:
    pass

EMPTY = Marker()
DELETED = Marker()


class Dictionary:
    def __init__(self, length):
        self.count_delete = 0
        self.total_delete = 0

        self.count_insert = 0
        self.total_insert = 0

        self.length = length
        self.elements = [EMPTY] * length

    def __getitem__(self, item):
        return self.elements[item]

    def __setitem__(self, item, vue):
        self.elements[item] = vue

    def hash(self, v):
        return hash(v) % self.length

    def locate(self, v):
        hsh = self.hash(v)

        i = 0
        while i < self.length:
            tv = self[self.hash(hsh + i)]

            if tv == v:
                break

            if tv == EMPTY:
                break

            i += 1

        return self.hash(hsh + i), i + 1

    def locate1(self, v):
        hsh = self.hash(v)

        i = 0
        while i < self.length:
            tv = self[self.hash(hsh + i)]

            if tv == v:
                break

            if tv == DELETED:
                break

            if tv == EMPTY:
                break

            i += 1

        return self.hash(hsh + i), i + 1

    def insert(self, v):
        loc, iter = self.locate(v)

        if self[loc] == v:
            return

        loc, iter = self.locate1(v)

        if not (self[loc] == EMPTY or self[loc] == DELETED):
            raise Exception('Table Full')

        self[loc] = v
        self.total_insert += 1
        self.count_insert += iter

    def delete(self, v):
        loc, iter = self.locate(v)

        if self[loc] == v:
            self[loc] = DELETED

            self.total_delete += 1
            self.count_delete += iter


def main():

    f = open('closedhash.txt', 'w')
    rand_numbers = []
    for i in range(2000):
        rand_numbers.append(random.randint(0, sys.maxint))

    
    f.write("-"*80 + "\n")
    f.write("Buckets" + "| Insert Count" + "| Deletion Count" + "| Average Insertion" + "| Average Deletion" + "\n")
    f.write("-"*80 + "\n")

    for i in range(2000, 20500, 500):
        dict = Dictionary(i)

        for num in rand_numbers:
            dict.insert(num)

        for num in rand_numbers:
            dict.delete(num)

        avg_insert = float(dict.count_insert) / dict.total_insert
        avg_del = float(dict.count_delete) / dict.total_delete

        f.write("\n" + '   {} |   {}    |     {}     |       {}     |    {}'.format(i, dict.count_insert, dict.count_delete, avg_insert, avg_del) + "\n")

    f.close()

main()
