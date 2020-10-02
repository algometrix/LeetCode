def subarraySort(array):
    # Write your code here.
    maxNum = float('-inf')
	length = len(array)
	maxIndex = -1
	highIndex = -1
	lowIndex = -1
	minSubArray = float('inf')
	for i in range(length):
		if maxNum < array[i]:
			maxNum = array[i]
			maxIndex = i
		if array[i] < maxNum:
			highIndex = i
			minSubArray = min(array[i], minSubArray)
	
	if highIndex == -1:
		return [-1,-1]
			
	for index, value in enumerate(array):
		if minSubArray < value:
			lowIndex = index
			break
	
	return [lowIndex, highIndex]
