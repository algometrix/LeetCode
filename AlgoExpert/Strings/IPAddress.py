def validIPAddresses(string:str):
    # Write your code here.
    def dfs(ip_addr, remaining_nums, num_dots, result):
        if num_dots > 4:
            return
        if len(remaining_nums) == 0 and num_dots == 4:
            result.append(ip_addr[:-1])
            return

        for i in range(1, len(remaining_nums)+1):
            if remaining_nums[:i] == '0' or (remaining_nums[0]!='0' and 0 <= int(remaining_nums[:i]) <= 255):
                if len(ip_addr) > 0:
                    dfs(ip_addr + 
                        remaining_nums[:i] + '.', remaining_nums[i:], num_dots + 1, result)
                else:
                    dfs(remaining_nums[:i] + '.', remaining_nums[i:], num_dots + 1, result)

    result = []
    dfs('', string, 0, result)
    print(result)
    return result


print(validIPAddresses('1921680'))
