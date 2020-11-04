

def kandane(array):
    total = maxTotal = array[0]
    for i in range(1, len(array)):
        total = max(array[i], array[i] + total)
        maxTotal = max(maxTotal, total)
    
    return maxTotal


if __name__ == "__main__":
    array = [1, 2, 4, -10, 8]
    result = kandane(array)
    print(result)