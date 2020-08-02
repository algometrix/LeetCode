import copy
import pprint
class Solution:
    def isGoalState(self, node):
        goalState = [
            [1,2,3],
            [4,5,0]
        ]
        row = 2
        col = 3
        return node == goalState

    def findZero(self, node):
        for xIndex, row in enumerate(node):
            for yIndex, element in enumerate(row):
                if element == 0:
                    return xIndex, yIndex
    
    def getNeighors(self, node):
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        zeroX, zeroY = self.findZero(node)
        neighbors = []
        row = 2
        col = 3
        for direction in directions:
            newX, newY = zeroX + direction[0], zeroY + direction[1]
            if 0 <= newX < row and 0 <= newY < col:
                #print('{},{}'.format(newX, newY))
                newBoard = copy.deepcopy(node)
                newBoard[newX][newY],newBoard[zeroX][zeroY] = newBoard[zeroX][zeroY], newBoard[newX][newY]
                neighbors.append(newBoard)

        return neighbors
        
    
    def bfs(self, queue, state):
        visitedNodes = state
        
        if len(queue) == 0:
            return -1
        node, step = queue.pop(0)
        if self.isGoalState(node):
            return step
        
        visitedNodes.append(node)
        neighbors = self.getNeighors(node)
        #print('{} => {}'.format(node, neighbors))
        nextStep = step + 1
        for neighbor in neighbors:
            if neighbor not in visitedNodes:
                queue.append((neighbor, nextStep))
        
        return self.bfs(queue, visitedNodes)
    
    def slidingPuzzle(self, board):
        queue = []
        step = 0
        queue.append((board, step))
        state = []
        result = self.bfs(queue, state)
        return result
        


if __name__ == "__main__":
    
    board = [[1,2,3],[4,0,5]]
    #board = [[4,1,2],[5,0,3]]

    obj = Solution()
    #obj.slidingPuzzle(board)
    print(board)
    print(obj.slidingPuzzle(board))