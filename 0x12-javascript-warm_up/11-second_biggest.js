#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg.length === 0) {
  console.log(0);
} else if (arg.length === 1) {
  console.log(0);
} else {
  const nums = arg.map(Number);

  const sortednums = nums.sort((a, b) => b - a);
  const secondMax = sortednums[1];
  console.log(secondMax);
}
