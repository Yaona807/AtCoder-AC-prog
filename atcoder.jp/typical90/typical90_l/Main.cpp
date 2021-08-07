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
using namespace std;
using ll = long long;
using str = string;
using dbl = double;
using ull = unsigned long long;
using P = pair<int, int>;
using vi = vector<int>;
using vll = vector<ll>;
using vd = vector<dbl>;

struct UnionFInd
{
	vector<int> parents, rank;

	void init(int n)
	{
		rank.resize(n, -1);
		parents.resize(n, -1);
		for (int i = 0; i < n; i++)
		{
			parents[i] = i;
			rank[i] = 0;
		}
	}

	int root(int x)
	{
		return parents[x] == x ? x : parents[x] = root(parents[x]);
	}

	bool same(int x, int y)
	{
		return root(x) == root(y);
	}

	void unite(int x, int y)
	{
		x = root(x);
		y = root(y);

		if (x == y)
		{
			return;
		}

		if (rank[x] < rank[y])
		{
			parents[x] = y;
		}
		else
		{
			parents[y] = x;
			if (rank[x] == rank[y])
			{
				rank[x]++;
			}
		}
	}
};

int main()
{
	int h, w;
	int q;
	int ra, ca, rb, cb;
	int t;
	UnionFInd uf;
	vector<int> dirX = {-1, 0, 1, 0};
	vector<int> dirY = {0, 1, 0, -1};

	in(h);
	in(w);
	in(q);

	uf.init(h * w);

	vector<vector<int>> treeId(h, vector<int>(w, 0));
	vector<vector<bool>> used(h, vector<bool>(w, false));

	rep(i, 0, h)
	{
		rep(j, 0, w)
		{
			treeId[i][j] = i * w + j;
		}
	}
	rep(i, 0, q)
	{
		in(t);
		if (t == 1)
		{
			in(ra);
			in(ca);
			rep(d, 0, 4)
			{
				if (0 > ra + dirX[d] - 1 || h <= ra + dirX[d] - 1 || 0 > ca + dirY[d] - 1 || w <= ca + dirY[d] - 1)
				{
					continue;
				}
				if (used[ra + dirX[d] - 1][ca + dirY[d] - 1] == false)
				{
					continue;
				}
				uf.unite(treeId[ra - 1][ca - 1], treeId[ra + dirX[d] - 1][ca + dirY[d] - 1]);
			}
			used[ra - 1][ca - 1] = true;
		}
		else
		{
			bool ans = false;
			in(ra);
			in(ca);
			in(rb);
			in(cb);
			if (uf.same(treeId[ra - 1][ca - 1], treeId[rb - 1][cb - 1]))
			{
				ans = true;
			}
			if (used[ra - 1][ca - 1] == false || used[rb - 1][cb - 1] == false)
			{
				ans = false;
			}
			if (ans == true)
			{
				outn("Yes");
			}
			else
			{
				outn("No");
			}
		}
	}
}