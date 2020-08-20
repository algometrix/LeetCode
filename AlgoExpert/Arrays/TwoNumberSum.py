def twoNumberSum(array, targetSum):
    # Write your code here.
	sorted_array = sorted(array)
	i, j = 0, len(sorted_array) - 1
	while i!=j:
		_sum = sorted_array[i] + sorted_array[j]
		if _sum < targetSum:
			i+=1
		elif _sum > targetSum:
			j-=1
		elif _sum == targetSum:
			return [sorted_array[i], sorted_array[j]]
	
	return []
		