#!/usr/bin/env python

class vertex:
    def __init__(self,lb,l):
        self.label = lb
        self.list = l # list of the vertex that linked to this vertex
        self.mark = 0 # 0 stand for unvisited, 1 stand for visited

    def dfs(self):
        self.mark = 1
        print(self.label, end = ' ')
        for v in self.list:
            if v.mark == 0:
                v.dfs()

def link(node, nodelist):
        for item in nodelist:
            node.list = node.list.append(item)
    
def unmark(list):
        for node in list:
            node.mark = 0



a = vertex("a",[])
b = vertex("b",[])
c = vertex("c",[])
d = vertex("d",[])
e = vertex("e",[])
f = vertex("f",[])

a = vertex("a",[b,d,f])
b = vertex("b",[c,f])
c = vertex("c",[d])
d = vertex("d",[b])
e = vertex("e",[d,f])
f = vertex("f",[d])

#link(a,[b,d,f])
#link(b,[c,f])
#link(c,[d])
#link(d,[b])
#link(e,[d,f])
#link(f,[d])

print("Visited node if start at node a:")
a.dfs()
unmark([a,b,c,d,e,f])
print()

print("Visited node if start at node b:")
b.dfs()
unmark([a,b,c,d,e,f])
print()

print("Visited node if start at node c:")
c.dfs()
unmark([a,b,c,d,e,f])
print()

print("Visited node if start at node d:")
d.dfs()
unmark([a,b,c,d,e,f])
print()

print("Visited node if start at node e:")
e.dfs()
unmark([a,b,c,d,e,f])
print()

print("Visited node if start at node f:")
f.dfs()
unmark([a,b,c,d,e,f])
print()
