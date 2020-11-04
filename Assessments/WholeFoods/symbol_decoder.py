


def symbol_decoder(nums, mapping):
    def dfs(digits, array):
        if len(digits) == 0:
            print(array)
            return
        for character in mapping[digits[0]]:
            dfs(digits[1:], array + character)
    
    dfs(str(nums), '')

if __name__ == "__main__":
    mapping = {
        '1':['a','b','c'],
        '2':['d','e','f'],
        '3':['g','h','i'],
    }
    nums = 12
    symbol_decoder(nums, mapping)