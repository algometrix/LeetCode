# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def backtrack(node, visited):
	while node != None:
		if node.name not in visited.keys():
			visited[node.name] = 1
		else:
			return node
		
		node = node.ancestor
		
		
	
		
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    visited = {}
	result = backtrack(descendantOne, visited)
	result = backtrack(descendantTwo, visited)
	return result
