amazon = ["a1","a2","a3","a4","a5","b1","b2","b3","b4","b5"]
amazon_final = []
index = amazon.index("b1")
for i in range(index): #0부터5미만 (0~4)
      amazon_final.append(amazon[i])
      amazon_final.append(amazon[index+i])

print(amazon_final)