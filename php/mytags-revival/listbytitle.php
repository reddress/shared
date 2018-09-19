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

$numperpage = 7;
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

$getPosts_sth = $dbh->prepare("SELECT id, date_format(date, '%d %b %Y') as date_fmt, date, user, title, tags, dayname(date) as wkday FROM `post` WHERE `tags` LIKE :tagname AND (`title` LIKE :keyword OR `content` LIKE :keyword) AND date >= :date_start AND date < :date_end ORDER BY `date` DESC LIMIT $start, $numperpage");
$getPosts_sth->bindParam(':tagname', $tagname);
$getPosts_sth->bindParam(':keyword', $keyword);
$getPosts_sth->bindParam(':date_start', $date_start_sql);
$getPosts_sth->bindParam(':date_end', $date_end_sql);
$getPosts_sth->execute();
$getPosts_result = $getPosts_sth->fetchAll();

$prevPage = $page - 1;
$nextPage = $page + 1;

// count total pages

$countPosts_sth = $dbh->prepare("SELECT COUNT(*) as ct FROM `post` WHERE `tags` LIKE :tagname AND (`title` LIKE :keyword OR `content` LIKE :keyword) AND date >= :date_start AND date < :date_end");
$countPosts_sth->bindParam(':tagname', $tagname);
$countPosts_sth->bindParam(':keyword', $keyword);
$countPosts_sth->bindParam(':date_start', $date_start_sql);
$countPosts_sth->bindParam(':date_end', $date_end_sql);
$countPosts_sth->execute();
$countPosts_result = $countPosts_sth->fetch();
$totalPosts = $countPosts_result['ct'];


$currentPage = $page;

$totalPages = ceil($totalPosts / $numperpage);

$numPageLinks = 5;
$pagination = "";

$showParams = "listbytitle.php?tagname=$tagname_get&keyword=$keyword_get&month=$mo_raw&year=$yr_raw";

if ($currentPage > 0) {
    $pagination .= "<a href=\"$showParams&page=0\">Newest</a>&nbsp;";
    $pagination .= "<a href=\"$showParams&page=$prevPage\">Prev</a>&nbsp;";
} else {
    $pagination .= "Newest Prev ";
}

// insert "fixed location" Next
if ($currentPage < $totalPages - 1) {
  $pagination .= "<a href='$showParams&page=$nextPage'>Next</a> ";
} else {
  $pagination .= "Next ";    
}

$leftmostPage = max(0, $currentPage - $numPageLinks);
for ($i = $leftmostPage; $i < $currentPage; $i++) {
    $pagination .= "<a href=\"$showParams&page=$i\">" . ($i + 1) . "</a>&nbsp;";
}

$pagination .= "<span class='underline'>" . ($currentPage + 1) . "</span>";

$rightmostPage = min($totalPages, $currentPage + $numPageLinks + 1);

for ($i = $currentPage + 1; $i < $rightmostPage; $i++) {
  $pagination .= "&nbsp;<a href='$showParams&page=$i'>" . ($i + 1) . "</a>";
}

if ($currentPage < $totalPages - 1) {
  $pagination .= "&nbsp;<a href='$showParams&page=$nextPage'>Next</a>";
  $pagination .= "&nbsp;<a href='$showParams&page=" . ($totalPages - 1) . "'>Oldest</a>";
} else {
  $pagination .= "&nbsp;Next Oldest";
    
}

echo $pagination;
echo "<br><br>";

foreach($getPosts_result as $row) {
  $rowTags = explode("|", $row['tags']);
  $tagLinks = "";
  for($i = 1; $i < count($rowTags) - 1; $i++) {
    $tagLinks .= '<a class="taglink" href="listbytitle.php?tagname=' . $rowTags[$i] . '">' . $rowTags[$i] . "</a> ";
  }

    $short_wkday = substr($row['wkday'], 0, 3);
  echo <<<EOD
  <div>

    <span class="date_sm">$short_wkday, ${row['date_fmt']}</span>

<a href="showpost.php?id=${row['id']}" class="postlink">
    ${row['title']}
</a>
&nbsp;
    $tagLinks
<br><br>
  </div>
EOD;

}

echo $pagination;

?>
