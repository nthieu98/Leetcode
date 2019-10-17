#include <bits/stdc++.h>

using namespace std;

int reversePairs(vector<int>& nums) {
  vector<int> a;
  a.push_back(-INT_MIN);
  for(int i = 0; i < nums.size(); i++)  {
    a.push_back(nums[i]);
    if(nums[i] >= 0) a.push_back(nums[i] * 2 + 1);
    else a.push_back(nums[i] * 2 - 1);
  }
  sort(a.begin(), a.end());
  int n = nums.size();
  int M = 2*n + 100;
  int T[M];
  memset(T, 0, sizeof(T));
  int ans = 0;
  int pos, k;
  for(int i = 0; i < nums.size(); i++) {
    if (nums[i] >= 0) {
      k = nums[i] * 2 + 1;
    }
    else {
      k = nums[i] * 2 - 1;
    }
    pos = lower_bound(a.begin(), a.end(), k) - a.begin();
    for(; pos < M; pos += (pos & (-pos))) {
      ans += T[pos];
    }
    pos = lower_bound(a.begin(), a.end(), nums[i]) - a.begin();
    for(; pos; pos -= (pos & (-pos))) {
      T[pos] ++;
    }

  }
  return ans;
}

int main()
{
    vector<int> a;
    a.push_back(-5);
    a.push_back(-5);
    cout << reversePairs(a);
    return 0;
}
