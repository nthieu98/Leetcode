
def isPalindrome(x):
  k = str(x)
  for i in range(len(k) // 2):
    if k[i] != k[len(k) - 1 - i]:
      return 0
  return 1
  
def primePalindrome(N: int) -> int:
  mark = [0 for i in range(2 * N)]
  
  # return self.isPalindrome("101")
  
  for i in range(2, 2 * N):
    if mark[i] == 0:
      print(i)
      if i >= N and isPalindrome(i):
        return i
      for j in range(i + i, 2 * N, i):
        mark[j] = 1

primePalindrome(100)
      
      
        