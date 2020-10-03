
import pprint
def generateSubset(array):
    temp = []
    result = []
    def search(k):
        if k == len(array):
            result.append([array[index] for index in temp])
        else:
            temp.append(k)
            search(k+1)
            temp.pop()
            search(k+1)
    
    search(0)
    return result

if __name__ == "__main__":
    array = [2,5,9]
    result = generateSubset(array)
    print('All possible permuations')
    pprint.pprint(result)