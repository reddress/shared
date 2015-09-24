// plotter

var width = 600;
var height = 400;

// 0, 0 should be width / 2, height / 2

var ctx = document.getElementById("canvas").getContext("2d");

var xMin = -6;
var xMax = 6;
var yMin = -4;
var yMax = 4;

ctx.fillStyle = 'black';
ctx.lineWidth = 1;
ctx.strokeStyle = 'black';

function plot(x, y) {
  ctx.beginPath();
  ctx.rect((x - xMin) * (width / (xMax - xMin)),
           height - ((y - yMin) * (height / (yMax - yMin))),
           1, 1);
  ctx.stroke();
}

function sqrt(x) {
  return Math.sqrt(x);
}

function abs(x) {
  return Math.abs(x);
}

function sq(x) {
  return Math.pow(x, 2);
}

// http://9gag.com/gag/aKB8VyO?ref=fbp
function batman(x, y) {
  return (sq(x/7) * sqrt(abs(abs(x)-3)/(abs(x)-3)) * sqrt(abs(y+(3*sqrt(33)/7))/(y+(3*sqrt(33)/7))) - 1) *
    (abs(x/2) - ((3*sqrt(33) - 7)/112)*sq(x) - 3 + sqrt(1-sq(abs(abs(x)-2)-1)) - y) *
    (3) * (4) *
    (5) * (6);
}

console.log(batman(-7, 0));

function circle(x, y) {
  return Math.pow(x, 2) + Math.pow(y, 2) - 9;
}

console.log(circle(2, 1));

var eps = 0.01;

// Note: Incredibly inefficient brute force 
function plotXYFn(fn) {
  for (var x = xMin; x <= xMax; x += 0.001) {
    for (var y = yMin; y <= yMax; y += 0.001) {
      if (Math.abs(fn(x, y)) <= eps) {
        plot(x, y);
      }
    }
  }
}

plotXYFn(circle);
  
plotXYFn(batman);

function offsetEllipse(x, y) {
  return sq(x-2) + sq(4*(y-3)) - 5;
}

plotXYFn(offsetEllipse);
