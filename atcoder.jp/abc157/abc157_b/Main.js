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
	let bingo = [];
	const ROW_COUNT = 3
	let ans = 'No';
	
	let index = 0
	
	for (let i = 0; i < ROW_COUNT; i++) {
		bingo.push([]);
		for (let j = 0; j < ROW_COUNT;j++){
			bingo[i].push(parseInt(lines[index++]));
		}
	}

	let n = parseInt(lines[index++]);

	for (let i = 0; i < n; i++) {
		let b = parseInt(lines[index++]);

		for (let j = 0; j < ROW_COUNT; j++) {
			for (let k = 0; k < ROW_COUNT;k++){
				if (bingo[j][k] === b){
					bingo[j][k] = -1;
				}
			}
		}
	}

	//　横の走査 
	for (let i = 0; i < ROW_COUNT; i++) {
		let cnt = 0;
		for (let j = 0; j < ROW_COUNT;j++){
			if (bingo[i][j] === -1){
				cnt++;
			}
		}
		if (cnt === 3){
			ans = 'Yes';
		}
	}

	//　縦の走査 
	for (let i = 0; i < ROW_COUNT; i++) {
		let cnt = 0;
		for (let j = 0; j < ROW_COUNT;j++){
			if (bingo[j][i] === -1){
				cnt++;
			}
		}
		if (cnt === 3){
			ans = 'Yes';
		}
	}

	// 斜めの走査
	let cnt1 = 0;
	let cnt2 = 0;
	for (let i = 0; i < ROW_COUNT; i++) {
		if (bingo[i][i] === -1){
			cnt1++;
		}
		
		if (bingo[ROW_COUNT-i-1][i] === -1){
			cnt2++;
		}
		
		if (cnt1 === 3 || cnt2 === 3){
			ans = 'Yes';
		}
	}

	console.log(ans);

}
