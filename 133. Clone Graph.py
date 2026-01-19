# class Solution:
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         old_to_new = {}

#         def dfs(curr):
#             if not curr:
#                 return None
#             if curr in old_to_new:   # already cloned
#                 return old_to_new[curr]

#             copy = Node(curr.val)          # 1. clone node itself
#             old_to_new[curr] = copy        # 2. save in map

#             for nei in curr.neighbors:     # 3. clone neighbors
#                 copy.neighbors.append(dfs(nei))
            
#             return copy

#         return dfs(node)
    
# just practicing the same code 

def clonegraph(node):
    new= {}

    def dfs(node):
        if not node:
            return None
        if node in new:
            return new[node]
        newnode = Node(node.val)
        new[node] =  newnode
        for i in node.neighbours:
            newnode.neighbours.append(dfs(i))
        return newnode
    return dfs(node)





def dd(node):
    new = {}

    def dfs(node):
        if not node : return None
        if node in new: return new[node]
        newNode = Node(node.val)
        new[node] = newNode
        for i in node.neighbours:
            newNode.neighbours.append(dfs(i))
        return newNode
    return dfs(node)