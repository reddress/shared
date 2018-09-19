<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>ALEXIE Beans</title>
    </head>
    <body>

        <?php
        require_once("../util.php");

        session_start();

        // Check if user is already logged in
        if (isset($_SESSION['username'])) {  
	   require_once("header.php");
        ?>

	<br>
	<a href="accounts.php">Manage accounts</a><br><br><br>
        <a href="logout.php">Logout</a>
        <?php
        } else {
        ?>
            <form action="login.php" method="post">
                Please login or <a href="signup.php">sign up</a><br>
                <br>
                Username: <input type="text" name="username" autofocus><br>
                <input type="submit">
            </form>
        <?php
        }
        ?>
    </body>
</html>
