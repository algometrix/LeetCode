
import heapq
def minMeetingRooms(intervals):
    intervals.sort(key=lambda x:x[0])
    heap = []  # stores the end time of intervals
    for i in intervals:
        if heap and i[0] >= heap[0]: 
            # means two intervals can use the same room
            heapq.heapreplace(heap, i[1])
        else:
            # a new room is allocated
            heapq.heappush(heap, i[1])
    return len(heap)

if __name__ == "__main__":
    intervals = [[2,11],[6,16],[11,16]]
    intervals = [[0, 30],[5, 10],[15, 20]]
    result = minMeetingRooms(intervals)
    print('Output : {}'.format(result))