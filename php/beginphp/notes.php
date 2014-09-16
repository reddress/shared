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
?>

</pre>
</body>
</html>