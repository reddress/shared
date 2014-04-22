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

remove whitespace with trim(), trimLeft(), and trimRight()

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

while apply may be used to call functions with array elements for parameters,
this approach does not work for constructors.

apply() can be simulated for constructors by first passing arguments to Date

new (Date.bind(null, 2011, 11, 24))

then, use apply() to hand an array to bind().

new (Function.prototype.bind.apply(Date, [null, 2011, 11, 24]))

var arr = [2011, 11, 24];
new (Function.prototype.bind.apply(Date, [null].concat(arr)))

when extracting a method, 'this' will be lost. In strict mode, you will get a
warning

bind() will ensure the connection to the original object is preserved

var counter = {
  count: 0,
  inc: function () {
    this.count++;
  }
}

var func = counter.inc.bind(counter);

with callbacks, bind() must be used too

function callIt(callback) {
  callback();
}

callIt(counter.inc.bind(counter));

when functions are nested, 'this' is shadowed. There are three ways around it

var that = this

bind()

this.friends.forEach(function (friend) {
  console.log(this.name);
}.bind(this));

when using forEach, provide 'this' as the second parameter

the prototype chain behaves as if it were a single object, therefore the value
of 'this' is the object where the property search began, not where it was
found

creating a new object with a given prototype:

Object.create(proto, propDescriptorObj?)

descriptors are verbose, so normally we create Object.create(Proto) then add
properties manually

Object.getPrototypeOf(obj) returns the prototype of obj

check prototype Object.prototype.isPrototypeOf(obj)

some JavaScript engines have __proto__, allowing direct access to get and set
the prototype

check for __proto__: Object.getPrototypeOf({ __proto__: null }) === null

setting and deleting ignores inheritance

get first object that has own property:

function getDefiningObject(obj, propKey) {
  obj = Object(obj)
  while (obj && !{}.hasOwnProperty.call(obj, propKey)) {
    obj = Object.getPrototypeOf(obj);
  }
  return obj;
}
 
iterating over and detecting properties are influenced by inheritance and
enumerability (an attribute)

Object.getOwnPropertyNames(obj) returns the keys of all own properties of obj

Object.keys(obj) returns the keys of all enumerable own properties of obj

to list all properties (own and inherited), there are two ways:

for (var v in object) {
  // statement
}

or implement your own function:

function getAllPropertyNames(obj) {
  var result = [];
  while (obj) {
    Array.prototype.push.apply(result, Object.getOwnPropertyNames(obj));
    obj = Object.getPrototypeOf(obj);
  }
  return result;
}

to check if a property exists (including inherited):

propKey in obj

for own properties (not inherited):

Object.prototype.hasOwnProperty(propKey)

or: {}.hasOwnProperty.call(obj, 'foo')
uses call because hasOwnProperty is called generically

directly calling obj.hasOwnProperty() is unsafe because hasOwnProperty may be
overridden

consider these objects:

var proto = Object.defineProperties({}, {
  protoEnumTrue: { value: 1, enumerable: true },
  protoEnumFalse: { value: 2, enumerable: false }
});
var obj = Object.create(proto, {
  objEnumTrue: { value: 10, enumerable: true },
  objEnumFalse: { value: 20, enumerable: false }
});

for (var x in obj) { console.log(x); }  // prints objEnumTrue and protoEnumTrue

Object.keys(obj)  // ['objEnumTrue']

Object.getOwnPropertyNames(obj)  // ['objEnumTrue', 'objEnumFalse']

only for-in and 'prop' in obj consider inheritance

the number of own properties of an object is Object.keys(obj).length

to iterate over own properties:

for (var key in obj) {
  if (Object.prototype.hasOwnProperty.call(obj, key)) {
    console.log(key);
  }
}

or

Object.keys(obj).forEach(function (key) {
  console.log(key);
});

you must use each key to obtain its value

accessors in an object literal:

var obj = {
  get foo() {
    return 'getter';
  },
  set foo(value) {
    console.log('setter: ' + value);
  }
};

