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

but, to check if a variable exists, use:
typeof undeclaredVariable === 'undefined'

falsy values include undefined, null, 0, NaN, and ''

empty objects and arrays are considered true, can check with Boolean()

typeof is mainly used to describe primitives; it may return (all strings):
  - 'undefined', 'object', 'boolean', 'number', 'string', 'function'
  - or an engine-specific value
  - typeof null returns 'object', a bug that is not fixed for legacy reasons

x instanceof C returns true if the object x has been created by the
constructor C
  - [] instanceof Array  // true

NaN is an error value, while Infinity exceeds normal numbers

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

ch07.html

{ foo: 123 }, an object literal, and function foo() { } are ambiguous. You
cannot use these as statements. To evaluate the object literal and return an
object, and to execute IIFEs, these expressions must be inside parentheses

({ foo: 123 })

(function () { return 'abc' }())

do-while must have a semicolon at the end: do { ... } while ();

invoking methods on number literals may be done as:

3..toString()  // two dots
3 .toString()  // space before dot
(3).toString()
3.0.toString()

ch08.html

wrapping primitives, such as new Boolean(true), result in objects. They cannot
be compared (== or ===) unless unwrapped (with .valueOf()). However, you can
attach properties to wrapped primitives.

converting any object (including new Booleans) with Boolean() results in true

can customize valueOf() and toString() to influence behavior of Number() and
String():

var n = { valueOf: function () { return 123; } };
Number(n)  // 123

var s = { toString: function () { return '8'; } };
String(s)  // '8'

ch09.html

void is useful to discard the result of an expression, for example:
javascript:void window.open("http://example.com/")

typeof returns a string: one of 'undefined', 'object', 'boolean', 'number',
'string', 'function', or 'object'. May also be engine-dependent

to check if a variable exists, use:
typeof undeclaredVariable === 'undefined'

ch10.html

check boolean value with Boolean() (the function, not constructor new Boolean)

all objects convert to boolean 'true', including new Boolean(false)

default value pattern: theValue || defaultValue (but will return defaultValue
                                                 if theValue is falsy)

ch11.html

NaN is of type 'number', and is the only value unequal to itself, that is,
NaN !== NaN is true

checking NaN with isNaN() may not be enough, because its argument is converted
first, and may incorrectly return true: isNaN('xyz')  // true

checking for Infinity can be done with === or with isFinite()

there are a positive and negative zero, which may be checked by division by
zero: the resulting infinity will be positive or negative

checking whether two floating numbers are about equal can be done by taking
an upper bound for rounding errors (machine epsilon)

var EPSILON = Math.pow(2, -53);
function epsEq(x, y) {
  return Math.abs(x - y) < EPSILON;
}

The remainder operator, %, is not modulo. In JavaScript, the result of % has
the sign of the first operand, while for modulo, it has the sign of the second
operand. This behavior might give unexpected results when the first operand is
negative

to input and output binary (or other numeric base) numbers, use:

parseInt(str, base) and num..toString(base)

control the string representation of a number using

num..toFixed(), the number of decimal digits after the dot,
num..toPrecision(), which limits the number of digits of the mantissa,
independent of the decimal dot
num..toExponential() forces exponential notation

isFinite() checks if argument is an actual number (not Infinity nor NaN)

ch12.html

to spread a string over multiple lines, use a backslash \ or concatenate (+)

character escapes \x-- (ASCII) and \u---- (Unicode)

'abc'.charAt(2) and 'abc'[2] get the nth character

for displaying data, JSON.stringify(value, replacer?, space?) is often better
than String()

conversions do not necessarily convert back

String.fromCharCode(97, 98, 99) produces a string from the UTF-16 code units

an array of numbers can be converted as follows
String.fromCharCode.apply(null, [97, 98, 99])

the inverse is "abc".charCodeAt(0)

to create an array of character codes,
'abc'.split('').map(function (x) { return x.charCodeAt(0); })

