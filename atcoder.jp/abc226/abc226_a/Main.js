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
	let x = parseFloat(lines[0]);

	console.log(parseInt(x+0.5));
}
