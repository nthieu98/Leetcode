def binSearch(arr, x):
  L = 0
  R = len(arr)
  while R - L > 1:
    M = (R + L) >> 1
    if arr[M] > x:
      R = M
    else:
      L = M
  return L

def reversePairs(nums):
  arr = nums.copy()
  for i in nums:
    arr.append(i * 2 + 1)
  arr.sort()
  arr.append(arr[len(arr)-1] + 1)
  BIT = [0 for i in range(len(nums)*3)]
  ans = 0
  print(arr)
  print(nums)
  for i in range(len(nums)):
    # print(i)
    k = 0
    pos = binSearch(arr, 2 * nums[i] + 1) + 1
    print('get', nums[i] * 2 + 1, pos)
    while pos <= len(nums) * 2:
      k += BIT[pos]
      pos += (pos & (-pos))
    ans += k
    pos = binSearch(arr, nums[i]) + 1
    print('up', nums[i], pos)
    while pos:
      BIT[pos] += 1
      pos -= (pos & (-pos))
  print('ans', ans)

inp = [1,3,2,3,1]

reversePairs(inp)
