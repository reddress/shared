// plotter

var width = 600;
var height = 400;

// 0, 0 should be width / 2, height / 2

var ctx = document.getElementById("canvas").getContext("2d");

var xMin = -6;
var xMax = 6;
var yMin = -4;
var yMax = 4;


function randomColor() {
  return '#'+Math.floor(Math.random()*16777215).toString(16);
}

function blueGradient(y) {
  return '#00' + (Math.floor((y / height) * 16)).toString(16);
}

function plot(x, y) {
  ctx.beginPath();
  var xPixel = (x - xMin) * (width / (xMax - xMin));
  var yPixel = height - ((y - yMin) * (height / (yMax - yMin)));
  ctx.rect(xPixel, yPixel, 1, 1);
  ctx.fillStyle = blueGradient(yPixel);
  ctx.lineWidth = 3;
  ctx.strokeStyle = blueGradient(yPixel);
  
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
  return (sq(x/7) * sqrt(abs(abs(x)-3)/(abs(x)-3)) +
          sq(y/3) * sqrt(abs(y+(3*sqrt(33)/7))/(y+(3*sqrt(33)/7))) - 1) *
    (abs(x/2) - ((3*sqrt(33) - 7)/112)*sq(x) - 3 + sqrt(1-sq(abs(abs(x)-2)-1)) - y) *
    (9*sqrt((abs((abs(x)-1)*(abs(x)-.75)))/((1-abs(x))*(abs(x)-.75))) - 8*abs(x)-y) * (3*abs(x)+.75*sqrt((abs((abs(x)-.75)*(abs(x)-.5)))/((.75-abs(x))*(abs(x)-.5)))-y) *
    (2.25*sqrt((abs((x-.5)*(x+.5)))/((.5-x)*(.5+x)))-y) * ((6*sqrt(10)/7)+(1.5-.5*abs(x))*sqrt((abs(abs(x)-1))/(abs(x)-1))-(6*sqrt(10)/14)*sqrt(4-sq(abs(x)-1))-y);
}

console.log(batman(-7, 0));

function circle(x, y) {
  return Math.pow(x, 2) + Math.pow(y, 2) - 9;
}

console.log(circle(2, 1));

var eps = 0.2;

function xPixelToCoord(x) {
  var coordWidth = xMax - xMin;
  return xMin + coordWidth * (x / width);
}

function yPixelToCoord(y) {
  var coordHeight = yMax - yMin;
  var invertY = height - y;
  return yMin + coordHeight * (invertY / height);
}

console.log(xPixelToCoord(200));
console.log(yPixelToCoord(100));

// Note: Incredibly inefficient brute force 
function plotXYFn(fn) {
//  for (var x = xMin; x <= xMax; x += 0.001) {
//  for (var y = yMin; y <= yMax; y += 0.001) {
  for (var x = 0; x <= width; x++) {
    for (var y = 0; y <= height; y++) {
      var coordX = xPixelToCoord(x);
      var coordY = yPixelToCoord(y);
      
      if (Math.abs(fn(coordX, coordY)) <= eps) {
        plot(coordX, coordY);
      }
    }
  }
}

plotXYFn(circle);
  
plotXYFn(batman);

function offsetEllipse(x, y) {
  var offX = 0;
  var offY = 0;
  var scaleY = 4
  return sq(x-offX) + sq(scaleY*(y-offY)) - 5;
}

plotXYFn(offsetEllipse);

function hyperbola(x, y) {
  return sq(x) - sq(y) - 4;
}

plotXYFn(hyperbola);
