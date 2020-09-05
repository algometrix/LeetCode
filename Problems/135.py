
def calc_candy(candies, ratings, index):
    print(candies)
    if candies[index] == 0:
        return 1
    if ratings[index] == 0:
        candies[index] = 1
        calc_candy(candies, ratings, index + 1)
        calc_candy(candies, ratings, index - 1)
    elif ratings[index] == -1:
        return -1
    else:
        candies[index] = 0
        if ratings[index - 1] >= ratings[index] and ratings[index] <= ratings[index + 1]:
            candies[index] = 1
        else:
            candies[index] = max(calc_candy(candies, ratings, index - 1), calc_candy(candies, ratings, index + 1)) + 1
        return candies[index]

def candy(ratings):
    ratings = [-1] + ratings + [-1]
    candies = [-1] * (len(ratings) + 2)
    calc_candy(candies, ratings, 1)
    return candies

if __name__ == "__main__":
    _input = [1,0,2,3,0,2]
    result = candy(_input)
    print('Number of Candies : {}'.format(result))