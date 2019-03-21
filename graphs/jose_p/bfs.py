graph = {'A': ['B', 'C'],
         'B': ['A', 'D','E'],
         'C':['A','F'],
         'D':['B'],
         'E':['B','F'],
         'F':['C','E','L'],
         'L':['A']}

# goal is to visit all the elements ? better to add
# better to do in a recursive manner

def bfs(graph, start):
    visited = set()
    stack = [start]
    order=[]
    i=0
    limit = len(graph)
    visited.add(start)

    while i<limit:

        elem = stack[i]

        for j in graph[elem]:
            if j not in visited:
                stack.append(j)
                visited.add(j)

        i+=1

    return stack

print(bfs(graph, 'A'))
