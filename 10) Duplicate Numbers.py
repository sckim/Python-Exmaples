n = [''.join(sorted(x)) for x in input().split()]
for x in n:
        print("true" if x == "0123456789" else "false")
