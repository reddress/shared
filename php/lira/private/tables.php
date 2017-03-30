<?php

$lira_tables = [

    ["name" => "user",
     "sql" => "
CREATE TABLE user
(id INTEGER NOT NULL AUTO_INCREMENT,
username VARCHAR(64) NOT NULL,
password VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
CONSTRAINT pk_user PRIMARY KEY (id),
CONSTRAINT uk_user_username UNIQUE KEY (username))
ENGINE=InnoDB"],

    ["name" => "currency",
     "sql" => "
CREATE TABLE currency
(id INTEGER NOT NULL AUTO_INCREMENT,
code CHAR(3) NOT NULL,
symbol VARCHAR(8) NOT NULL,
name VARCHAR(40) NOT NULL,
cents TINYINT NOT NULL,
CONSTRAINT pk_currency PRIMARY KEY (id),
CONSTRAINT uk_currency_code UNIQUE KEY (code))
ENGINE=InnoDB"],

    ["name" => "account_type",
     "sql" => "
CREATE TABLE account_type
(id INTEGER NOT NULL AUTO_INCREMENT,
user_id INTEGER NOT NULL,
name VARCHAR(64) NOT NULL,
sign TINYINT NOT NULL,
CONSTRAINT pk_account_type PRIMARY KEY (id),
CONSTRAINT fk_account_type_user FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE,
CONSTRAINT uk_account_type_user_name UNIQUE KEY (user_id, name))
ENGINE=InnoDB"],
    
    ["name" => "account",
     "sql" => "
CREATE TABLE account
(id INTEGER NOT NULL AUTO_INCREMENT,
user_id INTEGER NOT NULL,
account_type_id INTEGER,
name VARCHAR(80) NOT NULL,
CONSTRAINT pk_account PRIMARY KEY (id),
CONSTRAINT fk_account_user FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE,
CONSTRAINT fk_account_account_type FOREIGN KEY (account_type_id) REFERENCES account_type (id) ON DELETE SET NULL,
CONSTRAINT uk_account_user_name UNIQUE KEY (user_id, name))
ENGINE=InnoDB"],

    ["name" => "account_group",
     "sql" => "
CREATE TABLE account_group
(id INTEGER NOT NULL AUTO_INCREMENT,
user_id INTEGER NOT NULL,
name VARCHAR(80) NOT NULL,
CONSTRAINT pk_account_group PRIMARY KEY (id),
CONSTRAINT fk_account_group_user FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE)
ENGINE=InnoDB"],
    
    ["name" => "account_group_assoc",
     "sql" => "
CREATE TABLE account_group_assoc
(account_group_id INTEGER NOT NULL,
account_id INTEGER NOT NULL,
CONSTRAINT pk_account_group_assoc PRIMARY KEY (account_group_id, account_id),
CONSTRAINT fk_account_group_assoc_account_group FOREIGN KEY (account_group_id) REFERENCES account_group (id) ON DELETE CASCADE,
CONSTRAINT fk_account_group_assoc_account FOREIGN KEY (account_id) REFERENCES account (id) ON DELETE CASCADE)
ENGINE=InnoDB"],

    ["name" => "transaction",
     "sql" => "
CREATE TABLE transaction
(id INTEGER NOT NULL AUTO_INCREMENT,
user_id INTEGER NOT NULL,
description VARCHAR(255) NOT NULL,
currency_id INTEGER NOT NULL,
amount INTEGER NOT NULL,
debit INTEGER,
credit INTEGER,
created DATETIME NOT NULL,
CONSTRAINT pk_transaction PRIMARY KEY (id),
CONSTRAINT fk_transaction_user FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE,
CONSTRAINT fk_transaction_currency FOREIGN KEY (currency_id) REFERENCES currency (id),
CONSTRAINT fk_transaction_debit FOREIGN KEY (debit) REFERENCES account (id) ON DELETE SET NULL,
CONSTRAINT fk_transaction_credit FOREIGN KEY (credit) REFERENCES account (id) ON DELETE SET NULL)
ENGINE=InnoDB"],

    ["name" => "budget",
     "sql" => "
CREATE TABLE budget
(id INTEGER NOT NULL AUTO_INCREMENT,
account_id INTEGER NOT NULL,
currency_id INTEGER NOT NULL,
period_start DATE NOT NULL,
period_end DATE NOT NULL,
amount INTEGER NOT NULL,
CONSTRAINT pk_budget PRIMARY KEY (id),
CONSTRAINT fk_budget_account FOREIGN KEY (account_id) REFERENCES account (id) ON DELETE CASCADE,
CONSTRAINT fk_budget_currency FOREIGN KEY (currency_id) REFERENCES currency (id))
ENGINE=InnoDB"],

    ["name" => "currency_assoc",
     "sql" =>"
CREATE TABLE currency_assoc
(user_id INTEGER NOT NULL,
currency_id INTEGER NOT NULL,
position INTEGER,
CONSTRAINT pk_currency_assoc PRIMARY KEY (user_id, currency_id),
CONSTRAINT fk_currency_assoc_user FOREIGN KEY (user_id) REFERENCES user (id) ON DELETE CASCADE,
CONSTRAINT fk_currency_assoc_currency FOREIGN KEY (currency_id) REFERENCES currency (id))
ENGINE=InnoDB"],


    
    // end of tables
];
