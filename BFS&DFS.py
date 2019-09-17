graph = {
    "A": ["B"],
    "B": ["A", "C", "D"],
    "C": ["B", "D"],
    "D": ["B", "C", "E","F"],
    "E": ["D", "F"],
    "F": ["D", "E", "G"],
    "G": ["F"],
}
# Create BFS algorithm, parameters are graph and vertex in it.
def BFS(graph,vertex):
    # Create queue to contain.
    queue = []
    # Add the first vertice to the queue
    queue.append(vertex)
    # Use set to save vertex which have been visited.
    looked = set()
    # Add the first vertice because it was visited.
    looked.add(vertex)
    # Traversal when queue is not empty.
    while(len(queue)>0):
        # Get the node from head of queue and search vertex adjacent to it.
        temp = queue.pop(0)
        nodes = graph[temp]
        # Visit all the neighbor vertex.
        for newnode in nodes:
            # Judge whether it was visited.
            if newnode not in looked:
                # If not been visited, add it to queue and visited nodes.
                queue.append(newnode)
                looked.add(newnode)
        print(temp,end=' ')

# Create DFS algorithm, parameters are graph and vertex in it.
def DFS(graph,vertex):
    # Use stack.
    stack = []
    # Add first vertice to stack
    stack.append(vertex)
    looked = set()
    # Use set to save vertex which have been visited.
    looked.add(vertex)
    # Stack is not empty, then traversal.
    while len(stack)>0:
        # Get a node from bottom of stack, visit it and check its neighbors.
        temp = stack.pop()
        nodes = graph[temp]
        # Visit all the neighbors.
        for newnode in nodes:
            # Judge the node is visited or not.
            if newnode not in looked:
                # If not, add to stack and visited list.
                stack.append(newnode)
                looked.add(newnode)
        print(temp,end=' ')
# Operation
print("The result of unweighted graph with BFS algorithm is:\n ",end=" ")
BFS(graph,"A")
print("\n")
print("The result of unweighted graph with DFS algorithm is:\n ",end=" ")
DFS(graph,"A")
