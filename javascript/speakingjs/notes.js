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

typeof is mainly used to describe primitives; it may return (all strings):
  - 'undefined', 'object', 'boolean', 'number', 'string', 'function'
  - or an engine-specific value
  - typeof null returns 'object', a bug that is not fixed for legacy reasons

x instanceof C returns true if the object x has been created by the
constructor C
  - [] instanceof Array  // true

NaN is an error value (not a number), while Infinity exceeds normal numbers
Infinity can be used as default values in looking for a minimum or maximum

