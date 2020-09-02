'''
998 => 789
998 = 899

889

800 - 1

799
'''


def findDecrease(number):
    number_string = str(number)
    length = len(number_string) 
    if length == 0 or length == 1:
        return number
    
    for i in range(1, length):
        if number_string[i-1] >= number_string[i]:
            return i
    
    return i + 1
            
def monotoneIncreasingDigits(N):
    length = len(str(N))
    result = findDecrease(N)
    if length == result:
        return N
    else:
        decrease_number = str(N)[result - 1]
        decrease_index = None
        for index, digit in enumerate(str(N)):
            if decrease_number == digit:
                decrease_index = index + 1
                break
                
    normalize = int(str(N)[:decrease_index] + ('0' * (length-decrease_index)))
    return normalize - 1


result = 998
while findDecrease(result) != len('998'):
    result = monotoneIncreasingDigits(result)

print(result)        