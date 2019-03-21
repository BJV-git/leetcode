graph = {'A': ['B', 'C'],
         'B': ['A', 'D','E'],
         'C':['A','F'],
         'D':['B'],
         'E':['B','F'],
         'F':['C','E','L'],
         'L':['A']}

# goal is to visit all the elements ? better to add
# better to do in a recursive manner

def dfs(graph, start):
    visited = set()
    stack = [start]
    order=[]

    limit = len(graph)
    def dfss(start):

        if len(order) != limit: # to stop the entire process when ever the limit has been reached with out going any further

            if start not in visited:
                visited.add(start)
                order.append(start)
            else:
                return

            for i in graph[start]:
                if i not in visited:
                    dfss(i)
        else:
            return

    dfss(start)
    return (order)

print(dfs(graph, 'A'))