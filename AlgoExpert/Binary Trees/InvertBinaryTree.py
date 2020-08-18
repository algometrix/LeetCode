def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
		return
	
	tmp = tree.left
	tree.left = tree.right
	tree.right = tmp
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
	return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
