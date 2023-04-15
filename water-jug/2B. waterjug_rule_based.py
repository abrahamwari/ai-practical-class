import time
start=time.time()
def getNextStates(state):
    nextStates = []
    if(state[0] < m):
        nextStates.append((m,state[1]))
    if(state[1] < n):
        nextStates.append((state[0],n))
    if(state[0] != 0):
        nextStates.append((0, state[1]))
    if(state[1] != 0):
        nextStates.append((state[0], 0))
    if((state[0] + state[1] >= m) and state[1] > 0):
        nextStates.append((m, state[1] - (m- state[0])))
    if((state[0]+state[1] >= n) and state[0] > 0):
        nextStates.append((state[0] - (n - state[1]), n))
    if((state[0]+state[1] < m) and state[1] > 0):
        nextStates.append((state[0] + state[1], 0))
    if((state[0]+state[1] < n) and state[0] > 0):
        nextStates.append((0, state[0] + state[1]))    
    return nextStates

m = int(input('enter m-')) 
n = int(input('enter n-'))

x = 0
y = 0

goalstate = int(input('enter goalstate-'))

visited = set()
queue = [(x,y)]
path = []
flag = 0
while(len(queue) > 0):
    node = queue.pop(0)
    if(node in visited):
        continue
    visited.add(node)
    path.append(node)
    if(node[0] == goalstate or node[1] == goalstate):
        print("Success ", path)
        flag = 1
        break
    nextStates = getNextStates(node)
    for state in nextStates:
        if(state not in visited):
            queue.append(state)
if(flag == 0):
    print("Solution not found")
end=time.time()
print(end-start)