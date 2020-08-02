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
                    #print(word, word_list[i], self.find_difference(word, word_list[i]))
                    count = self.find_difference(word, word_list[i])
                    if count == 1:
                        transitions[word].append(word_list[i])

        self.transitions = transitions
        for t in transitions:
            print(t, transitions[t])
        return transitions

    def isGoal(self, word):
        if word is self.goalState:
            return True
        else:
            return False
    
    def get_neighbors(self, word):
        return self.transitions[word]

    def bfs(self, beginWord, endWord):
        queue = []
        all_transisitons = []
        state = (beginWord, [beginWord,], 1 + self.find_difference(beginWord, endWord))
        queue.append(state)
        while(True):
            queue = sorted(queue, key=lambda x:x[2])
            if len(queue) == 0:
                return all_transisitons

            current_word, path, diff = queue.pop(0)
            if self.isGoal(current_word):
                if len(all_transisitons) != 0:
                    first_sol = all_transisitons[0]
                    if len(path) > len(first_sol):
                        return all_transisitons

                all_transisitons.append(path)
                return all_transisitons
            
            neighbors = self.get_neighbors(current_word)
            for neighbor in neighbors:
                if neighbor not in path:
                    new_path = []
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path, len(new_path) + self.find_difference(neighbor, endWord)))

    def findLadders(self, beginWord, endWord, wordList):
        complete_word_list = []
        beginWord = beginWord[0]
        endWord = endWord[0]
        complete_word_list = complete_word_list + wordList
        if beginWord not in complete_word_list:
            complete_word_list.append(beginWord)
        if endWord not in complete_word_list:
            return []
        
        self.goalState = endWord
        neighbor_list = self.create_neighbor_list(complete_word_list)
        #print(neighbor_list)
        #print(self.get_neighbors(beginWord))
        #all_transisitons = self.bfs(beginWord, endWord)
        #for t in all_transisitons:
        #    print(t)
        


if __name__ == "__main__":
    beginWord = "cet",
    endWord = "ism",
    wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
    sol = Solution()
    sol.findLadders(beginWord, endWord, wordList)
    