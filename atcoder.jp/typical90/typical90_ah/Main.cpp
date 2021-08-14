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

// 要素数のカウント
void cntMap(map<int,int> *m, int a){
	if ((*m).find(a) == (*m).end()){
		(*m).insert(make_pair(a,1));
	}else{
		(*m)[a]++;
	}
}

int main(){
	int n,k;
	in(n >> k);
	vi aVec(n);

	rep(i,0,n){
		int a;
		in(a);
		aVec[i] = a;
	}

	// 二分探索
	int ok,ng;
	ok = 1;
	ng = n+1;
	while(abs(ok-ng) > 1){
		int mid = (ok+ng) / 2;
		int flag = false;
		
		// 初めの要素数をカウント
		map<int,int> m;
		rep(i,0,mid){
			cntMap(&m,aVec[i]);
		}

		rep(i,0,n-mid){
			// 条件を満たしていたらtrue
			if (m.size() <= k) flag = true;
			
			// しゃくとり法の要領で探索
			m[aVec[i]]--;

			if(m[aVec[i]] == 0){
				m.erase(aVec[i]);
			}

			cntMap(&m,aVec[i+mid]);
		}

		if (m.size() <= k) flag = true;

		if (flag){
			ok = mid;
		}else{
			ng = mid;
		}
	}

	outn(ok);
}

