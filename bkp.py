class Solution:
    goalState = None
    transitions = None
    def find_difference(self, firstWord, endWord):
        length = len(firstWord)
        count = 0
        for i in range(length):
            if firstWord[i] != endWord[i]:
                count = count + 1

        return count
    
    def create_neighbor_list(self, word_list):
        transitions = {}
        length = len(word_list)
        #print(word_list)
        for index, word in enumerate(word_list):
            transitions[word] = []
            for i in range(length):
                if index != i:
                    count = self.find_difference(word, word_list[i])
                    if count == 1:
                        transitions[word].append(word_list[i])

        self.transitions = transitions
        return transitions

    def isGoal(self, word):
        if word == self.goalState:
            return True
        else:
            return False
    
    def get_neighbors(self, word):
        #print(word, self.transitions[word])
        return self.transitions[word]

    def bfs(self, beginWord, endWord):
        queue = []
        all_transisitons = []
        state = (beginWord, [beginWord,], self.find_difference(beginWord, endWord))
        queue.append(state)
        while(True):
            if len(queue) == 0:
                return all_transisitons

            current_word, path = queue.pop(0)
            if self.isGoal(current_word):
                if len(all_transisitons) != 0:
                    first_sol = all_transisitons[0]
                    if len(path) > len(first_sol):
                        return all_transisitons
                        
                all_transisitons.append(path)
            
            neighbors = self.get_neighbors(current_word)
            for neighbor in neighbors:
                if neighbor not in path:
                    new_path = []
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path, self.find_difference(neighbor, endWord)))

    def findLadders(self, beginWord, endWord, wordList):
        complete_word_list = []
        complete_word_list = complete_word_list + wordList
        if beginWord not in complete_word_list:
            complete_word_list.append(beginWord)
        if endWord not in complete_word_list:
            return []
        
        self.goalState = endWord
        neighbor_list = self.create_neighbor_list(complete_word_list)
        all_transisitons = self.bfs(beginWord, endWord)
        return all_transisitons 
    

    