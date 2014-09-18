<?php

$starttime = microtime(true);

for ($num = 1; microtime(true) < $starttime + 0.01; $num *= 2) {
	echo "Current number: $num<br>";
}

echo "Time's up";
?>
