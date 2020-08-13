
IGNORE_VALUE = None

def swapValues(nums, i, j):
    if nums[i] == nums[j]:
        nums[j] = None
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
    if nums[j] != IGNORE_VALUE and nums[j] - 1 != j:
        swapValues(nums, j, nums[j] - 1)
    elif nums[i] != IGNORE_VALUE and nums[i] - 1 != i:
        swapValues(nums, i, nums[i] - 1)
    
def firstMissingPositive(nums):
    array_length = len(nums)
    for i in range(array_length):
        if nums[i] > array_length or nums[i] <= 0:
            nums[i] = IGNORE_VALUE

    for i in range(array_length):
        if nums[i] != IGNORE_VALUE and nums[i] != i + 1:
            swapValues(nums, i, nums[i] - 1)
    
    
    for i in range(array_length):
        if nums[i] == IGNORE_VALUE:
            return i + 1

    return array_length

if __name__ == "__main__":
    nums = [1,1]
    print('Input\t:\t{}'.format(nums))
    result = firstMissingPositive(nums)
    print('Result\t:\t{}'.format(result))