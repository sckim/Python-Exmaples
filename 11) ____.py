def convert(n, base):
    T = "0123456789ABCDEF"  # 16진수까지 표현하기 위해
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
print (convert(233, 2))
print (convert(233, 8))
print (convert(233, 16))