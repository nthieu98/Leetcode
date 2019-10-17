# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  d = [0 for i in range(100000)]
  ans = 1
  
  def DFS(self, u, v, f):
    if u == None:
      return
    if self.d[f] == -1:
      self.d[f] = v
    else:
      self.d[f] = min(self.d[f], v)
    self.ans = max(self.ans, v - self.d[f] + 1)
    if u.left != None:
      self.DFS(u.left, v * 2, f + 1)
    if u.right != None:
      self.DFS(u.right, v * 2 + 1, f + 1)
    
  def widthOfBinaryTree(self, root: TreeNode) -> int:
    for i in range(100000):
      self.d[i] = -1
    self.DFS(root, 1, 0)
    return self.ans