class Solution:
    p = [0 for i in range(100)]
    ans = []
    l = []
    target = 0
    def Get(self, x, remain):
      
      if x == len(self.l):
        if remain == 0:
          # print(p)
          res = []
          for i in range(len(self.l)):
            for j in range(self.p[i]):
              res.append(self.l[i])
          self.ans.append(res)
        
        return
      print(x, self.p[x], self.l[x], remain)
      k = remain // self.l[x]
      for i in range(k + 1):
        self.p[x] = i
        self.Get(x + 1, remain - self.l[x] * i)
    def combinationSum(self, candidates, target: int):
      self.target = target
      candidates.sort()
      self.l = candidates
      print(self.l)
      self.Get(0, target)
      return self.ans
      
Z = Solution()
nums = [2, 3, 5]
target = 8
print(Z.combinationSum(nums, target))