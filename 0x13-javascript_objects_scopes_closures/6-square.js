#!/usr/bin/node
/**
 * Square class that inherits Square
 */
const SquareEnt = require('./5-square');

module.exports = class Square extends SquareEnt {
  charPrint (c) {
    const display = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let A = '';
      let y = 0;
      while (y < this.width) {
        A += display;
        y++;
      }
      console.log(A);
    }
  }
};
