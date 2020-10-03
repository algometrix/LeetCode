

def gaming(array, k):
    counter = {}
    rankList = {}
    _rank = 1
    for value in array:
        if value in counter:
            counter[value] += 1
        else:
            counter[value] = 1 
    
    for key in sorted(counter.keys(), reverse=True):
        rankList[key] = _rank
        _rank += counter[key]
        
    return len([ val for val in array if rankList[val] <= k ])
    


if __name__ == "__main__":
    array = [2,2,3,4,5]
    array = [0,0,0,0]
    #array = [100, 50, 50, 25]
    #array = []
    k = 0
    result = gaming(array, k)
    print('Output : {}'.format(result))