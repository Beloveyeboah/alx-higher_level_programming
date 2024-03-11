#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  const print = 'X';

  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += print;
    }
    console.log(row);
  }
}
