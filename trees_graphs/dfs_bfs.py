import pprint
pp = pprint.PrettyPrinter(indent=4)

import Queue
myqueue = Queue.Queue() # supports put() and get()
                        # Check if empty using empty() 

# This is a adjacency set. Sets are used
# as its much better since they eliminate
# duplicate entry.
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])
        }

# There is nothing like visit left first then 
# right, just go through the depth of neighbours 
# one by one.

visited = set()
visited_ = set()

def dfs(graph, start, visited):
    # Note this base condition
    if not visited:
        visited.add(start)
    for val in graph[start] - visited:
        if val not in visited:
            print "Visiting {0} -> {1}".format(start, val)
            # Add it to visited just before calling dfs
            visited.add(val)
            dfs(graph, val, visited)
    return visited

def bfs(graph, start, visited):
    # Note this base condition
    if not visited:
        visited.add(start)
    for val in graph[start] - visited:
        if val not in visited:
            print "Visiting {0} -> {1}".format(start, val)
            # Add it to visited just before putting in the queue
            myqueue.put(val)
            visited.add(val)
    while not myqueue.empty():
        bfs(graph, myqueue.get(), visited)
    return visited
    
if __name__ == '__main__':
    print "\nGraph\n"
    pp.pprint(graph)
    print "\nDFS\n"
    dfs(graph, 'A', visited)    
    print "\nBFS\n"
    bfs(graph, 'A', visited_)    
    print '\n'

'''
Notes:

1) In DFS you only need one for loop that is to iterate through
   the neighbours of the node
2) In BFS you need two iteration, one is for the neighbours of 
   the neighbours, and other is to iterate through the queue.
   This second iteration is taken for granted in DFS as recurssion
   maintains the stack for us.
'''
