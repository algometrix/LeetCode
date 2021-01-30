


def trap(height):
    stack = [0]
    trapped_water = 0
    for index, h in enumerate(height + [0]):
        while stack and h >= stack[-1]:
            trapped_water += height[stack.pop()] * (index - stack[-1] - 1) - sum(height[stack[-1]:index])
        stack.append(index)

    print(trapped_water)
    return trapped_water

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = trap(height)
    print('Trapped Water : {}'.format(result))