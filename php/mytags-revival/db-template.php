<?php

// save real data in db.php


$dbh = new PDO('mysql:host=127.0.0.1;dbname=mytags',"root","") or die("Could not connect to tags");
$dbh->exec("SET NAMES 'utf8'");
$dbh->exec("SET CHARACTER SET 'utf8'");

?>
