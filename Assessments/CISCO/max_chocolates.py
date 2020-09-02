

def num_jar(jar_list):
    jar_length = len(jar_list)
    if jar_length == 0:
        return 0
    elif jar_length == 1:
        return jar_list[0]
    
    max_chocolates = jar_list[:]
    max_chocolates[1] = max(jar_list[0], jar_list[1])
    for i in range(2, jar_length):
        max_chocolates[i] = max(max_chocolates[i-1], max_chocolates[i-2] + jar_list[i])

    return max_chocolates[-1]

if __name__ == "__main__":
    print(num_jar([12, 45, 0, 87, 0, 46, 90]))