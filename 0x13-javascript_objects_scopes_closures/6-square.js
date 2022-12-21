#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (char) {
    if (char === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.height; col += 1) {
        console.log(char.repeat(this.width));
      }
    }
  }
};
