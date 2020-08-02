def findMedianSortedArrays(nums1, nums2):
    lengthX = len(nums1)
    lengthY = len(nums2)
    start = 0
    end = lengthX - 1
    leftX, leftY = 0, 0
    rightX, rightY = 0, 0
    while True:
        partitionX = int((start + end) / 2)
        partitionY =  int(lengthY - partitionX)
        if partitionX == 0:
            leftX = -float('inf')
        else:
            leftX = nums1[partitionX - 1]

        leftY = nums2[partitionY - 1] if partitionY > 0 else -float('inf')
        rightX = nums1[partitionX] if partitionX <lengthX else float('inf')
        if partitionY == lengthY:
            rightY = float('inf')
        else:
            rightY = nums2[partitionY]
        
        if leftX <= rightY and leftY <= rightX:
            if (lengthX + lengthY) % 2 == 0:
                return (max(leftX, leftY) + min(rightX, rightY)) / 2
            else:
                return max(leftX, leftY)
        else:
            if leftX > rightY:
                end = partitionX
            else:
                start = partitionX + 1


if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3, 4]
    result = findMedianSortedArrays(nums1, nums2)
    print('Median : {}'.format(result))