class Solution:
    def check(self, p, x):
      k = p
      while k:
        k -= 1
        if k % x != 0:
          return False
        k /= x
      return True
    
    def smallestGoodBase(self, n: str) -> str:
      p = int(n)
      for i in range(2, p):
        if i * i * i * i> p:
          break
        if self.check(p, i):
          return str(i)
      L = 2
      R = 1000000
      while R - L > 1:
        M = (R + L) // 2
        if M * M * M + M * M + M + 1 <= p:
          L = M
        else:
          R = M
      if L * L * L + L * L + L + 1 == p:
        return str(L)
      k = int(math.sqrt(p - 1))
      if k < 2:
        return str(p - 1)
      if k * (k + 1) == p - 1:
        return str(k)
      return str(p - 1)