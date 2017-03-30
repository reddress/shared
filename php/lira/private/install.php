<?php
include("../public/html_head.php");
?>

<body>
    <h1>Lira - Instalação de tabelas</h1>
    <pre><?php
         require("../public/db_connect.php");
         require("tables.php");

         $dbh = connect($db_credentials);
         
         function create_table($dbh, $db_name, $table_name, $table_sql) {
             // check table existence
             $table_exists_sql = "
             SELECT table_name
             FROM information_schema.tables
             WHERE table_schema = :db_name
             AND table_name = :table_name";
             
             $table_exists_stmt = $dbh->prepare($table_exists_sql);
             $table_exists_stmt->execute([':db_name' => $db_name,
                                          ':table_name' => $table_name]);
             $table_exists_row = $table_exists_stmt->fetch();
             if ($table_exists_row) {
                 echo("Tabela $table_name já existe.");
             } else {
                 echo("Criando tabela $table_name");
                 ob_flush();
                 flush();
                 $create_table_stmt = $dbh->exec($table_sql);
             }
             echo("\n");
         }

         foreach ($lira_tables as $table) {
             create_table($dbh, $db_credentials['db_name'], $table['name'], $table['sql']);
         }

         echo("\nTodas as tabelas foram criadas com sucesso.");
         ?>
    </pre>
</body>
</html>
