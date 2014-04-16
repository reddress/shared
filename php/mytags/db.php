<?php

$dbh = new PDO('mysql:host=mysql1.alwaysdata.com;dbname=freezoo_mytags',"freezoo","123abc!") or die("Could not connect to tags");
$dbh->exec("SET NAMES 'utf8'");
$dbh->exec("SET CHARACTER SET 'utf8'");

?>