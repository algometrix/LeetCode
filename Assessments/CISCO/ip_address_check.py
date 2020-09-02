


def ip_address_check(ip_address):
    split_numbers = ip_address.split('.')
    split_length = len(split_numbers)
    if split_length != 4:
        return 'INVALID'
    
    for num in split_numbers:
        if 0 <= int(num) <= 255:
            pass
        else:
            return 'INVALID'

    return 'VALID'


if __name__ == "__main__":
    print(ip_address_check('10.102.34.48'))