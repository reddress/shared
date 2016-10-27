// Warmup default code to read line by line

process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

function strToArr(str) {
  var arr = str.split(' ');
  return arr.map(Number);
}

// Writing output

console.log("...");
// or
process.stdout.write("...");

////////////////////////////////////////////
// Solve problem, called after end of input

function main() {
  // ...
}


//////////////////////////////////
// Alternate code to read in data

// called after end of input
function processData(input) {
    //Enter your code here
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
