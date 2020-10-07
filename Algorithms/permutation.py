

def search(n, perm = [], choosen = [], result = []):
    if len(perm) == n:
        result.append(perm[::])
    else:
        for i in range(n):
            if choosen[i]:
                continue
            choosen[i] = True
            perm.append(i)
            search(n, perm=perm, choosen=choosen, result=result)
            choosen[i] = False
            perm.pop()
    
    return result


if __name__ == "__main__":
    perm = []
    n = 4
    result = []
    search(n, perm=[],choosen=[False]*n, result=result)
    print('Output : {}'.format(result))