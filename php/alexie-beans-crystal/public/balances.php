<?php

// SEARCH "MONTHLY" TO UPDATE BUDGET

require_once("header.php");
require_once("formatters.php");
?>
<form action="balances.php" method="get">
    <?php
    require_once("currency_date_form.php");
    ?>
</form>
<?php 

// initialize account sums
$account_balances = [];
$account_debits = [];
$account_credits = [];
$account_names = [];

// get all accounts
$all_accounts_sql = "select id, name from account where username = :username";
$stmt = $dbh->prepare($all_accounts_sql);
$stmt->execute([":username" => $_SESSION["username"]]);

foreach ($stmt as $row) {
    $account_balances[$row['id']] = 0;
    $account_debits[$row['id']] = 0;
    $account_credits[$row['id']] = 0;
    $account_names[$row['id']] = $row['name'];
}

// tables side-by-side, one for each account type
//
// first, get account types
$account_types_sql = "select id, name from account_type where username = :username";
$stmt = $dbh->prepare($account_types_sql);
$stmt->execute([":username" => $_SESSION["username"]]);

$account_types = [];
$account_type_totals = [];
$account_ref = [];  // hold account data, as a sublevel of account type

foreach ($stmt as $type_row) {
    $account_types[$type_row['id']] = $type_row['name'];
    $account_type_totals[$type_row['id']] = 0;
    $account_ref[$type_row['id']] = [];

    // then get names of accounts matching the type
    $accounts_of_type_sql = "select id, name from account
where username = :username
and account_type = :account_type
order by name";
    $account_stmt = $dbh->prepare($accounts_of_type_sql);
    $account_stmt->execute([":username" => $_SESSION["username"],
                            ":account_type" => $type_row['id']]);
    foreach($account_stmt as $account_row) {
        $account_ref[$type_row['id']][$account_row['id']] = $account_row['name'];
    }
}

// define common transaction criteria
$transactions_criteria_sql = "inner join account_type at on a.account_type = at.id
where t.currency = :currency
and t.created >= :start_created
and t.created <= :end_created
and a.username = :username
group by a.id, at.sign";

// FIX FOR Full_group_by error: group by a.id, at.sign

// then get debits multiplied by sign
$debits_of_account_sql = "select a.id, sum(t.amount) * at.sign as total
from account a
inner join transaction t on a.id = t.debit " . $transactions_criteria_sql;

$stmt = $dbh->prepare($debits_of_account_sql);
$stmt->execute([":currency" => $currency,
                ":start_created" => $start_datetime,
                ":end_created" => $end_datetime,
                ":username" => $_SESSION["username"]]);
foreach ($stmt as $row) {
    $account_debits[$row['id']] = $row['total'];
}

// then get credits multiplied by sign
$credits_of_account_sql = "select a.id, sum(t.amount) * at.sign * -1 as total
from account a
inner join transaction t on a.id = t.credit " . $transactions_criteria_sql;

$stmt = $dbh->prepare($credits_of_account_sql);
$stmt->execute([":currency" => $currency,
                ":start_created" => $start_datetime,
                ":end_created" => $end_datetime,
                ":username" => $_SESSION["username"]]);
foreach ($stmt as $row) {
    $account_credits[$row['id']] = $row['total'];
}

// sum debits and credits to get total
foreach ($account_balances as $id => $value) {
    $account_balances[$id] = $account_debits[$id] + $account_credits[$id];
}

// 9 feb 2016
// budget total
$budget_total = 0;
$budget_overdrawn = 0;

// USED IN COMPUTING AMOUNT NEEDED
$budgets_positive = 0;

