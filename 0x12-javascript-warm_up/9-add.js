#!/usr/bin/node

function add (a, b) {
	let sum = a + b;
  return (sum);
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
if (isNaN(arg1) || isNaN(arg2)) {
  console.log('NaN');
} else {
  const ans = add(arg1, arg2);
  console.log(ans);
}
