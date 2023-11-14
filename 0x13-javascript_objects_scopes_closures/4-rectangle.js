#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let k = 0; k < this.height; k++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    if (!this.width || !this.height) {
      return;
    }
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    if (!this.width || !this.height) {
      return;
    }
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
