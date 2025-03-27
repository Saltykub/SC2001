#include<bits/stdc++.h>
using namespace std;
int main(){   
   // initialize dp 
    int n = 3, C = 14;
    vector<int> w{0, 4, 6, 8}, p{0,7,6,9};
    vector<int> dp(C+1,0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= C; j++) {
          if (j - w[i] >= 0) dp[j] = max(dp[j], dp[j - w[i]] + p[i]);
        }
      }
    cout << dp[C];
}