class Solution:
    def superEggDrop(self, K, N):  # method 1
        dp = [ [0] * (K + 1) for i in range(N + 1) ]
        #print(dp)
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N:
                print_matrix(dp, "Moves/Eggs")
                return m

        return 0

    def superEggDrop1(self, K, N):  # 2 + space optimization method
        dp = [0] * (K + 1)
        m = 0
        while dp[K] < N:
            for k in range(K, 0, -1):
                dp[k] = dp[k - 1] + dp[k] + 1
            m += 1
        return m

def print_matrix(matrix, label):
    row, col = len(matrix), len(matrix[0])
    print(label)
    print('')
    print('\t', end='')
    for i in range(col):
        print(i, end='\t')
    print('\n')
    for i in range(row):
        print(i, end='\t')
        for j in range(col):
            print(matrix[i][j], end='\t')
        print('\n')

if __name__ == '__main__':
    solu = Solution()
    N, K = 10, 10
    '''
    dp = [ [0] * (K + 1) for i in range(N + 1) ]
    for j in range(0, N + 1):
        for i in range(0, K + 1):
            dp[j][i] = solu.superEggDrop(j, i)
    '''

    print(solu.superEggDrop(2, 6))
    #print_matrix(dp)