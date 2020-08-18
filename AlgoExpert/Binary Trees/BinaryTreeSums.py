# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSum(root, value, sum_list):
	if root is None or value is None:
		return 0
	
	if root.left is None and root.right is None:
		return sum_list.append(value + root.value)
	
	branchSum(root.left, value + root.value, sum_list)
	branchSum(root.right, value + root.value, sum_list)
		
def branchSums(root):
    # Write your code here.
	sum_list = []
	branchSum(root, 0, sum_list)
	print(sum_list)
	return sum_list
	
