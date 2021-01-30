def subarraySum(nums, k):
    count, cur, res = {0: 1}, 0, 0
    for v in nums:
        cur += v
        res += count.get(cur - k, 0)
        count[cur] = count.get(cur, 0) + 1
    return res

if __name__ == "__main__":
    nums = [1, 1, -1, 1]
    k = 2
    result = subarraySum(nums, k)
    print('Output : {}'.format(result))