obj.foo = 'bla';
obj.foo

property descriptors are an alternate way to achieve the above:

var obj = Object.create(
  Object.prototype, {
    foo: {
      get: function () {
        return 'getter';
      },
      set: function (value) {
        console.log('setter: ' + value);
      }
    }
  }
);

getters and setters are inherited from prototypes

property attributes are the atomic building blocks of properties

property descriptors are data structures for working programmatically with
attributes

attributes store property data and metadata

all properties have these attributes:

[[Enumerable]] (boolean) affects detection of the property

[[Configurable]] (boolean) if it is false, it cannot be deleted, and its
metadata cannot be altered. The exception is that you are allowed to change an
unconfigurable property from writable to read-only

arrays` property length has been writable and unconfigurable, to allow freezes

normal properties have:

[[Value]]

[[Writable]] (boolean) can this property be changed?

accessor specific attributes:

[[Get]] and [[Set]] are functions that are called on property gets and sets

a descriptor is a data structure:

{
  value: 123,
  writable: false,
  enumerable: true,
  configurable: false
}

such immutability can be achieved with an accessor:

{
  get: function () { return 123; },
  enumerable: true,
  configurable: false
}

when getting a property, all its attributes are returned as a descriptor

defining a nonexistent property with a descriptor creates a new property
with defaults dictated by what the attribute names mean. They are the opposite
of the values used when a property is created via assignment. To be clear,
all attributes should be explicitly stated

if a property already exists, update its attributes as specified by the
descriptor.

to get property attributes (returns undefined if propKey does not exist):

Object.getOwnPropertyDescriptor(obj, propKey)

to set property attributes (returns the modified object):

Object.defineProperty(obj, propKey, propDesc)

var obj = Object.defineProperty({}, 'foo', {
  value: 123,
  enumerable: true,
  writable: false,
  configurable: false
});

define multiple properties with an object holding property descriptors:

Object.defineProperties(obj, propDescObj)

var obj = Object.defineProperties({}, {
  foo: { value: 123, enumerable: true },
  bar: { value: 'abc', enumerable: true }
});

create an object with prototype proto and optional property descriptors:

Object.create(proto, propDescObj?)

to copy an object, the copy must have the same prototype and the same
properties with the same attributes as the original

function copyObject(orig) {
  var copy = Object.create(Object.getPrototypeOf(orig));
  copyOwnPropertiesFrom(copy, orig);
  return copy;
}

function copyOwnPropertiesFrom(target, source) {
  Object.getOwnPropertyNames(source).forEach(function (propKey) {
    var desc = Object.getOwnPropertyDescriptor(source, propKey);
    Object.defineProperty(target, propKey, desc);
  });
  return target;
};

defining a property via defineProperty() or defineProperties() ignores the
prototype chain

assigning to a property prop with = changes an existing property. If prop is
a setter, call that setter. If prop is read-only, throw an exception in
strict mode or do nothing in sloppy mode. If prop is own and writable, change
that value. Otherwise, there is no prop or it is inherited and writable. Then,
define an own property prop that is writable, configurable, and enumerable.

if obj inherits a property, prop, and it is not writable, then you cannot
assign to obj.prop. However, defining an own property circumvents this
protection. Object.defineProperty(obj, 'prop', { value: 'a' });

generally, properties created by the system are nonenumerable, while user
properties are. Object.keys() will return enumerable properties, and
Object.getOwnPropertyNames() returns keys of all own properties.

enumerability affects the for-in loop, Object.keys(), and JSON.stringify()

there are three levels to protect objects: preventing extensions, sealing, and
freezing.

Object.preventExtensions(obj);  // check with Object.isExtensible(obj)

Object.seal(obj); will prevent extensions and make all properties
unconfigurable. Check with Object.isSealed(obj)

Object.freeze(obj); makes all properties nonwritable and seals obj. Check:
Object.isFrozen(obj);

when in sloppy mode, failures are silent

protection is shallow, a mutable value of a property (such as an array) can be
changed. Also, an object obj has the prototype Object.prototype, which is
also mutable.

JavaScript constructors are like classes in other languages

objects created by a constructor are called instances

data (such as a person`s name) is instance-specific and stored in each
instance`s own properties

behavior is shared by all instances, through methods of the common prototype

a constructor is a function invoked by the new operator. By convention,
constructor names start with uppercase letters

function Person(name) {
  this.name = name;
}
Person.prototype.describe = function () {
  return 'Person named ' + this.name;
};
var jane = new Person("Jane");
jane.describe();

jane instanceof Person checks if an object is the instance of a constructor

the new operator does roughly:
function newOperator(Constr, args) {
  var thisValue = Object.create(Constr.prototype);
  var result = Constr.apply(thisValue, args);
  if (typeof result === 'object' && result !== null) {
    return result;
  }
  return thisValue;
}

prototype has two meanings in JavaScript:

an object can be the prototype of another object

var proto = {};
var obj = Object.create(proto);
Object.getPrototypeOf(obj) === proto  // true

prototype can be the value of the property 'prototype'

function C() {}
Object.getPrototypeOf(new C()) === C.prototype  // true

function Foo() {}
Object.getPrototypeOf(Foo) === Function.prototype  // true

by default, each function C contains an instance prototype object
C.prototype whose property constructor points back to C

function C() {}
C.prototype.constructor === C  // true

the constructor property is inherited by each instance

switch over direct instances of a given constructor:

switch (e.constructor) {
case SyntaxError:
  //
  break;
case CustomError:
  //
}

getting constructor`s name: f.constructor.name (not supported everywhere)

