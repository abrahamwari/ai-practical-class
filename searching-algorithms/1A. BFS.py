graph = {
  'A' : ['B','C','D'],
  'B' : ['E', 'F','K'],
  'C' : ['G','L'],
  'D' : ['H','I','J'],
  'E' : [],
  'F' : ['M'],
  'K' : ['N'],
  'G' : [],
  'L' : ['P'],
  'H' : [],
  'I' : [],
  'J' : [],
  'M' : [],
  'N' : [],
  'P' : [],

} #dictionary, key is the node, value is the list of nodes that are connected to the key node

visited = [] 
queue = [] 

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


bfs(visited, graph, 'A')

from collections import defaultdict

def BFS(graph, start, goal):

    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)


        if vertex == goal:
            return path


        for neighbor in graph[vertex]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))


    return None

print(BFS(graph, 'A', 'P'))