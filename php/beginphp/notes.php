<!DOCTYPE html>
<html>
<body>
<pre>
<?php function nl() { echo "\n"; }
function println($arg) { echo $arg; echo "\n"; }
function h3($arg) { echo "<h3>" . $arg . "</h3>"; }?>

p. 35
the default value of an uninitialized variable is null

the four scalar data types are:
integer
float
string
boolean (true or false)

the two compound types are:
array (really, a map)
object

the two special types are:
resource (such as to a file or database)
null (meaning, a variable that does not contain any value)

<?php
h3("p. 36 Loose typing");
println(1/3 . " grams");
println("a " + "b");
?>

<?php
h3("Testing the type of a variable");
$myarray[] = 0;
$nothing = null;
$not_true = false;
println(gettype($nothing));
println(gettype(1/3));
println(gettype("abc"));
println(gettype($not_true));
println(gettype($myarray));
// println(gettype($undeclared));	
?>

p. 37 testing types
is_int(value), is_float(value), is_string(value), is_bool, array, object,
resource, null

p. 38
settype($variable, "string"); changes the type while preserving the contents
as much as possible. Types are passed as strings.

alternatively, cast the variable so that its value is treated as a specific
type. Unlike settype, the casted variable is unchanged.

echo (string) $variable;

the possible casts are (int), (integer), (float), (string), (bool), (boolean),
(array), and (object)

another way of casting is through these three functions:
intval("value", base) such as intval("11", 5) returns 6
floatval("value")
strval(value)

p. 40
an expression is anything that evaluates to a value, such as
$x + $y
$x
6
true
gettype($some_var)

p. 45
=== tests for equality and that the two sides are of the same type

these values are considered false:
false, 0, 0.0, " ", "0", an array with zero elements, null, empty XML tag

<?php
$x = 3 > 1;
println($x);
println(1 > 2);
?>

the operators and, or have lower precedences than && and ||.
In general, use && and || 

p. 49
define("MY_CONSTANT", value);  by convention, use uppercase

<?php
println(M_PI);
?>

p. 52
if can be combined with elseif and else

p. 53
script can be terminated with exit(int status);

p. 55
switch ($variable) {
	case "open":
		do_something();
		break;
	case "close":
		do_another();
		break;
	default:
		do_nothing();
}

<?php
h3("p. 56 ternary operator");
println((3 > 1) ? "yes" : "no");
?>

use parentheses around the conditional test for clarity

p. 63
in general, pre-computing the test condition in for loops is faster

p. 65
break can have an optional numeric argument that tells how many levels of
nesting to break out of. Breaking too many levels is an error.

<?php
h3("p. 75 Strings");
$my_multiline_string = "
line 1
line 2
";

println($my_multiline_string);
?>

surrond variables, array elements, and object properties with curly braces when
inserting them in strings

<?php

$docstr = <<<'ENDDOC'
heredoc strings parse variables
$my_heredoc = <<<END
String value
END;

nowdoc strings are used as-is
$my_nowdoc = <<<'END'
String value
END;
ENDDOC;

println(htmlspecialchars($docstr));
?>

p. 77
string length is strlen($s)

<?php
$s = "abcdef";
println(substr($s, -3, 3));
?>

p. 79
when using strpos, if the search string is found at the beginning of the test
string, 0 will be returned, which can be misinterpreted as false. So, an
explicit check is needed:
if (strpos($myString, "Hi") === false) { echo "not found"; }


</pre>
</body>
</html>
