def hasSingleCycle(array):
    # Write your code here.
	#print("Input Array : ", array)
	length = len(array)
	index = 0
	for i in range(length + 1):
		if array[index] == 0:
			return False
		jump = jumpIndex(index, array[index], length)
		print("Jump : ", jump)
		if i != 0:
			array[index] = 0
		index = jump
		
	#print("Output Array : ", array)
	return sum(array) == 0
		

def jumpIndex(currentIndex, jumpValue, length):
	#print('Current Index : ', currentIndex)
	#print('jumpValue : ', jumpValue)
	jumpValue = jumpValue % length
	jumpIndex = currentIndex + jumpValue
	if jumpIndex >= length:
		jumpIndex = jumpIndex % length
	elif jumpIndex < 0:
		jumpIndex += length
	
	return jumpIndex
		
		
