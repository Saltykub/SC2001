#include<bits/stdc++.h>
#define ll long long 
#define st first
#define pii pair<ll,ll>
#define nd second
#define pb push_back
using namespace std;
const int N = 2e5+10;
bool CASE = false;
vector<pii> adj[N];
void solve (){
    int n,m;
    cin >> n >> m;
    for(int i = 0; i < m; i++){
        int u,v,w;
        cin >> u >> v >> w;
        adj[u].pb({w,v});
        // adj[v].pb({w,u});
    }
    vector<ll> dis(n+1,LLONG_MAX);
    vector<bool> vis(n+1,false);
    dis[1] = 0;
    priority_queue<pii,vector<pii>,greater<pii>> pq;
    pq.push({0,1});
    while(!pq.empty()){
        ll cur = pq.top().st, node = pq.top().nd;
        pq.pop();
        if(vis[node]) continue;
        vis[node] = true;
        for(auto a:adj[node]){
            ll v = a.nd, w = a.st;
            if(dis[v] > cur+w){
                dis[v] = cur+w;
                pq.push({dis[v],v});
            }
        }
    }
    for(int i = 1; i <= n; i++) cout << dis[i] << " ";
}
int main(){   
    ios_base::sync_with_stdio(false);cin.tie(0);
    int t = 1;
    if(CASE) cin >> t;
    while(t--){   
        solve();
    }
}