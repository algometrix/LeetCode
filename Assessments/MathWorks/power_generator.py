import collections
def segment(x, space):
    window = collections.deque()
    out = []
    for i, n in enumerate(space):
        while window and space[window[-1]] > n:
            window.pop()
        window += i,
        if window[0] == i - x:
            window.popleft()
        if i >= x - 1:
            out += space[window[0]],
    return max(out)


if __name__ == "__main__":
    nums = [7,1,3]
    k = 2
    print(segment(k, nums))