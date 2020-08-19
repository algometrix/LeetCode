# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    # Write your code here.
    flattened_tree = [] 
	inorderTraversal(root, flattened_tree)
	numberOfNodes = len(flattened_tree)
	if numberOfNodes > 0:
		flattened_tree[0].left = None
		flattened_tree[-1].right = None
	
	for i in range(0, numberOfNodes-1):
		flattened_tree[i].right = flattened_tree[i+1]
		flattened_tree[i+1].left = flattened_tree[i]
	
	return flattened_tree[0]

def inorderTraversal(root, flattened_tree):
	if root is None:
		return
	
	inorderTraversal(root.left, flattened_tree)
	flattened_tree.append(root)
	inorderTraversal(root.right, flattened_tree)
