def validateStackSequences(pushed, popped):
    stack = [-1]
    stack_tracker = 0
    for popped_item in popped:
        if popped_item not in stack:
            while stack[-1] != popped_item:
                stack.append(pushed[stack_tracker])
                stack_tracker += 1
        
        if popped_item in stack:
            _pop = stack.pop()
            if popped_item != _pop:
                return False

    return True

if __name__ == "__main__":
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    result = validateStackSequences(pushed, popped)
    print('Valid Stack Operations : {}'.format(result))