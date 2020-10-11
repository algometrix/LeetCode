import random

def lcm(a, b):
    return int(a*b/(gcd(a, b)))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == "__main__":
    _range = 10
    for _ in range(_range):
        a, b = random.randint(0, 100), random.randint(0, 100) 
        print('LCM({},{}) = {}'.format(a, b, lcm(a, b)))
        print('GCD({},{}) = {}\n'.format(a, b, gcd(a, b)))