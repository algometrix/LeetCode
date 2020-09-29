def candy(ratings):
    ratings = [float('inf')] + ratings + [float('inf')]
    length = len(ratings)
    candies = [1] * length
    for i in range(1, length-1):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    
    for i in range(length-2, 0, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i+1] + 1, candies[i])
    
    return sum(candies[1:-1])

if __name__ == "__main__":
    ratings = [29,51,87,87,72,12]
    result = candy(ratings)
    print('Total number of candies required : {}'.format(result))