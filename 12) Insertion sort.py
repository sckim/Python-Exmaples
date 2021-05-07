t0 = [5,2,4,6,1,3]
for i in range( 1, len(t0) ):  # 1이상6미만 (range(a,b)):a이상b미만
       for j in range( 0,len(t0)-1 ):  #0~4까지
           while t0[i] < t0[j]:
               t0[i], t0[j] = t0[j], t0[i]

print(t0)