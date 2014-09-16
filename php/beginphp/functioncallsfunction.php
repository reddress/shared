<?php

function double($x) {
    return $x * 2;
  }

function addone($x) {
    return $x + 1;
}

function callwith2($fn) {
    return call_user_func($fn, 2);
}

echo callwith2('addone');

?>
