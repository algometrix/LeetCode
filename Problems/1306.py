class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        goal_index = [ index for index, val in enumerate(arr) if val == 0 ]
        goal_index = set(goal_index)
        visited = set([])
        bfs = [start]
        for val in bfs:
            if val in goal_index:
                return True
            else:
                visited.add(val)
                prev_step, next_step = val - arr[val], val + arr[val]
                if prev_step >= 0 and prev_step not in visited:
                    bfs.append(prev_step)
                if next_step < len(arr) and next_step not in visited:
                    bfs.append(next_step)
        
        return False