// sort by account type
foreach ($account_types as $type_id => $type) {
    print("<table class='balances'>");
    print("<thead>
    <tr>
        <th colspan='2'>$type</th>
    </tr>
    </thead>");
    
    foreach ($account_ref[$type_id] as $account_id => $account_name) {
        // update type total
        $account_type_totals[$type_id] += $account_balances[$account_id];
        
        print("<tr>");
        print("<td>");
        print("<a href='account.php?id=$account_id&amp;currency=$currency&amp;start=$start_date&amp;end=$end_date'>$account_name</a></td>");
        print("<td class='right_align'>");
        if ($cents > 0) {
            print(separate_amount($account_balances[$account_id]));
        } else {
            print($account_balances[$account_id]);
        }

// personal patch to insert budget %
if ($type == "Expenses" && isset($_GET["start"])) {

    // hard-coded budget, lack of cents offsets percentage x 100
    $budget = ["acct_name" => 0,

// MONTHLY BUDGET (monthly budget)
"comm" => 30,  // 30 claro
"doac" => 0,
"elec" => 0,
"ent"  => 0, 
"exp"  => 0,
"groc" => 700,
"home" => 0,
"junk" => 67,
"livr" => 0,
"med"  => 400 + 150, // alex, meds, terapia lucia
"pres" => 0,
"rest" => 0,
"self" => 0,
"svc"  => 100 * 5, // val mondays
"tar"  => 46,
"tr"   => 307,  // mensal

];


    if (isset($budget[$account_name]) && $budget[$account_name] > 0) {
	$acct_budget = $budget[$account_name];
	$budget_percentage = ceil(ceil($account_balances[$account_id] / 100) / ($acct_budget / 100)) . "%";
	$budget_total += $acct_budget;
    } else {
	$acct_budget = 0;
	$budget_percentage = "";
    }
    $budget_left = round($acct_budget - ceil($account_balances[$account_id] / 100));
    if ($budget_left < 0) {
        $budget_overdrawn += $budget_left;
    }
    print(" / </td><td align='right'> $acct_budget = </td><td align='right'>$budget_percentage</td>");

    print("<td align='right'>");

print("&nbsp;");


if ($budget_left < 0) {
  print("<span style='color: red;'> (");
}

if ($budget_left > 0) {
  $budgets_positive = $budgets_positive + $budget_left;
}

$budget_left_display = $budget_left == 0 ? "" : abs($budget_left);

print($budget_left_display);

if ($budget_left < 0) {
  print(")</span>");
}

print("</td>");

} // end patch

        print("</td>");
        print("</tr>");
    }
    print("<tr><td colspan='2'><hr></td></tr>");
    print("<tr><td>Total</td><td>$currency_symbol ");
    if ($cents > 0) {
        print(separate_amount($account_type_totals[$type_id]));
    } else {
        print($account_type_totals[$type_id]);
    }

    // Budget total
    if ($type == "Expenses" && isset($_GET["start"])) {
	print(" / </td><td align='right'> $budget_total = </td>");
	$total_budget_percentage = ceil($account_type_totals[$type_id] / $budget_total);
	// PRINT REST %
	// print("<td align='right'>$total_budget_percentage%</td>");

// total of remaining budget (in currency)
$budget_total_left = round($budget_total - $account_type_totals[$type_id] / 100);

// if ($budget_total_left < 0) {

// PRINT HOW MUCH STILL NEEDED
// $amount_needed = abs($budget_overdrawn) + $budget_total - round($account_type_totals[$type_id] / 100);

$amount_needed = $budgets_positive;

print("<td align='right' style='color: #00F;' title='Amount needed to cover 100% of necessary expenses'>$amount_needed</td>");


print("<td align='right'>");


if ($budget_overdrawn < 0) {
   // print("<span style='color: red;'> (");
   print("<span style='color: purple;' title='100% of necessary expenses + current excess'> (");
}

// print(abs($budget_total_left));

// print(abs($budget_overdrawn));

// PRINT TOTAL + OVERDRAWN
print(abs($budget_overdrawn) + $budget_total);

// if ($budget_total_left < 0) {
if ($budget_overdrawn < 0) {
  print(")</span>");    
}

print("</td>");

print("<tr><td colspan='5' align='right' style='color: red;' title='Excess'>(" . abs($budget_overdrawn) . ")</td></tr>");

    }  // end budget total
    
    print("</table>");
}

require_once("footer.php");
?>

<script src="js/date_presets.js"></script>
