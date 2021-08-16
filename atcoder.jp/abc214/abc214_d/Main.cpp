#include <iostream>		 // cout, endl, cin
#include <string>		 // string, to_string, stoi
#include <vector>		 // vector
#include <algorithm>	 // min, max, swap, sort, reverse, lower_bound, upper_bound
#include <utility>		 // pair, make_pair
#include <tuple>		 // tuple, make_tuple
#include <cstdint>		 // int64_t, int*_t
#include <cstdio>		 // printf
#include <map>			 // map
#include <cmath>		 // pow
#include <queue>		 // queue, priority_queue
#include <set>			 // set
#include <stack>		 // stack
#include <deque>		 // deque
#include <unordered_map> // unordered_map
#include <unordered_set> // unordered_set
#include <bitset>		 // bitset
#include <cctype>		 // isupper, islower, isdigit, toupper, tolower
#define rep(i, j, n) for (ll i = j; i < (ll)(n); ++i)
#define reps(i, j, n, k) for (ll i = j; i < (ll)(n); i += k)
#define INTMAX 2147483647
#define INTMIN -2147483648
#define LLMAX 9223372036854775807
#define LLMIN -9223372036854775808
#define in(s) cin >> s;
#define out(s) cout << s;
#define outn(s) cout << s << endl;
#define sortN(v) sort(v.begin(),v.end());
#define sortR(v) sort(v.begin(),v.end(),greater<int>{});
using namespace std;
using ll = long long;
using str = string;
using dbl = double;
using ull = unsigned long long;
using P = pair<int, int>;
using vi = vector<int>;
using vll = vector<ll>;
using vd = vector<dbl>;
using vb = vector<bool>;

struct UnionFInd{
	vector<int> parents, rank;

	void init(int n){
		rank.resize(n, -1);
		parents.resize(n, -1);
		for (int i = 0; i < n; i++){
			rank[i] = 0;
		}
	}

	int root(int x){
		if (parents[x] < 0){
			return x;
		}else{
			parents[x] = root(parents[x]);
			return parents[x];
		}
	}

	bool same(int x, int y){
		return root(x) == root(y);
	}

	void unite(int x, int y){
		x = root(x);
		y = root(y);

		parents[x] += parents[y];
		parents[y] = x;
	}
	int size(int x){
		x = root(x);
		return -parents[x];
	}
};

int main(){
	int n;
	in(n);
	vector<vi> edges(n-1);
	rep(i,0,n-1){
		int u,v,w;
		in(u >> v >> w);
		u--;
		v--;
		edges[i].push_back(w);
		edges[i].push_back(u);
		edges[i].push_back(v);

	}
	sort(edges.begin(),edges.end());
	ll ans = 0;
	UnionFInd uf;
	uf.init(n);
	rep(i,0,n-1){
		int u,v,w;
		w = edges[i][0];
		u = edges[i][1];
		v = edges[i][2];
		ans += (ll)w * uf.size(u) * uf.size(v);
		uf.unite(u,v);
	}
	outn(ans);
}

