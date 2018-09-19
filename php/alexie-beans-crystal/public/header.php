<!doctype html>
<html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>ALEXIE Beans</title>
        <link href="css/alexie_beans.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        
        <?php
        require_once("../db.php");
        require_once("../util.php");

        date_default_timezone_set('America/Sao_Paulo');
        
        session_start();

        if (!isset($_SESSION['username'])) {
            println('Please <a href="login.php">log in</a>');
            exit(0);
        } else {
            print("<a href='index.php'>AB</a> ");
            print("(" . $_SESSION['username'] . ")");
        ?>
 <a href="balances.php">Balances (all time)</a>
<a href="balances.php?start=<?= (new DateTime("first day of this month"))->format("Y-m-d") ?>">(this month)</a> |
<a href="transactions.php">Add transaction</a> |
<a href="search.php">Search</a> |
<a href="acctgroups_all_and_this_month.php">Groups</a> |
<a href="adjust.html" target="_blank">Adjust balance</a> |
<a href="notes.html" target="_blank">Notes</a>
<hr>


<?php
      
   }
   ?>
