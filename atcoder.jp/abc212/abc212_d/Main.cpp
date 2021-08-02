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
#define rep(i,j,n) for (int i = j; i < (n); ++i)
#define INTMAX 2147483647
#define INTMIN -2147483648
#define LLMAX 9223372036854775807
#define LLMIN -9223372036854775808
using namespace std;
using ll = long long;
using P = pair<int, int>;

int main() {
    int q;
    int p;
    ll x;
    priority_queue<
        ll,
        vector<ll>,
        greater<ll>
    > que;
    ll num = 0;
    cin >> q;

    rep(i,0,q){
        cin >> p;
        if (p == 1){
            cin >> x;
            que.push(x - num);
        } 
        if (p == 2){
            cin >> x;
            num += x;
        } 
        if (p == 3){
            cout << que.top() + num << endl;
            que.pop();
        } 
    }
}