creating new objects with the same constructor of an existing object:

var y = new x,constructor();

SuperConstr.prototype.createCopy = function () {
  return new this.constructor(...);
};

avoid replacing C.prototype and only add properties to it:

C.prototype.method = function () { ... }

if it is replaced, manually assign the correct value to constructor:

C.prototype = {
  constructor: C,
  method1: function () { }
};

value instanceof Constr is the same as
Constr.prototype.isPrototypeOf(value)

primitives are never instanceof any object

prototypes of Object.create(null) and Object.prototype are not Object, but
null. However, typeof classifies them as objects

crossing realms (frames or windows) will prevent instanceof from working

there are functions like Array.isArray() that will work instead

also, use postMessage() or check the name of the constructor; but may not
work in all engines

use a prototype property to mark instances belonging to a type T:

value.isT(); but superconstructors return false

'T' in value; tag instances with a property whose key is 'T'

value.TYPE_NAME === 'T'

use strict mode to protect against forgetting new

a constructor can return whatever object

avoid prototype properties with initial values for instance properties

create an instance property on demand:

function Names(data) {
  if (data) this.data = data;
}
Names.prototype = {
  constructor: Names,
  get data() {
    Object.defineProperty(this, 'data', {
      value: [],
      enumerable: true,
      configurable: false,
      writable: false
    });
    return this.data;
  }
};

prototype properties that are not polymorphic should be replaced by variables

polymorphic prototype properties with immutable data can be used to tell them
apart.

there are three ways of storing private data:
  - in the environment of a constructor
  - in properties, with marked keys
  - in properties, with reified keys

also, global data can be kept private with IIFEs

the constructor`s environment is data storage that is independent of the
instance, though it is created at the same time as the instance

an instance can have three kinds of values associated with it:
  - public properties
  - private values (data and functions stored in the environment)
  - privileged methods (public methods in the instance, that have access to
                        private values)

prototype properties are usually methods

Constr.prototype.publicMethod = function () { };

instance properties usually hold data

function Constr(...) {
  this.publicData = ...;
}

private values are accessible only from inside the constructor
the constructor`s environment consists of the parameters and local variables

privileged methods are created in the constructor and added as instance
methods

function Constr() {
  var that = this;  // make accessible to private functions
  var privateData = ...;
  function privateFunction(...) {
    privateData = ...;
    that.publicData = ...;
  }

  this.privilegedMethod = function (...) {
    privateData = ...;
    this.publicData = ...;
  };
}

  in the privileged method, its this refers to object on which it was invoked,
