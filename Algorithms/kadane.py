

def kadanesAlgorithm(array):
    total = [array[0]]
    for i in range(1,len(array)):
        total.append(max(total[-1] + array[i], array[i]))

    return max(total)


if __name__ == "__main__":
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    result = kadanesAlgorithm(array)
    print('Max Sum Subarray : {}'.format(result))
	
	
