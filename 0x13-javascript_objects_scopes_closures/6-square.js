#!/usr/bin/node
/**
 * Square class that inherits Square
 */
const SquareEnt = require('./5-square');

module.exports = class Square extends SquareEnt {
  charPrint (c) {
	  for (let i = 0; i < this.height; i++)
	  {
		  if (!c) {
			  console.log('X'.repeat(this.height));
		  }
		  if (c == 'C') {
			  console.log('C'.repeat(this.height));
		  }
	  }
  }

};

