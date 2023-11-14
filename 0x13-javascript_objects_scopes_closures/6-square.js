#!/usr/bin/node

/**
 * Square class that inherits from squareExt class
 */
const SquareExt = require('./5-square');
class Square extends SquareExt {
  charPrint (c) {
	  if (c === undefined) {
		  c = 'X';
	  }

	  let display = '';
	  for (let y = 0; y < this.height; y++) {
		  display += c.repeat(this.width) + '\n';
	  }

	  console.log(display);
  }
}

module.exports = Square;
