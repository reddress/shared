<?php

require("../private/db_config.php");

// $db_credentials holds 'db_name'

function connect($db_credentials) {
    $dsn = "mysql:host={$db_credentials['host']};dbname={$db_credentials['db_name']};charset=utf8";

    try {
        $dbh = new PDO($dsn, $db_credentials['user'], $db_credentials['password']);
        $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $dbh->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        $dbh->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
        $dbh->exec("SET CHARACTER SET 'utf8'");
    } catch (PDOException $e) {
        die("DB connection error " . $e->getMessage());
    }
    return $dbh;
}
