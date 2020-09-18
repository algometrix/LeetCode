


def jump(nums):
    length = len(nums)
    if length == 1:
        return 0
    print('Number of stops : {}'.format(length))
    array = [float('inf')] * length
    array[0] = 0
    array[1] = 1
    for i in range(0, length):
        print('Current Stop : {}'.format(i))
        if i > 1 and nums[i] < nums[i-1] and array[i] != float('inf'):
            continue
        for j in range(i + 1, min(i + nums[i] + 1, length)):
            array[j] = min(array[j], 1 + array[i])
            
    return array[-1]

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    result = jump(nums)
    print('Minimum number of jumps : {}'.format(result))