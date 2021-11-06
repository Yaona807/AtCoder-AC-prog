process.stdin.resume();
process.stdin.setEncoding("utf8");

let lines = [];
const reader = require("readline").createInterface({
	input: process.stdin,
	output: process.stdout,
});
reader.on("line", (line) => {
	lines.push(...line.split(" "));
});
reader.on("close", () => {
	solve();
});

function solve() {
	let x = BigInt(lines[0]);
	let y = BigInt(lines[1]);
	let a = BigInt(lines[2]);
	let b = BigInt(lines[3]);

	let ans = 0n;
	while(x*a <= x+b && a*x < y) {
		x *= a;
		ans++;
	}

	ans += (y - x - 1n) / b;

	console.log(ans.toString());

}
