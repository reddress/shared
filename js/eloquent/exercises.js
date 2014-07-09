// ch02 program structure

function print() {
  //console.log("print()");
  console.log.apply(console, arguments);
}

function loopTriangle(rows) {
  for (var i = 0; i < rows; i++) {
    var row = "";
    do {
      row += "#";
    } while (row.length <= i)
    print(row);
  }
}

function fizzBuzz() {
  for (var n = 0; n < 32; n++) {
    if (n % 5 === 0 && n % 3 === 0) {
      print("FizzBuzz");
    } else if (n % 5 === 0) {
      print("Buzz");
    } else if (n % 3 === 0) {
      print("Fizz");
    } else {
      print(n);
    }
  }
}

function chessBoard(n) {
  var output = "";
  for (var row = 0; row < n; row++) {
    if (row % 2 === 1) {
      output += " ";
    }
    for (var col = 0; col < n; col++) {
      if (col % 2 === 1) {
        output += " ";
      } else {
        output += col;
      }
    }
    output += "\n";
  }
  return output;
}

function minOfTwo(a, b) {
  return a < b ? a : b;
}
// minOfTwo(23,2)

function min() {
  var result = Infinity;
  for (var i = 0; i < arguments.length; i++) {
    if (arguments[i] < result) {
      result = arguments[i];
    }
  }
  return result;
}
// min(30,12,2,3,4,5)

function isEven(n) {
  if (n === 0) {
    return true;
  } else if (n === 1) {
    return false;
  } else {
    return isEven(n - 2);
  }
}
// isEven(41)

function countChar(s, c) {
  var count = 0;
  for (var i = 0; i < s.length; i++) {
    if (s.charAt(i) === c) {
      count++;
    }
  }
  return count;
}

function countBs(s) {
  return countChar(s, "B");
}
// countBs("BBCB", "B");
// countChar("abracadabra", 'a');

