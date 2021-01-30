def maximizeSweetness(sweetness, K):
    def number_of_pieces(target):
        count = 0
        minSweet = 0
        for sweet in sweetness:
            minSweet += sweet
            if minSweet >= target:
                count +=1
                minSweet = 0
        
        return count
    
    low, high = min(sweetness), sum(sweetness)
    while low < high:
        mid = (low + high)//2
        r = number_of_pieces(mid)
        if r < K+1:
            high = mid - 1
        elif r > K + 1:
            low = mid
        elif r == K+1:
            return mid
        
        
    return low

if __name__ == '__main__':
    sweetness = [1,2,3,4,5,6,7,8,9]
    K = 5
    result = maximizeSweetness(sweetness, K)
    print('Result : {}'.format((result)))