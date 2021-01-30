

def partition(s):
    def dfs(remaining_characters, path, result):
        if len(remaining_characters) == 0:
            result.append(path)
        else:
            for i in range(1, len(remaining_characters) + 1):
                if remaining_characters[:i] == reversed(remaining_characters[:i]):
                    dfs(remaining_characters[i:], path + [ remaining_characters[:i] ], result)
    result = []
    dfs(s, [], result)
    return result

if __name__ == "__main__":
    _input =  "aab" 
    result = partition(_input)
    print("Result : {}".format(result))