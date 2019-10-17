
strs = ["abc", "ped"]
gen = [[] for i in range(len(strs))]
for id in range(len(strs)):
  k = len(strs[id])
  for i in range(0, (1 << k)):
    newStr = ""
    # print(i)
    for j in range(0, k):
      # print (1<<j)
      if i & (1 << j):
        print(i, j, strs[id][j])
        newStr = newStr + strs[id][j]
    gen[id].append(newStr)
ans = 0
print(gen)