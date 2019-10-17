class Solution:
    mark = [[0 for i in range(3)] for j in range(3)]
    nBoard = [[0 for i in range(3)] for j in range(3)]

    sample = [[1, 2, 1], [2, 0, 2], [1, 2, 1]]
    ans = 0
    
    def checkE(self):
      endrow = [1 for i in range(3)]
      endcol = [1 for i in range(3)]
      endd1, endd2 = 1, 1
      
      for i in range(3):
        for j in range(3):
          if self.mark[i][0] == 0 or self.mark[i][0] != self.mark[i][j]:
            endrow[i] = 0
          if self.mark[0][j] == 0 or self.mark[0][j] != self.mark[i][j]:
            endcol[j] = 0
      if 1 in endrow or 1 in endcol:
        return 1
      
      for i in range(3):
        if self.mark[0][0] == 0 or self.mark[0][0] != self.mark[i][i]:
          endd1 = 0
        if self.mark[0][2] == 0 or self.mark[0][2] != self.mark[i][2-i]:
          endd2 = 0
      if endd1 == 1 or endd2 == 1:
        return 1
      return 0
      
      
    def checkS(self):
      checkState = 1
      for i in range(3):
        for j in range(3):
          if self.mark[i][j] != self.nBoard[i][j]:
            checkState = 0
            break
      return checkState
      
          
    def search(self, x, y, p):
      # print(p)
      # if self.mark == self.sample:
      #   print('clgt')
      # print(self.mark)
      if self.ans == 1:
        return

      if self.checkE():
        if self.checkS():
          self.ans = 1
          return
        else:
          return
      else: 
        if self.checkS():
          self.ans = 1
          return
      for i in range(3):
        for j in range(3):
          if self.mark[i][j] == 0:
            self.mark[i][j] = 3 - p
            self.search(i, j, 3 - p) 
            self.mark[i][j] = 0
    
    def validTicTacToe(self, board) -> bool:
      for i in range(3):
        for j in range(3):
          if board[i][j] == "X":
            self.nBoard[i][j] = 1
          elif board[i][j] == "O":
            self.nBoard[i][j] = 2
          else:
            self.nBoard[i][j] = 0
      # print(self.nBoard)
      for i in range(3):
        for j in range(3):
          self.mark[i][j] = 1
          self.search(i, j, 1)
          self.mark[i][j] = 0
      if self.ans == 1:
        return True
      else:
        return False

g = Solution()

inp = ["XOX","O O","XOX"]

print(g.validTicTacToe(inp))