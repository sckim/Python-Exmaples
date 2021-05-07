s = 'aabcccaaaaas'

result = s[0]
count  = 0

for st in s:
    if st == result[-1]:
        count += 1
    else:
        result += str(count) + st
        count = 1
result += str(count)

print(result)