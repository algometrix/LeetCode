def moveElementToEnd(array, toMove):
    # Write your code here.
    length = len(array)
    i, j = 0, length - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1

        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]

        i += 1
    return array


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 2, 2, 2, 2, ]
    print(array)
    toMove = 2
    result = moveElementToEnd(array, toMove)
    print(result)
