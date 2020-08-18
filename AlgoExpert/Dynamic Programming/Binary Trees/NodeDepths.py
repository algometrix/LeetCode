def nodeDepths(root):
    # Write your code here.
    queue = []
	queue.append((root, 0))
	total_depth = 0
	while len(queue) > 0:
		node, depth = queue.pop(0)
		if node is None:
			continue
		
		total_depth += depth
		queue.append((node.left, depth + 1))
		queue.append((node.right, depth + 1))
	
	print(total_depth)
	return total_depth
		


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
