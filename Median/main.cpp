#include <iostream>

using namespace std;

int n, m, x;
vector<int> a, b;

int main()
{
  cin >> n;
  for(int i = 1; i <= n; i++) {
    cin >> x;
    a.push_back(x);
  }
  cin >> m;
  for(int i = 1; i <= m; i++) {
    cin >> x;
    b.push_back(x);
  }

  while(1) {
    int L1 = 0;
    int R1 = n;
    int L2 = 0;
    int R2 = m;
    int M1 = (L1 + R1) / 2;
    int M2 = (L2 + R2) / 2;
    if ()
  }
  return 0;
}
