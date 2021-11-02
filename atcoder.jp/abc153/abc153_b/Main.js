process.stdin.resume();
process.stdin.setEncoding('utf8');

var lines = [];
var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
reader.on('line', (line) => {
  lines.push(...line.split(' '));
});
reader.on('close', () => {
  solve();
});

function solve(){
	let h = parseInt(lines[0]);
	let n = parseInt(lines[1]);
	let a_array = [];

	for(let i = 2; i < lines.length; i++){
		a_array.push(parseInt(lines[i]));
	}

	totalDamage = a_array.reduce(function(total,elem){
		return total + elem;
	},0);

	if (totalDamage < h){
		console.log('No');
	}
	else{
		console.log('Yes');
	}
}
