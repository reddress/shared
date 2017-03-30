<?php
include("../public/html_head.php");
?>

<body>
    <pre><?php
         require("../public/db_connect.php");

         $dbh = connect($db_credentials);

         function exec_sql($dbh, $sql) {
             try {
                 echo($sql);
                 echo("\n");
                 $dbh->exec($sql);
             } catch (PDOException $e) {
                 echo("Erro: " . $e->getMessage() . "\n\n");
             }
         }

         exec_sql($dbh, "DELETE FROM user WHERE id = 1");
         ?>
    </pre>
</body>
