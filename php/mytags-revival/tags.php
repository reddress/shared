<?php 

include "header.php";
include "db.php";

$getTags_result = $dbh->query("SELECT `name` FROM `tag` ORDER BY `name`");

foreach($getTags_result as $row) {
  echo '<a class="taglink taglink_all" href="listbytitle.php?tagname=' . $row['name'] . '">' . $row['name'] . "</a> ";
}
