def intersectionSizeTwo(intervals):
    length = len(intervals)
    if length == 0:
        return 0
    
    result = 2
    intervals = sorted(intervals, key=lambda x: x[1])
    _set = [intervals[0][1] - 1, intervals[0][1]]
    for start, end in intervals[1:]:
        if start > _set[1]:
            result += 2
            _set = [end - 1, end]
        elif _set[0] < start:
            result += 1
            _set = [_set[1], end]

    return result
    

if __name__ == "__main__":
    intervals = [[1,3],[1,4],[2,5],[3,5]]
    print(intersectionSizeTwo(intervals))