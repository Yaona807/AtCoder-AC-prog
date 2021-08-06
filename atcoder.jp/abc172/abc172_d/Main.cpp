#include <iostream> // cout, endl, cin
#include <string> // string, to_string, stoi
#include <vector> // vector
#include <algorithm> // min, max, swap, sort, reverse, lower_bound, upper_bound
#include <utility> // pair, make_pair
#include <tuple> // tuple, make_tuple
#include <cstdint> // int64_t, int*_t
#include <cstdio> // printf
#include <map> // map
#include <cmath> // pow
#include <queue> // queue, priority_queue
#include <set> // set
#include <stack> // stack
#include <deque> // deque
#include <unordered_map> // unordered_map
#include <unordered_set> // unordered_set
#include <bitset> // bitset
#include <cctype> // isupper, islower, isdigit, toupper, tolower
#define rep(i,j,n) for (ll i = j; i < (ll)(n); ++i)
#define reps(i,j,n,k) for (ll i = j; i < (ll)(n); i += k)
#define INTMAX 2147483647
#define INTMIN -2147483648
#define LLMAX 9223372036854775807
#define LLMIN -9223372036854775808
#define in(s) cin >> s;
#define out(s) cout << s;
#define outn(s) cout << s << endl;
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
	int n;
	ll ans = 0;
	vector<int> cnt(20000000);
	in(n);
	
	rep(i,1,n+1){
		reps(j,i,n+1,i){
			cnt.at(j) += 1;
		}
	}

	rep(i,1,n+1){
		ans += cnt.at(i) * i;
	}

	outn(ans);

}