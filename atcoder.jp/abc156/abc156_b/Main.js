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
	const n = lines[0];
	const k = lines[1];

	console.log(parseInt(n,10).toString(k).length)
}
