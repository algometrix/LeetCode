def findClosestValueInBst(tree, target):
    # Write your code here.
	def binarySearch(node, val, nearestVal):
		if node is None:
			return float('inf')
		else:
			if val < node.value:
				nearestVal = binarySearch(node.left, val, nearestVal)
			elif val > node.value:
				nearestVal = binarySearch(node.right, val, nearestVal)
			
			if abs(node.value - val) < abs(nearestVal - val):
				nearestVal = node.value
			
			return nearestVal
	
	result = binarySearch(tree, target, float('inf'))
	return result