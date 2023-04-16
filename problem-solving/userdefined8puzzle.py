import copy
def get_input_matrix():
    matrix = []
    for i in range(n):
        row = input("Enter row {} (space-separated integers): ".format(i + 1)).strip().split()
        matrix.append([(x) for x in row])
    return matrix
    
def sort_matrix(initial_state):
    
    flat_list = [item for row in initial_state for item in row]
    
    flat_list.sort()
    
    return [flat_list[i:i+len(initial_state)] for i in range(0, len(flat_list), len(initial_state))]
    
n = int(input("enter value for matrix:"))
print("Put _ for blank space and Enter the initial state of the {}x{} puzzle:".format(n, n))
initial_state = get_input_matrix()
print("The start state is:")
print(initial_state)
sorted_matrix = sort_matrix(initial_state)
print("goal state is")
print(sorted_matrix)
print("sorting start")
startstate = initial_state
goalstate =  sorted_matrix   

visited = []
queue  = [initial_state]

def getNext(node):
    nextStates = []
    for row in range(0, len(node)):
        for col in range(0, len(node[row])):
            if(node[row][col]=='_'):
                if(row==0 or row==1):
                    a = copy.deepcopy(node)
                    a[row][col], a[row+1][col] = a[row+1][col], a[row][col]
                    nextStates.append(a)

                if(row==1 or row==2):
                    a = copy.deepcopy(node)
                    a[row][col], a[row-1][col] = a[row-1][col], a[row][col]
                    nextStates.append(a)
                
                if(col==0 or col==1):
                    a = copy.deepcopy(node)
                    a[row][col], a[row][col+1] = a[row][col+1], a[row][col]
                    nextStates.append(a)

                if(col==1 or col==2):
                    a = copy.deepcopy(node)
                    a[row][col], a[row][col-1] = a[row][col-1], a[row][col]
                    nextStates.append(a)

    return nextStates

while(queue):
    node = queue.pop(0)
    neighbours = getNext(node)
    if node not in visited:
        print(node, end = " ")
        if(node == goalstate):
            break
        print('\n\n Next State\n')
        visited.append(node)
        for neighbour in neighbours:
            queue.append(neighbour)