that is, the outer this. So, we can access this`s properties without 'that'

one convention for marking property keys as private is using an underscore,
for example, _buffer

reifying a key is storing it in a variable:
var StringBuilder = function () {
  var KEY_BUFFER = '_StringBuilder_buffer';

  function StringBuilder() {
    this[KEY_BUFFER] = [];
  }
  return StringBuilder;
}();

an IIFE is wrapped around StringBuilder so that KEY_BUFFER stays local

private global data can be attached to a singleton object:

var obj = function () {  // open IIFE
  // public
  var self = {
    publicMethod: function () {
      privateData = ...;
    },
    publicData: ...
  };

  // private
  var privateData = ...;
  function privateFunction() {
    privateData = ...;
  }
  
  return self;
}();  // close IIFE

global data relevant only for a constructor and prototype methods can be
wrapped by an IIFE

var StringBuilder = function () {
  var KEY_BUFFER = ...;
  function StringBuilder() {
    this[KEY_BUFFER] = [];
  }
  StringBuilder.prototype = {
    // methods accessing this[KEY_BUFFER]
  };
  return StringBuilder;
}();

if global data is needed for a single method, it can stay private inside the
environment of an IIFE wrapped around the method

var obj = {
  method: function () {  // open IIFE
    var invocCount = 0;  // method-private
    return function () {
      invocCount++;
      return 'result';
    }
  }()  // close IIFE
};

to inherit instance properties:

function Sub(prop1, prop2) {
  Super.call(this, prop1);
  this.prop2 = prop2;
}

to inherit prototype properties, give Sub.prototype the prototype
Super.prototype

Sub.prototype = Object.create(Super.prototype);
Sub.prototype.constructor = Sub;  // needed because the original instance
                                  // prototype was replaced
Sub.prototype.methodB = ...;

subInstance instanceof Sub is the same as
Sub.prototype.isPrototypeOf(subInstance)

the home object of a method is the object that owns the method

to supercall a method, start the search in the prototype of the home object
and invoke it with the current 'this', because it must be able to access the
same instance properties

Sub.prototype.methodB = function (x, y) {
  var superResult = Super.prototype.methodB.call(this, x, y);
  return this.prop3 + ' ' + superResult;
}

to avoid hardcoding the superconstructor`s name, assign it to a property of
Sub: Sub._super = Super.prototype;

an utility function can connect the subprototype to the superprototype:

function subclasses(SubC, SuperC) {  // subclasses used here as a verb
  var subProto = Object.create(SuperC.prototype);
  copyOwnPropertiesFrom(subProto, SubC.prototype);
  SubC.prototype = subProto;
  SubC._super = SuperC.prototype;
};

example: Employee as a subconstructor of Person:

function Employee(name, title) {
  Person.call(this, name);
  this.title = title;
}
Employee.prototype = Object.create(Person.prototype);
Employee.prototype.constructor = Employee;
Employee.prototype.describe = function () {
  return Person.prototype.describe.call(this) + ' (' + this.title + ')';
};

using subclasses:

function Employee(name, title) {
  Employee._super.constructor.call(this, name);
  this.title = title;
}
Employee.prototype.describe = function() { ... };
subclasses(Employee, Person);

Object.prototype.toString() returns a string representation

Object.prototype.valueOf() is the preferred way of converting an object to a
number

Object.prototype.toLocaleString() returns a locale-specific string

Object.prototype.isPrototypeOf(obj) is true if the receiver is part of the
prototype chain of obj

Object.prototype.hasOwnProperty.call(obj, 'key'); checks for properties in
the object itself and not in its prototypes

Object.prototype.propertyIsEnumerable(propKey) looks only at own properties

instance prototype methods may be used generically:

function Wine(age) { this.age = age; }
Wine.prototype.incAge = function (years) { this.age += years; }

var chablis = new Wine(3);
chablis.incAge(1);  // chablis is the receiver of the method call, passed
                    // via this
