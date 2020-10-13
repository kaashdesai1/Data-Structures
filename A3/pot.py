#!/usr/bin/env python

#Initialize the maximum number of vertices  and the infinity number
MAX_SIZE = 6
MAX_VALUE = 99999

#Priorityqueue class is used as a partially ordered tree
class priorityqueue:
    def __init__(self):
        self.list = []

    def enqueue(self,pair):
        self.list.append(pair)
        self.list.sort(reverse=True)

    def dequeue(self):
        return self.list.pop()

    def isEmpty(self):
        return self.list == []

result = priorityqueue()

#dijkstra class return vertex, distance of vertex, and the previous vertex
def dijkstra(source_vertex, adjacent_list):
    visited = [False] * MAX_SIZE                #visited list is to detect if the path went through a vertex
    D = [MAX_VALUE] * MAX_SIZE
    P = [None] * MAX_SIZE
    #Initialize D and P
    D[source_vertex] = 0                        #D[0] is set to be 0 and the others D are equal to the maximum value
    P[source_vertex] = 0
    while True:
        min_D = MAX_VALUE
        next_vertex = -1
        visited[source_vertex] = True
        for i in range(MAX_SIZE):
            if visited[i]: continue
            if adjacent_list[source_vertex][i]:
                d = D[source_vertex] + adjacent_list[source_vertex][i]
                if d < D[i]:
                    D[i] = d
                    P[i] = source_vertex
            if min_D > D[i]:
                min_D = D[i]
                next_vertex = i
        source_vertex = next_vertex
        if next_vertex == -1: break

    #Push value of vertex, its distance, and its previous vertex into a priority queue
    for i in range(MAX_SIZE):
        result.enqueue([i,D[i],P[i]])
    return result

def print_result():
    while result.isEmpty() == False:
        A = result.dequeue()
        if A[0] == 0:
            continue
        else:
            print "From the source vertex to vertex %d:" %(A[0]+1)
            print "D[%d] = %d | P[%d] = %d" % (A[0]+1, A[1], A[0]+1, A[2]+1)

if __name__ == '__main__':
    adjacent_list = [
        [0, 4, 1, 5, 8, 10],  # Add Edges from vertex 1
        [0, 0, 0, 0, 0, 0],   # Add Edges from vertex 2
        [0, 2, 0, 0, 0, 0],   # Add Edges from vertex 3
        [0, 0, 0, 0, 2, 0],   # Add Edges from vertex 4
        [0, 0, 0, 0, 0, 1],   # Add Edges from vertex 5
        [0, 0, 0, 0, 0, 0],   # Add Edges from vertex 6
    ]
    result = dijkstra(0,adjacent_list)
    print "Test problem 6 of review 2:"
    print_result()