a string`s length is a property: 'abc'.length

'abc'.charAt(n) or 'abc'[n] returns a string with the character at position n

'abc'.slice(start, end) returns a substring from start up to, but excluding end
its parameters may be negative, and then the length is added to them

'abc'.substring() should be avoided in favor of slice()

to get an array of substrings, use 'a,b,c'.split(',', limit?) where limit is
the upper limit of array elements

if a regular expression group is used, the matches are returned as elements
'a,  b  ,  '.split(/(,)/)  // ['a', ',', '  b  ', ',', '  ']

the empty string separates all characters 'abc'.split('')  // ['a', 'b', 'c']

string transformation functions include
str.trim(), str.concat(s1, s2, s3, ...), toLower/UpperCase(),
toLocaleLower/UpperCase()

str.indexOf(searchString, position?) looks for searchString starting from
position, and returns the position where it is found, or -1 if it is not found

str.lastIndexOf() looks backwards

str.localeCompare(other) returns a number, where 0 means the two are equivalent
not all JavaScript engines implement this method correctly

str.search(re) returns the first index where the regular expression matches

str.match(re) returns a match object for the first match if /g is not set
otherwise, all complete matches (group 0) are returned in an array

str.replace(search, replacement) will only replace the first occurrence unless
a regular expression with /g flag is used for 'search' parameter

a $ sign in a replacement string allows you to refer to the complete match or
a captured group

'iixxxixx'.replace(/i+/g, '($&)') or '($1)'

the replacement may also be a function
function replacement(all) { return '(' + all.toUpperCase() + ')'; }
'axabbyyxaazz'.replace(/a+|b+/g, replacement)

ch13.html

variable declarations may be combined in a single var statement

var x, y=123, z;

a label is an identifier followed by a colon; it allows breaking or continuing
even from a loop nested in it. A label in front of a block allows breaking out
of that block. In both cases, the label name becomes an argument of break or
continue: break myLabel;

for do-while loops, the do statement is executed at least once

for loops execute the init statement once before the loop, and it continues
as long the condition is true. post_iteration is executed after each iteration
of the loop.
  
when incrementing an index, the iterating variable ends up holding the value
that does not satisfy the condition:

var x = 0;
for (; x < 3; x++) {
  console.log(x);  // 0 1 2
}
x  // 3

avoid using for-in, because it iterates over indices and property keys, not
values. Also, it includes inherited properties and methods, which may not be
what you want

do not use for each-in (it exists only in Firefox)

if (condition) {
  // something
} else if (other condition) {
  // other
} else {
  // return 0;
}

better to use braces to avoid ambiguous interpretation

execution in a switch clause continues to the next clause if there is no
terminating statement such as break. return and throw also exit the switch

there may be multiple case labels in a row:

switch (color) {
case 'red':
case 'yellow':
case 'blue':
  // primary color
  break;
case 'purple':
case 'green':
  // secondary color
default:
  throw 'not a color';
}

the value after case may be arbitrary, such as x < y, x === y, 2 + 3

with (object) { /* statements */ } turns the properties of object into local
variables for statements. Its use is discouraged. Instead, assign a temporary
variable for the desired object:

var b = foo.baz.quux;
console.log(b.firstName + ' ' + b.lastName);

or use an IIFE:

(function (b) {
  console.log(b.firstName + ' ' + b.lastName);
}(foo.baz.quux));

if the debugger is active, the statement "debugger;" functions as a breakpoint

ch14.html

if there is a problem that can`t be handled meaningfully, throw an exception
catch exceptions where errors can be handled

throw can throw any JavaScript values, but preferably, exception objects
should be used (or subclasses)

if (somethingBad) {
  throw new Error('Error: something bad happened');
}

a try must be followed by at least one of catch and finally.

to switch between different kinds of errors, you can use

try {
  // ...
} catch (e) {
  switch (e.constructor) {
  case SyntaxError:
    break;
  case CustomError:
    break;
  }
}

but this approach only matches direct instances of the constructor

finally is executed after a return statement in try.

Error is a generic constructor for errors

Other errors include RangeError, ReferenceError, SyntaxError, TypeError and
URIError

the error properties are: message, name and stack: non-standard but generally
available

ch15.html

invoking a function with new makes it a constructor (an object factory). By
convention, constructor names start with uppercase letters

