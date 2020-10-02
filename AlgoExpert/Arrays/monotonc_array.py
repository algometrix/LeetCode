
def isMonotonic(array):
    # Write your code here.
    def numCheck(value_1, value_2, flag):
        if flag == 1:
            return value_1 <= value_2
        else:
            return value_1 >= value_2

    if len(array) == 1 or len(array) == 0:
        return True
    difference = array[-1] - array[0]
    if difference == 0:
        return True

    flag = difference / abs(difference)
    for i in range(1, len(array)):
        if not numCheck(array[i-1], array[i], flag):
            return False

    return True

if __name__ == "__main__":
    array = [1,2,3,4,5,6]
    result = isMonotonic(array)
    print('Result : {}'.format(result))
			
