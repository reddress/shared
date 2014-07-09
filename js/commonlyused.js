_ length of things

"some string".length
[3,4,5].length

objects do not have lengths

function Point(x, y) {
  this.x = x;
  this.y = y;
}
Point.prototype.dist = function () {
  return Math.sqrt(this.x * this.x + this.y * this.y);
};
var p = new Point(3, 5);
p instanceof Point  // true

iterating over array elements:

[1, 2, 3].forEach(
  function (elem, index) {  // index is optional
    // index + " " + elem
  });

[1, 2, 3].map(function (x) { return x * x; })

