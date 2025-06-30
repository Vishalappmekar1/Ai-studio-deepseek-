def gpt4_ipv4(ip):
    parts = ip.split(".")
    if len(parts) != 4: return False
    return all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

def deepseek_ipv4(ip):
    try:
        nums = list(map(int, ip.split(".")))
        return len(nums) == 4 and all(0 <= n < 256 for n in nums)
    except:
        return False

def gpt4_roman(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(s):
        val = roman_map[char]
        total += val if val >= prev else -val
        prev = val
    return total

def deepseek_roman(s):
    lookup = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and lookup[s[i]] < lookup[s[i + 1]]:
            result -= lookup[s[i]]
        else:
            result += lookup[s[i]]
    return result

def gpt4_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def deepseek_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def gpt4_sort(lst):
    return sorted(lst)

def deepseek_sort(lst):
    return list(sorted(lst))
