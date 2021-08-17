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

int main(){
	int n;
	in(n);
	vi aVec(n);
	rep(i,0,n) {in(aVec[i]);}

	for(auto a : aVec){
		if (a % 2 != 0){continue;}

		bool judge = (a % 3 == 0 || a % 5 == 0);
		if (!judge){
			outn("DENIED");
			return 0;
		}
	}
	outn("APPROVED");
}

