def longestPeak(array):
    # Write your code here.
    array = [float('inf')] + array + [float('inf')]
    length = len(array)
    maxPeak = 0
    for i in range(length - 1):
        if array[i-1] < array[i] > array[i+1]:
            left, right = i-1, i+1
            while array[left-1] < array[left] and left > 1:
                left -= 1
            while array[right] > array[right+1] and right < length - 1:
                right += 1
            
            #print(array[i], left, right, right - left)
            maxPeak = max(maxPeak, right - left + 1)

    return maxPeak

if __name__ == "__main__":
    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    result = longestPeak(array)
    print('Result : {}'.format(result))