when a function is an object`s property, it is a method, invoked as
obj.method(). By convention, method names start with lowercase letters

parameters are used when defining functions; arguments are used to invoke a
function

all functions are objects (instances of Function), and get their methods from
Function.prototype

function (x, y) { return x + y; } is a (anonymous) function expression; it may
be assigned to a variable:

var add = function (x, y) { return x + y; };

named function expressions allow self-recursion; its name is only accessible
inside the function expression

function f(x) { return x; } is a function declaration

the Function() constructor accepts strings, similar to eval() and is slow

var add = new Function('x', 'y', 'return x + y');

hoisting is moving to the beginning of a scope; function declarations are
hoisted completely

only variable declarations are hoisted, assignments are not

f.name is a nonstandard property for function objects; it is '' for anonymous
function expressions

function declarations are preferred over function expressions because of
hoisting

func.apply(thisValue, argArray) takes the elements of argArray as arguments to
func. In a non-object-oriented setting, thisValue can be null

for example:
Math.max.apply(null, [12, 33, 2])

func.bind(thisValue, arg1, arg2, ..., argN) creates a new function with first
arguments arg1 up to argN. It has the effect of partial function application

a function`s parameters are stored in the array-like variable arguments, from
which extra parameters may be accessed

if a function call is missing parameters, they will be undefined

arguments is an object, and the length property. Individual parameters may be
read and written by index, but there are no array methods like slice, forEach

arguments.callee (a reference to the current function) does not work in strict
mode. Instead, use named function expressions

to check for mandatory parameters, you can check param === undefined, or
arguments.length < 1.

to assign a default value, you can write:

if (optional === undefined) { optional = "default value"; }

if (!optional) { optional = "default value"; }

optional = optional || "default value";  // careful with falsy values

if (arguments.length < 3) { optional = "default value"; }

to simulate pass-by-reference, you must wrap the variable`s value in an array

function incRef(numberRef) {
  numberRef[0]++;
}
var n = [7];
incRef(n);
console.log(n[0]);

combining map with a function like parseInt(), where signatures do not match,
can lead to unexpected results.

explicitly assigning signatures with a callback avoids unexpected results:
['1', '2', '3'].map(function (x) { return parseInt(x, 10); })

named parameters can be placed in an "option object", usually after
positional parameters:

selectEntries({ start: 3, end: 20, step: 2});

function selectEntries(options) {
  options = options || {};
  var start = options.start || 0;
  // ...
}

ch16.html

variables are lexically scoped. Variables are accessible in nested scopes

if an inner scope variable has the same name as one surrounding it, it will
shadow (block) the outer variable.

variables in JavaScript are function-scoped

with non-strict (sloppy) mode, undeclared variables become global

new scopes are introduced with Immediately Invoked Function Expressions, IIFEs
which must be surrounded by parentheses, otherwise they are interpreted as
function declarations.

if (cond) {
  (function () { // open IIFE
    var tmp = 0;
    // ...
  }());  // close IIFE, remember to put trailing semicolon
}

IIFEs can also start with ! or void instead of using surrounding parentheses

if already in expression context, the surrounding parentheses are not needed:

var File = function () {
  var UNTITLED = "Untitled";
  function File(name) {
    this.name = name || UNTITLED;
  }
  return File;
}();

parameters can be used to define variables inside the IIFE:

var x = 15;
(function (twice) {
  console.log(twice);
}(x * 2));

an IIFE enables private data, to avoid polluting the global namespace

var setValue = function () {
  var prevValue;  // accessible only by setValue
  return function (value) {
    if (value !== prevValue) {
      console.log('Changed: ' + value);
      prevValue = value;
    }
  };
}();

avoid global variables because of unwanted side effects and name clashes

IIFEs make local scopes:

<script>
  (function () {
    var tmp = something();
    processData(tmp);
  }());
</script>

the global object, accessible as this in global scope, can be used to create,
read, and change global variables

for cross-platform (Node.js or browser) access to the global object:

(function (g) {
  // g points to the global object
}(typeof window !== 'undefined' ? window : global));

to indicate a variable is global, you can add a prefix such as g_

use window.someVar to add variables to the global scope, even from a nested
scope

closure: if a function leaves the scope where it was created, it still stays
connected to the variables of that scope and its surrounding scopes

function createInc(startValue) {
  return function (step) {
    startValue += step;
    return startValue;
  };
}

var inc = createInc(5);
inc(1)  // 6
inc(2)  // 8

a closure is a function plus the connection to the scope in which it was
created. A variable is free if it was not declared within the function

a closure is an example of an environment surviving after execution has
left its scope.

due to functions being closures, they work with the current value of the
variable. For example, in for loops:

function f() {
  var result = [];
  for (var i = 0; i < 3; i++) {
    var func = function () {
      return i;
    };
    result.push(func);
  }
  return result;
}
console.log(f()[1]());  // 3, because when the inner function is called,
                        // the loop has finished and i is 3

we must create new environments for each iteration of i, with IIFEs:

function f() {
  var result = [];
  for (var i = 0; i < 3; i++) {
    (function () {
      var pos = i;
      var func = function () {
        return pos;
      };
      result.push(func);
    }());
  }
  return result;
}
console.log(f()[1]());  // 1

or:

for (var i = 0; i < 3; i++) {
  (function (i) {
    var func = function () {
      return i;
    };
    result.push(func);
  }(i));
}

ch17.html

roughly, all objects are maps (dictionaries) from strings to values

a (key, value) entry is called a property. Keys are always strings. When a
value is a function, such a property is called a method.

there are three kinds of properties:

properties (or named data properties) are mappings from strings to values,
including methods. The most common type of property.

accessors (or named accessor properties) are methods whose invocations look
like getting or setting a property. They allow you to compute the values of
properties. They are virtual properties and not storage space.

internal properties exist only in the language specification. They are shown
inside brackets. For example, [[Prototype]] is readable via
Object.getPrototypeOf()

object literals are direct instances of Object

var jane = {
  name: 'Jane',
  describe: function () {
    return 'Person named ' + this.name;
  }
};

describe is a method; this refers to the current object, also called the
receiver of a method invocation

when property keys are identifiers, the dot operator is the most compact way
of accessing properties. For arbitrary names or computed keys, brackets []
are needed

jane.describe()

obj['some' + 'Property']

the bracket operator coerces its contents to a string:

obj[3+3]  // obj['6']

obj['myMethod']()

delete obj.property completely removes the direct property. Prototypes are
unaffected. However, delete may prevent engine optimizations, so should be
used sparingly

delete will return false only if the property is an own property, but cannot
be deleted. Otherwise it returns true. Inherited properties cannot be deleted

Object() will convert any value to an object:

empty parameter, undefined and null result in {}

called on an object, nothing is done

otherwise, it is like calling new Boolean(bool), new Number(num), and
new String(str)

to check if a value is an object:

function isObject(value) {
  return value === Object(value);
}

or new Object(obj) === obj

this is an implicit parameter of functions and methods

when in sloppy mode, normal functions` this refers to the global object,
window, in browsers

