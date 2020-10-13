#!/usr/bin/python

import random

#Node for tree
class Node:
    def __init__(self, x):
        self.element = x
        self.leftchild = None
        self.rightchild = None

class Dictionary:
    def __init__(self):
        self.root = Node(None)
        #to count number of nodes to a node
        self.path = 0

    def INSERT(self, x):
        if self.root == None:
            self.root = Node(x)
        else:
            #CAll helper function 
            self.INSERT_NODE(self.root, x)

    #Helper function to evaluate insertion
    def INSERT_NODE(self, current, x):
        if x <= current.element:
            if current.leftchild == None:
                current.leftchild = Node(x)
            else:
                self.INSERT_NODE(current.leftchild, x)
        elif x > current.element:
            if current.rightchild == None:
                current.rightchild = Node(x)
            else:
                self.INSERT_NODE(current.rightchild, x)
                
    def MEMBER(self, x):
        #Call helper function
        return self.FIND_NODE(self.root, x)
    
    #Helper function to find member
    def FIND_NODE(self, current, x):
        #Later we will ned to -2 from path to exclude root and final node
        self.path = self.path + 1
        if current == None:
            return False
        elif x == current.element:
            return True
        elif x < current.element:
            return self.FIND_NODE(current.leftchild, x)
        else: 
            return self.FIND_NODE(current.rightchild, x)

    def PRINT_PATH(self):
        #path -2 because we exclude root and node itself from calculation
        return self.path - 2


def main():
    f = open('bst.txt','w')
    f.write("Log 2 of 99 is 6.6. Below is average of node visited: \n\n")
    tries = 1
    for t in range(0,6):
        f.write("n = 99 iteratirons = " + str(tries*1000) + "\n")
        sum = 0.00
        for j in range(0,tries*1000):
            tree = Dictionary()
            rand_int = random.sample(xrange(1,100),99)
            for i in rand_int:
                tree.INSERT(i)
            if tree.MEMBER(random.randint(1,50)) != False:
                sum = sum + tree.PRINT_PATH()
        f.write("Average node visited = " + str(sum/(tries*1000)) + "\n")
        tries = tries + 1
    f.close()


main()
