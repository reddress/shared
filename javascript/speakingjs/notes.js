ch01.html

statements "do things"
  - ex. var foo;

expressions produce values
  - ex. function arguments
  - ex. right side of assignment
  - ex. ternary if, which can be used as a function argument
  - myFunction(y >= 0 ? y : -y)

an expression may be used in place of a statement

place a semicolon at the end of a function expression:
  - var f = function () { };

all values have properties, which consist of a key/name and a value
  - properties may be read/written with the dot operator

strings have the length property (str.length)

primitive values are:
  - numbers (all are floating point)
  - strings (enclosed by ' ' or " ")
  - booleans (true, false)
  - null (no object: a nonvalue where an object is expected, such as params)
  - undefined (no value: uninitialized variables, nonexistent properties)

everything else is an object, which commonly are:
  - plain objects created by literals: { firstName: "Joe", lastName: "H" }
  - arrays: ['a', 'b', 'c']
  - regular expressions: /^a+b+$/

while primitives representing the same value are considered equal, each object
has a unique identity:

var obj1 = {};
var obj2 = {};
obj1 === obj2  // false

primitives are always immutable, including their properties

objects are mutable, you can freely add, remove, and change properties

explicitly check for undefined and null values
  - if (x === undefined || x === null) { }

falsy values include undefined, null, 0, NaN, and ''

empty objects and arrays are considered true, can check with Boolean()

typeof is mainly used to describe primitives; it may return (all strings):
  - 'undefined', 'object', 'boolean', 'number', 'string', 'function'
  - or an engine-specific value
  - typeof null returns 'object', a bug that is not fixed for legacy reasons

x instanceof C returns true if the object x has been created by the
constructor C
  - [] instanceof Array  // true

NaN is an error value (not a number), while Infinity exceeds normal numbers
Infinity can be used as default values in looking for a minimum or maximum

get a string substring with slice()

remove whitespace with trim()

find a string with indexOf()

conditionals:

if (condition) {
  // then
} else if (something else) {
  // then
} else {
  // else
}

switch (fruit) {
case 'banana':
  //
  break;
case 'apple':
  //
  break;
default:
  //
}

for (var i=0; i < arr.length; i++) {
  // arr[i];
}

while (i < arr.length) {
  // arr[i];
  i++;
}

do {
  // ...
} while (condition);  // body is always executed at least once

break leaves the loop, continue starts a new loop iteration

function declaration:

function add(x, y) {
  return x + y;
}

add(6, 2)  // 8

assign a function expression to a variable:

var add = function (x, y) {
  return x + y;
};  // add a semicolon in this case

the special variable arguments stores the arguments of a function call; it is
not a proper array, it is array-like, with a length property and indexable

converting array-like object to an array:
function toArray(arrayLikeObj) {
  return Array.prototype.slice.call(arrayLikeObj);
}

assign default parameters with OR:

function pair(x, y) {
  x = x || 0;
  y = y || 0;
  return [x, y];
}

exceptions are thrown and used in try/catch blocks

throw new Error("message");

try {
  //
} catch (exception) {
  console.log(exception);
}

'use strict'; as first line in <script> or function body enables strict mode

variables are function-scoped

although variable declarations are hoisted, assignments are not

a closure is a function plus the connections to the variables of its
surrounding scopes:

function makeIncrementor(start) {
  return function () {
    start++;
    return start;
  }
}

var inc = makeIncrementor(5);
inc();
inc();

IIFE: immediately invoked function expression: used to introduce a new scope
and prevent a variable becoming global

(function () {
  var tmp = ...;
}());

closures keep connections to outer variables, which sometimes is not wanted

var result = [];
for (var i = 0; i < 5; i++) {
  result.push(function () { return i; });
}
console.log(result[2]());  // 5, not 2

to keep a snapshot of i, an IIFE is needed:

var resultIIFE = [];
for (var i = 0; i < 5; i++) {
  (function () {
    var i2 = i;
    resultIIFE.push(function () { return i2; });
  }());
}

alternatively:

var resultIIFE = [];
for (var i = 0; i < 5; i++) {
  (function (i) {
    resultIIFE.push(function () { return i; });  // variable name can be same
  }(i));  // pass i as IIFE's argument
}

objects are a set of properties; a function property is called a method

the in operator checks if a property exists; if not, you get undefined

'property' in myobject is the same as myobject.property !== undefined

delete will remove a property

use square brackets to access non-identifier keys or key as a variable

bind() may be used to extract a method (without it, this becomes undefined)

every function has its own special variable, this

one way to refer to an outer this is to save it in a different variable:

function () {
  var that = this;
  this.friends.forEach(function (friend) {
    console.log(that.name + " says hi to " + friend);
  });
}

forEach also has a second parameter to provide a value for this

functions, when invoked with new, become constructors; by convention they
should begin with a capital letter

function Point(x, y) {
  this.x = x;
  this.y = y;
}
Point.prototype.dist = function () {
  return Math.sqrt(this.x * this.x + this.y * this.y);
};
var p = new Point(3, 5);
p instanceof Point  // true

the instance data (this) x and y are specific to each instance, but the method
attached to the prototype is shared among all instances

assigning out of bounds to an array will extend it, filling empty spaces as
undefined

may check if something is in an array with the in operator

arrays, being objects, can have properties: arr.foo = 123;

some array methods: slice(a, b), push(v), pop(), shift(), unshift(v),
indexOf(v), join(sep)

the most important ways of iterating over array elements are forEach and map

[1, 2, 3].forEach(
  function (elem, index) {  // index is optional
    // index + " " + elem
  });

[1, 2, 3].map(function (x) { return x * x; })

regular expressions are delimited by slashes
  /$abc^/  /[A-Za-z0-9]+/

  /^a+b+$/.test('aaa')  // false - sees if there is a match

  /a(b+)a/.exec('_abbba_aba_')  // matches and captures groups

'<a> <bbb>'.replace(/<(.*?)>/g, '[$1]')  // /g flag replaces all
// , otherwise only the first occurrence is replaced