when in strict mode, this is undefined for normal functions

for methods, this refers to the object on which the method was invoked. The
value of this is called the receiver of the method call

since functions are objects, they have their own methods. We consider call(),
apply(), and bind() for the following object, jane:

var jane = {
  name: 'Jane',
  sayHelloTo: function (otherName) {
    'use strict';
    console.log(this.name + ' says hello to ' + otherName);
  }
};

Function.prototype.call(thisValue, arg1?, arg2?, ...). The following are
equivalent

jane.sayHelloTo('Tarzan');
jane.sayHelloTo.call(jane, 'Tarzan');
var func = jane.sayHelloTo;
func.call(jane, 'Tarzan');

for the second case, jane is repeated because call() does not know where the
function came from. Using this instead will refer to the global object.

jane.sayHelloTo.call(this, 'Tarzan');
is the same as
jane.sayHelloTo.call(window, 'Tarzan');

Function.prototype.apply(thisValue, argArray). The following are equivalent:

jane.sayHelloTo('Tarzan');
jane.sayHelloTo.apply(jane, ['Tarzan']);
var func = jane.sayHelloTo;
func.apply(jane, ['Tarzan']);

Function.prototype.bind(thisValue, arg1?, ... argN?) is for partial function
application. A new function calls the receiver of bind with arguments arg1 to
argN, followed by arguments of the new function.

function func() {
  console.log('this: '+this);
  console.log('arguments: '+Array.prototype.slice.call(arguments));
}
var bound = func.bind('abcde', 1, 2);

the following are equivalent:

jane.sayHelloTo('Tarzan');

var func1 = jane.sayHelloTo.bind(jane);
func1('Tarzan');

var func2 = jane.sayHelloTo.bind(jane, 'Tarzan');
func2();

