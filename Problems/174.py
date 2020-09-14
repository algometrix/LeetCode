class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def dfs(i, j, val, result, space, _min, row, col):
            #print("{} {} : {} => {}".format("-" * space, i, j, val))
            if (i < 0 or i >= row) or (j < 0 or j >= col):
                return val
            if _min > val + dungeon[i][j]:
                _min = val + dungeon[i][j]
            
            if i == row - 1 and j == col - 1:
                #print(_min)
                if _min < val + dungeon[i][j] and _min <= 0:
                    result.append(_min)
                elif val + dungeon[i][j] <= 0:
                    result.append(val + dungeon[i][j])
            else:
                dfs(i+1,j,val + dungeon[i][j], result, space + 1, _min, row, col)
                dfs(i,j+1,val + dungeon[i][j], result, space + 1, _min, row, col)
            
        
        row, col = len(dungeon), len(dungeon[0])
        result = []
        dfs(0,0, 0, result, 0, float('inf'), row, col)
        if len(result) == 0:
            return 1
        return -1 * (max(result) - 1)
        