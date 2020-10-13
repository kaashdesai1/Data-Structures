#!/usr/bin/python

from __future__ import print_function
import sys
import random
import collections


class Node(collections.Iterable):

    class NodeIterator:
        def __init__(self, begin):
            self.current = begin

    def __init__(self, element=None, n3xt_node=None):
        self.element = element
        self.n3xt_node = n3xt_node

    def __eq__(self, other):
        return self.element == other

    def __iter__(self):
        current = self
        while current is not None:
            yield current
            current = current.n3xt_node


class Dictionary:
    def __init__(self, length):
        self.count_delete = 0
        self.total_delete = 0

        self.count_insert = 0
        self.total_insert = 0

        self.length = length
        self.elements = [None] * length

    def __getitem__(self, item):
        return self.elements[item]

    def __setitem__(self, item, vue):
        self.elements[item] = vue

    def __contains__(self, item):
        return self.member(item)

    def hash(self, v):
        return hash(v) % self.length

    def insert(self, v):
        if v not in self:
            hsh = self.hash(v)

            current_head = self[hsh]
            node = Node(element=v, n3xt_node=current_head)
            self[hsh] = node

    def delete(self, v):
        
        iter_count = 1
        hsh = self.hash(v)

        if self[hsh] != v:
            node = self[hsh]

            for nxt in node:
                if nxt == v:
                    if nxt.n3xt_node is not None:
                        nxt.n3xt_node = nxt.n3xt_node.n3xt_node
                    break

                iter_count += 1

        self.count_delete += iter_count
        self.total_delete += 1

    def member(self, v):
        iter_count = 1

        hsh = self.hash(v)

        node = self[hsh]

        if node is None:
            self.count_insert += 1
            self.total_insert += 1
            return False

        for nxt in node:
            if nxt == v:
                self.count_insert += iter_count
                self.total_insert += 1
                return True

            iter_count += 1

        self.count_insert += iter_count
        self.total_insert += 1

        return False


def main():

    f = open('openhash.txt', 'w')
    rand_numbers = []
    for i in range(10000):
        rand_numbers.append(random.randint(0, sys.maxint))

    f.write("-"*80 + "\n")
    f.write("Buckets" + "| Insert Count" + "| Deletion Count" + "| Average Insertion" + "| Average Deletion" + "\n")
    f.write("-"*80 + "\n")
    for i in range(1000, 50500, 500):
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
