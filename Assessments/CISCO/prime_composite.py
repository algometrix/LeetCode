



def prime_check(number):
    import math
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    
    return True

def prime_composite(number_list):
    result = ''
    for num in number_list:
        if prime_check(num):
            result += 'Prime '
        else:
            result += 'Composite '
    
    return result[:-1]

if __name__ == "__main__":
    num_list = [10, 11, 12, 41, 21, 2]
    print(prime_composite(num_list))