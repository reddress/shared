<?php
// used as a shortcut

session_start();

$_SESSION['username'] = 'heitor';
header('Location: transactions.php');

?>
