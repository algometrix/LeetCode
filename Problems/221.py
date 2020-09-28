
import pprint

def maximalSquare(matrix):
    if not matrix:
        return 0
    row, col = len(matrix), len(matrix[0])
    dp = [ [ 0 for i in range(col+1) ] for j in range(row+1)]
    dim = 0
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                dim = max(dp[i][j], dim)
    
    print(dim)
    return dim ** 2


if __name__ == "__main__":
    matrix = [["1","1","1","1","1"],["1","1","1","1","1"],["0","0","0","0","0"],["1","1","1","1","1"],["1","1","1","1","1"]]
    matrix = [["1"]]
    matrix = [["1","0","1","1","1"],["1","1","1","0","1"],["1","1","1","1","1"],["1","1","0","1","1"]]
    pprint.pprint(matrix)
    print('\n\n')
    result = maximalSquare(matrix)
    print('Output : {}'.format(result))