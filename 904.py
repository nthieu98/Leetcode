class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        numberType = 0
        mark = [0 for i in range(len(tree))]
        cur = 0
        ans = 0
        for i in range(len(tree)):
          if mark[tree[i]] == 0:
            mark[tree[i]] += 1
            numberType += 1
          else:
            mark[tree[i]] += 1
          while(numberType > 2):
            mark[tree[cur]] -= 1
            if mark[tree[cur]] == 0:
              numberType -= 1
            cur += 1
          ans = max(ans, i - cur + 1)
        return ans