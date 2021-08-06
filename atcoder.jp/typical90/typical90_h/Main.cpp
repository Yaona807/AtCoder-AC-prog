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
using str = string;
using dbl = double;
using ull = unsigned long long;
using P = pair<int, int>;
using vi = vector<int>;
using vll = vector<ll>;
using vd = vector<dbl>;

int main() {
	int n;
	str s;
	str checkStr = "atcoder";
	vector<ll> cnt(8);
	int mod = pow(10,9) + 7;
	cnt.at(0) = 1;
	in(n);
	in(s);

	rep(i,0,s.length()){
		rep(j,0,7){
			if (s[i] == checkStr[j]){
				cnt.at(j+1) += cnt.at(j);
				cnt.at(j + 1) %= mod;
				break;
			}
		}
	}
	outn(cnt.at(7) % mod);
}