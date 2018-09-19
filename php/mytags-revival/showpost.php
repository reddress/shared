<?php

include "header.php";
include "db.php";

// SOURCE: http://snipplr.com/view/19085/
function replace_urls($string, $rel = 'nofollow') {
    $host = "([a-z\d][-a-z\d]*[a-z\d]\.)+[a-z][-a-z\d]*[a-z]";
    $port = "(:\d{1,})?";
    // $path = "(\/[^?<>\#\"\s]+)?";
    $path = "(\/[^?<>\"\s]+)?";
    $query = "(\?[^<>\#\"\s]+)?";
    return preg_replace("#((ht|f)tps?:\/\/{$host}{$port}{$path}{$query})#i", "<a href=\"$1\" rel=\"{$rel}\" target=\"_blank\">$1</a>", $string);
}

if (isset($_GET['tagname'])) {
    $tagname_get = $_GET['tagname'];
} else {
    $tagname_get = "";
}

if (isset($_GET['keyword'])) {
    $keyword_get = $_GET['keyword'];
} else {
    $keyword_get = "";
}

if (isset($_GET['page'])) {
    $page = (int)$_GET['page'];
} else {
    $page = 0;
}

if ($page < 0 || !is_int($page)) {
  $page = 0;
}

// prev and next id numbers
$prevId = (int)$_GET['id'] - 1;
$nextId = (int)$_GET['id'] + 1;

echo <<<EOD
  <div>

<!-- prev/next post id links -->

<a href="showpost.php?id=$nextId">Newer</a> 
|
<a href="showpost.php?id=$prevId">Older</a>
</div>
EOD;

$numperpage = 3;
$start = $page * $numperpage;

echo "<h3>$tagname_get</h3>";

if(trim($tagname_get) != "") {
  $tagname = "%|" . $tagname_get . "|%";
}
else {
  $tagname = "%";
}

if(trim($keyword_get) != "") {
  $keyword = "%" . $keyword_get . "%";
}
else {
  $keyword = "%";
}

if (isset($_GET['month']) and isset($_GET['year'])) {
    $mo_start = (int) $_GET['month'];
    $yr_start = (int) $_GET['year'];

    $mo_raw = $mo_start;
    $yr_raw = $yr_start;
    
    if ($yr_start == 0 && $mo_start == 0) {
        // $date_start_sql = "2012-01-01";
        // $date_end_sql = "2099-01-01";
        $mo_start = 1;
        $yr_start = 2001;
        $mo_end = 1;
        $yr_end = 2099;
    } else if ($yr_start > 0 && $mo_start == 0) {
        $mo_start = 1;
        $mo_end = 1;
        $yr_end = $yr_start + 1;
    } else if ($yr_start == 0 && $mo_start > 0) {
        $yr_start = date("Y");
        $mo_end = $mo_start + 1;
        $yr_end = $yr_start;
    } else if ($mo_start == 12) {
        $yr_end += 1;
        $mo_end = 1;
    } else {
        $yr_end = $yr_start;
        $mo_end = $mo_start + 1;
    }

    $mo_start = str_pad($mo_start, 2, "0", STR_PAD_LEFT);
    $mo_end = str_pad($mo_end, 2, "0", STR_PAD_LEFT);

    $date_start_sql = "$yr_start-$mo_start-01";
    $date_end_sql = "$yr_end-$mo_end-01";
} else {
    $mo_raw = 0;
    $yr_raw = 0;
    
    $date_start_sql = "2001-01-01";
    $date_end_sql = "2099-01-01";
}

// echo("Dates: $date_start_sql to $date_end_sql <br><br>");

$getPosts_sth = $dbh->prepare("SELECT id, date_format(date, '%d %b %Y, %H:%i') as date_fmt, date, user, title, content, tags, dayname(date) as wkday FROM `post` WHERE id = :id");
$getPosts_sth->bindParam(':id', $_GET['id']);
$getPosts_sth->execute();
$getPosts_result = $getPosts_sth->fetchAll();

foreach($getPosts_result as $row) {
  $rowTags = explode("|", $row['tags']);
  $tagLinks = "";
  $contentWithLinks = replace_urls($row['content']);
  for($i = 1; $i < count($rowTags) - 1; $i++) {
    $tagLinks .= '<a class="taglink" href="listbytitle.php?tagname=' . $rowTags[$i] . '">' . $rowTags[$i] . "</a> ";
  }

    
  echo <<<EOD
  <div>
    <span class="date_sm">${row['wkday']}, ${row['date_fmt']}</span>
<br><br>
    <span class="posttitle">${row['title']}</span>
    <a href="edit.php?id=${row['id']}">edit</a>
    <pre>$contentWithLinks</pre>
    $tagLinks
    <br><br><hr>
  </div>
EOD;

}

?>
