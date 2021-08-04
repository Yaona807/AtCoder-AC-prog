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
	string s;

	in(s);
	rep(i,0,(s.length()-1)/2){
		if (s[i] != s[s.length()-1-i]){
			outn("No");
			return 0;
		}
	}

	rep(i,(s.length()+3)/2,s.length()){
		if (s[i-1] != s[s.length()-1+((s.length()+3)/2-i)]){
			outn("No");
			return 0;
		}
	}

	outn("Yes");
}