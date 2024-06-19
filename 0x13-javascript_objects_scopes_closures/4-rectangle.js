#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((h > 0) && (w > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const rotator = this.height;
    this.height = this.width;
    this.width = rotator;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
