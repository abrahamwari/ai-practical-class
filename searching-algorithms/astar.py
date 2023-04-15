#A star
graph = {
    'A' : [['B', 1], ['C', 2],['E',3]],
    'B' : [['A', 1]],
    'C' : [['A', 2], ['E', 4],['D', 5]],
    'E' : [['A', 3], ['C', 4], ['D', 6], ['F', 7]],
    'D' : [['C', 5], ['E', 6], ['F', 3]],
    'G' : [['F', 1]],
    'F' : [['G', 1],['E', 7],['D', 8]],
    }

heuristic = {
    'A' : 25,
    'B' : 2,
    'C' : 30,
    'D' : 7,
    'E' : 6,
    'F' : 8,
    'G' : 0
    }

startstate = 'A'
goalstate = 'G'

queue = [[startstate, 0]]

def orderByCost(queue):
    return sorted(queue, key = lambda x: x[1]+heuristic[x[0][-1]])

while(len(queue)>0):
    print(queue)
    currpath, currcost = queue.pop(0)
    if(currpath[-1] == goalstate):
        print("Success", "\nPath: ", currpath, " ( Cost = ", currcost, ")")
        break
    for node, cost in graph[currpath[-1]]:
        if node in currpath:
            continue
        queue.append([currpath+node, currcost+cost])
    queue = orderByCost(queue)