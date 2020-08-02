from sys import stdin
from collections import Counter
def calc(val, cl, result):
    if val == 0:
        return result
    if val < cl[-1]:
        return result.append(-1)
    else:
        for index, c in enumerate(cl):
            if val >= c:
                calc(val - c, cl, result)
                result.append(c)
                break

    return result


def answer():
    line = stdin.readline()
    b, w, n = [ int(val) for val in line.split(' ') ]
    if b < w:
        print('Not enough balance')

    currrency_list = []
    for i in range(n):
        line = stdin.readline()
        currrency_list.append(int(line))

    currrency_list.sort(reverse=True)  
    result = []
    #print(currrency_list)  
    r = calc(w, currrency_list, result)
    #print(r)
    if -1 in r:
        print('Cannot put into packets')
    else:
        counter = Counter(r)
        currrency_list.sort()  
        for c in currrency_list:
            print('{}:{} '.format(counter[c],c)),

        print(b - w)




if __name__ == "__main__":
    answer()