
def validityCheck(value):
    if value == '0':
        return True
    elif value.startswith('0') or value == '':
        return False
    elif 0 <= int(value) <= 255:
        return True
    else:
        return False


def dfs(s, discovered_ip, prev_dot=-1, space=0, result=[]):
    if prev_dot == len(s) - 1 and space == 4:
        result.append(discovered_ip)
    elif space > 4:
        return
    for j in range(prev_dot + 2, prev_dot + 5):
        ip_section = s[prev_dot + 1:j]
        if validityCheck(ip_section):
            dfs(s, discovered_ip + '.' + ip_section if prev_dot != -
                1 else ip_section, prev_dot=j-1, space=space+1, result=result)


def restoreIpAddresses(s):
    result = []
    if len(s) > 12:
        return []
    dfs(s, '', result=result)
    return result


if __name__ == "__main__":
    s = '25525511135'
    result = restoreIpAddresses(s)
    print('Output : {}'.format(result))