is equivalent to Wine.prototype.incAge.call(chablis, 1);

so we can call Wine.prototype.incAge.call(john, 3)

Object.prototype and Array.prototype can be replaced by {} and [] when used
to generically call methods:

{}.hasOwnProperty.call(obj, 'propKey');
[].join.call(str, '-');

examples:

var arr1 = ['a','b'];
[].push.apply(arr1, ['c','d']);

[].join.call('abc', '-');

[].map.call('abc', function (x) { return x.toUpperCase(); });

you can also apply string methods to nonstrings (they are converted), or
array methods on fake arrays (objects with length and numbered indices)

array-like objects have indices and a length property, but none of the array
methods. Generic array methods can be used as a workaround

array-like objects include:
  - arguments
  - browser DOM node lists like document.getElementsBy*()
  - strings

to convert an array-like object to an array:

[].slice.call(obj);

to iterate over an array-like object, use a for loop

or [].forEach.call(obj, function (elem, i) {
  // print(i + ": " + elem);
});

generic array methods: concat, every, filter, forEach, indexOf, join,
lastIndexOf, map, pop, push, reduce, reduceRight, reverse, shift, slice,
some, sort, splice, toLocaleString, toString, unshift

generic: Date.prototype.toJSON

all Object.prototype methods are generic

generic string.methods: charAt, charCodeAt, concat, indexOf, lastIndexOf,
localeCompare, match, replace, search, slice, split, substring,
toLocaleLowerCase, toLocaleUpperCase, toLowerCase, toUpperCase, trim

when using objects as maps from strings to values, we must consider:
  - inheritance when reading properties: in will return inherited properties,
while hasOwnProperty looks only at the object itself
for-in will return inherited properties. To list enumerable own properties,
use obj.keys(). For all properties, use Object.getOwnPropertyNames()

  - overriding hasOwnProperty
  - overriding the special property __proto__

the dict pattern creates an object without a prototype:

var dict = Object.create(null);

ch18.html

array literal (trailing commas are ignored) and access:

var arr = ['a', 'b', 'c', ];
arr[0]
arr.length  // can be reduced to remove last elements
arr.push('d')  // append element

arrays are maps, not tuples (they can have holes)

arrays can have properties, becauee they are objects

avoid using Array() or new Array(), because calling it with one argument
produces an empty array with n holes, while using multiple arguments produces
the array with the given elements

multi-dimensional arrays must be nested: row[0][2] = "0";

indices are limited to 2^32 - 1, outside this range, the index is a string
property

the 'in' operator can be used to determine if an index exists in an array

delete will delete elements

length gives the highest index. To count actual elements, a function is needed

function countElements(arr) {
  var elemCount = 0;
  arr.forEach(function () {
    elemCount++;
  });
  return elemCount;
}

clearing an array by setting length to 0 affects all references, while
  assigning to an empty literal does not.

to create a hole, delete that element in the desired index

having undefined is different than having a hole. forEach() skips holes,
and while an existing undefined element will be used by forEach()

every() and some() skip holes

