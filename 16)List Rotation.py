data = input('회전수와 문자열을 입력하세요. : ').split()
rn = int(data.pop(0)) % len(data)
print(' '.join([(data*3)[len(data) + i - rn] for i in range(len(data))]))