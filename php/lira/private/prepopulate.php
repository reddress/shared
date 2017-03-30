<?php
include("../public/html_head.php");
?>

<body>
    <pre><?php
         require("../public/db_connect.php");
         
         $dbh = connect($db_credentials);

         function prepopulate($dbh, $sql) {
             try {
                 $dbh->exec($sql);
                 echo("$sql : Sucesso\n\n");;
             } catch (PDOException $e) {
                 echo($e->getMessage());
                 echo("\n\n");
             }
         }

         prepopulate($dbh, "
INSERT INTO user (username, password, email)
VALUES
('heitor', 'secret', 'heitorchang@gmail.com'),
('tina', 'secret', 'tinacgh@gmail.com'),
('ken', 'secret', 'ken@tinacg.com')
");

         prepopulate($dbh, "
INSERT INTO currency (code, symbol, name, cents)
VALUES
('BRL', 'R$ ', 'Real (Brasil)', 2),
('USD', '$', 'Dólar (Estados Unidos)', 2),
('TWD', 'NT$', 'New Taiwan Dollar', 0) 
");

         prepopulate($dbh, "
INSERT INTO account_type (user_id, name, sign)
VALUES
(1, 'Assets', 1),
(1, 'Expenses', 1),
(1, 'Income', -1),
(2, 'Inventory', 1),
(2, 'World', -1),
(3, 'Assets', 1),
(3, 'Expenses', 1),
(3, 'Income', -1)
");

         prepopulate($dbh, "
INSERT INTO account (user_id, account_type_id, name)
VALUES
(1, 1, 'Checking'),
(1, 1, 'Wallet'),
(1, 2, 'Groceries'),
(1, 3, 'Salary'),
(1, 1, 'Savings')
");

         prepopulate($dbh, "
INSERT INTO account_group (user_id, name)
VALUES
(1, 'Bank')
");

         prepopulate($dbh, "
INSERT INTO account_group_assoc (account_group_id, account_id)
VALUES
(1, 1),
(1, 5)
");

         prepopulate($dbh, "
INSERT INTO transaction (user_id, description, currency_id, amount, debit, credit, created)
VALUES
(1, 'Feb salary', 1, 2000, 1, 4, '2017-02-05')
");

         prepopulate($dbh, "
INSERT INTO budget (account_id, currency_id, period_start, period_end, amount)
VALUES
(3, 1, '2017-03-01', '2017-03-31', 700)
");

         prepopulate($dbh, "
INSERT INTO currency_assoc (user_id, currency_id, position)
VALUES
(1, 1, 1)
");

         ?>
    </pre>
</body>
