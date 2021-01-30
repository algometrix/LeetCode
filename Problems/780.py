


def reachingPoints(sx, sy, tx, ty):
    bfs = [(sx, sy)]
    while len(bfs) > 0:
        x, y = bfs.pop(0)
        print(x, y)
        if x > tx or y > ty:
            continue
        elif x == tx and y == ty:
            return True
        else:
            bfs.append((x+y, y))
            bfs.append((x, x+y))
            
    
    return False

if __name__ == "__main__":
    '''
    35
    13
    455955547
    420098884
    '''
    sx, sy, tx, ty = 35, 13, 455955547, 420098884
    result = reachingPoints(sx, sy, tx, ty)
    print('Output : {}'.format(result))