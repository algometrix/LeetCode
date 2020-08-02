
def largestRectangleArea(heights):
    stack, max_area = [-1], 0
    for i, h in enumerate(heights + [-1]):
        while stack and stack[-1] >= 0 and h <= heights[stack[-1]]:
            max_area = max(heights[stack.pop()] * (i - stack[-1] - 1), max_area)
        stack.append(i)
    return max_area

if __name__ == "__main__":
    r = largestRectangleArea([2,1,5,6,2,3])
    print(r)