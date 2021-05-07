divisor = lambda n: ((i, n//i) for i in range(1,int(n**0.5)+1) if not n%i) #튜플
for i in divisor(int(input('n: '))):
        if i[0]==i[1]: print(i)
        else: print(i, (i[1],i[0]),sep='\n')

