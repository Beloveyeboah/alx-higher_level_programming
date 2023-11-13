#!/usr/bin/node

const arg = parseInt(process.argv[2]);
const msg = 'C is fun';

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < arg) {
    console.log(msg);
    count++;
  }
}