map()`s function skips holes, but the result will have holes

filter() eliminates holes

join() converts holes, undefined, and null to empty strings

sort() preserves holes

for-in correctly lists property keys (a superset of the indices)

Function.prototype.apply() turns holes into an argument whose value is
undefined.

Array.apply(null, Array(3))  // array with 3 undefineds

check if obj is an array: Array.isArray(obj), works for objects that cross
realms (windows or frames)

Array.prototype methods:

arr.shift() removes arr[0] and returns it

unshift(elem1, elem2, ...) prepends the given elements and returns new length

pop() removes the last element and returns it

push(elem1, elem2, ...) adds the given elements and returns new length

[].push.apply(arr1, arr2) appends arr2 to arr1

splice(start, deleteCount?, elem1?, elem2?...) deletes deleteCount elements
starting at start and inserts the given elements, returning the elements
removed. If start is negative, length is added to determine the start index.
  If deleteCount is omitted, all elements after start are deleted

reverse() is in place, and returns a reference to the original (modified)
array

sort(compareFunction?) converts values to strings then sorts them. To compare
numbers, compareFunction(a, b) must be given. It should return -1 if a < b,
0 if a === b, and 1 if a > b

function compareNumbers(a, b) {
  return a < b ? -1 : (a > b ? 1 : 0);
}

for comparing strings, use a.localeCompare(b);

or compare by object properties: a.name.localeCompare(b.name);

concatenate is nondestructive:

var arr = ['a', 'b'];
arr.concat('c', ['d', 'e']);  // ['a', 'b', 'c', 'd', 'e']

arr is unchanged

slice(begin?, end?) (nondestructive), copies from begin up to but not
including end

to copy up to the end, omit parameter 'end?', for negative indices, length
is added

slice() copies the entire array

Array.prototype.join(separator?) creates a string, separator defaults to ','

holes, undefineds, and nulls become empty strings

Array.prototype.indexOf(searchValue, startIndex?) returns the index of the
first occurrence, or -1 if nothing is found. === is used

[0,1,2,3,4,5].indexOf(3);  // 3

arr.lastIndexOf(searchElement, startIndex?) starts at given index and searches
backwards

array iteration uses functions; there are three kinds:
  - examination methods (observe content)
  - transformation methods (derive a new array)
  - reduction methods (compute a result)

arr.examinationMethod(function callback(element, index, array), thisValue?)
include forEach(), every(), and some()

var arr = ['apple', 'pear', 'orange'];
arr.forEach(function (elem) {
  console.log(elem);
});

arr.every(callback, thisValue?) returns true if callback is true for every
element. every() interprets an undefined returned as false

var squares = [0, 1, 4, 9, 16, 25];
squares.every(function (elem, index) {
  return elem === index * index;
});

function isEven(x) { return x % 2 === 0 }
[2, 4, 6].every(isEven);

function returnNothing(x) { };
['a', 'b'].every(returnNothing);

if the array is empty, every() returns true, and callback is not called
[].every(returnNothing);

arr.some(callback, thisValue?) returns true if callback is true of at least
one element. It is like asking "does there exist?"

if the array is empty, some() returns false

one drawback of forEach() is that it does not support break to end the loop

some() may be used for this purpose

function breakAtEmptyString(strArr) {
  var lastNonEmpty = "";
  strArr.some(function (elem) {
    if (elem.length === 0) {
      return true;  // has effect of break
    }
    console.log(elem);
    lastNonEmpty = elem;
    // implicit: return undefined, which is interpreted as false
  });
  return lastNonEmpty;
}
breakAtEmptyString(['a', 'b', '', 'd'])

transformation methods take an input array and produce an output array, with
  the callback controlling how the output is produced

callbacks have this signature: function callback(element, index, array) { }

there are two transformation methods: map(callback, thisValue?) and filter()

map creates a new array whose elements are the result of applying callback to
the input elements.

the output of filter contains only those input elements for which callback
returns true

Array.prototype.reduce(callback, initialValue?) and
Array.prototype.reduceRight(callback, initialValue?) are the reduction methods

for reducing, the callback has a different signature:

function callback(previousValue, currentElement, currentIndex, array) { }

previousValue is the value previously returned by the callback. When first
called, an explicit initialValue may be provided, making previousValue equal
to initialValue. Then, currentElement is the first array element
(for reduceRight, the last array element)

if no explicit initialValue has been provided, previousValue is the first
array element and currentElement, the second element. For reduceRight, they
become the last and second-to-last array elements.

function add(prev, cur) {
  return prev + cur;
}
[1, 2, 3].reduce(add);  // 6
[7].reduce(add);  // 7
[].reduce(add, 10);  // 10

reduceRight() works from right to left

reducing is like applying a binary operator n times:
(...(x_0 op x_1) op x2 ...) op x_n

avoid for-in when iterating over arrays. Use a simple for loop or forEach(),
every(), some(), map() or filter()

