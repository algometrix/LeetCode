'''
12324 => 12321
10000 => 9999
9999 => 10001
7 => 6
10001 => 9999
1221 => 1111
'''

from math import log10, ceil

def nearestPalindromic(n):
    parsed_int = int(n) 
    number_length = len(n)
    if number_length == 1:
        return str(parsed_int - 1)
    elif log10(parsed_int).is_integer() or log10(parsed_int - 1).is_integer():
        return '9' * (number_length - 1)
    elif log10(parsed_int + 1).is_integer():
        return str(parsed_int + 2)
    
    number_parts = [ digit for digit in n ]
    reflection_point = ceil(number_length / 2)
    number_reflection = None
    print('{} => Reflection Point : {}'.format(n, reflection_point))
    if number_length % 2 == 0:
        number_reflection = number_parts[:reflection_point] + number_parts[reflection_point - 1::-1]
    else:
        number_reflection = number_parts[:reflection_point] + number_parts[max(reflection_point - 2, 0)::-1]

    print('Reflection : {}'.format(number_reflection))
    upper_palindrome = number_reflection[::]
    lower_palindrome = number_reflection[::]
    if number_length % 2 == 0:
        upper_palindrome[reflection_point - 1] = str(min(int(upper_palindrome[reflection_point - 1]) + 1, 9))
        lower_palindrome[reflection_point - 1] = str(max(int(lower_palindrome[reflection_point - 1]) - 1, 0))

        upper_palindrome[reflection_point] = str(min(int(upper_palindrome[reflection_point]) + 1, 9))
        lower_palindrome[reflection_point] = str(max(int(lower_palindrome[reflection_point]) - 1, 0))
    else:
        upper_palindrome[reflection_point - 1] = str(min(int(upper_palindrome[reflection_point - 1]) + 1, 9))
        lower_palindrome[reflection_point - 1] = str(max(int(lower_palindrome[reflection_point - 1]) - 1, 0))

        

    print(number_reflection)
    print(lower_palindrome)
    print(upper_palindrome)

    number_reflection = int(''.join(number_reflection))
    upper_palindrome = int(''.join(upper_palindrome))
    lower_palindrome = int(''.join(lower_palindrome))
    candidates = [number_reflection, upper_palindrome, lower_palindrome]
    candidates = sorted(candidates)
    distance = [float('inf'), float('inf')]
    for candidate in candidates:
        diff = abs(candidate - parsed_int)
        if diff < distance[0] and diff != 0:
            distance = [diff, candidate]

    return str(distance[1])

if __name__ == "__main__":
    input_list = ["11911", "88", "11011", '230', '12324', '10000', '9999', '7', '10001', '1221', '12']
    for _input in input_list:
        print('{} => {}\n'.format(_input, nearestPalindromic(_input)))