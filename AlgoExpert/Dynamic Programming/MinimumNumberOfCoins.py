def getNumber(n, demons):
    print(demons)
    pending_amount = n
    number_of_coins = []
    sorted_denoms = demons  # sorted(denoms, reverse=True)
    for _denom in sorted_denoms:
        if _denom <= pending_amount:
            _coins = pending_amount // _denom
            pending_amount = pending_amount % _denom
            number_of_coins.append(_coins)

    print(number_of_coins)
    if pending_amount == 0:
        return sum(number_of_coins)
    else:
        return float('inf')


def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    sorted_denoms = sorted(denoms, reverse=True)
    length = len(sorted_denoms)
    result = []
    for i in range(0, length):
        value = getNumber(n, sorted_denoms[i:])
        print(value)
        result.append(value)

    answer = min(result)
    if answer == float('inf'):
        return -1
    else:
        return answer


if __name__ == "__main__":
    _input = {"denoms": [1, 3, 4], "n": 10}
    minNumberOfCoinsForChange(_input['n'], _input['denoms'])
