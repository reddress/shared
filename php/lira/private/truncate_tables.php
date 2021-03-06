<?php
include("../public/html_head.php");
?>

<body>
    <h1>Lira - Instalação de tabelas</h1>
    <pre><?php

         // DOES NOT SEEM TO WORK PROPERLY BECAUSE OF FOREIGN KEY CONSTRAINTS
         
         require("../public/db_connect.php");
         require("tables.php");

         $dbh = connect($db_credentials);
         
         $reverse_tables = array_reverse($lira_tables);
         foreach ($reverse_tables as $table) {
             $table_exists_sql = "
             SELECT table_name
             FROM information_schema.tables
             WHERE table_schema = :db_name
             AND table_name = :table_name";
             
             $table_exists_stmt = $dbh->prepare($table_exists_sql);
             $table_exists_stmt->execute([':db_name' => $db_credentials['db_name'],
                                          ':table_name' => $table['name']]);
             $table_exists_row = $table_exists_stmt->fetch();
             
             if ($table_exists_row) {
                 echo("Limpando tabela {$table['name']}\n");
                 ob_flush();
                 flush();                    

                 // Cannot bind to table name
                 // http://stackoverflow.com/questions/14553157/cant-drop-a-table-with-bindparam-using-pdo-and-php
                 // $stmt = $dbh->prepare("DROP TABLE :table_name");
                 // $stmt->execute([':table_name' => $table['name']]);
                 $dbh->exec("TRUNCATE TABLE {$table['name']}");
             } else {
                 echo("Tabela {$table['name']} não existe.\n");
             }
         }
         echo("\nOperação concluída."); 
         ?>
    </pre>
</body>
</html>
