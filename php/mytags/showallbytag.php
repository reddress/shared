<?php

include "header.php";
include "db.php";

// SOURCE: http://snipplr.com/view/19085/
function replace_urls($string, $rel = 'nofollow') {
    $host = "([a-z\d][-a-z\d]*[a-z\d]\.)+[a-z][-a-z\d]*[a-z]";
    $port = "(:\d{1,})?";
    $path = "(\/[^?<>\#\"\s]+)?";
    $query = "(\?[^<>\#\"\s]+)?";
    return preg_replace("#((ht|f)tps?:\/\/{$host}{$port}{$path}{$query})#i", "<a href=\"$1\" rel=\"{$rel}\" target=\"_blank\">$1</a>", $string);
}

$tagname = $_GET['tagname'];
$keyword = $_GET['keyword'];
$page = (int)$_GET['page'];

if ($page < 0 || !is_int($page)) {
  $page = 0;
}

$numperpage = 10;
$start = $page * $numperpage;

echo "<h3>$tagname</h3>";

if(trim($tagname) != "") {
  $tagname = "%|" . $tagname . "|%";
}
else {
  $tagname = "%";
}

if(trim($keyword) != "") {
  $keyword = "%" . $keyword . "%";
}
else {
  $keyword = "%";
}

$getPosts_sth = $dbh->prepare("SELECT * FROM `post` WHERE `tags` LIKE :tagname AND (`title` LIKE :keyword OR `content` LIKE :keyword) ORDER BY `date` DESC LIMIT $start, $numperpage");
$getPosts_sth->bindParam(':tagname', $tagname);
$getPosts_sth->bindParam(':keyword', $keyword);
$getPosts_sth->execute();
$getPosts_result = $getPosts_sth->fetchAll();

$prevPage = $page - 1;
$nextPage = $page + 1;
echo "&lt; <a href=\"showallbytag.php?tagname=${_GET['tagname']}&keyword=${_GET['keyword']}&page=$prevPage\">Prev page</a> | <a href=\"showallbytag.php?tagname=${_GET['tagname']}&keyword=${_GET['keyword']}&page=$nextPage\">Next page</a> &gt;";
echo "<br><br>";

foreach($getPosts_result as $row) {
  $rowTags = explode("|", $row['tags']);
  $tagLinks = "";
  $contentWithLinks = replace_urls($row['content']);
  for($i = 1; $i < count($rowTags) - 1; $i++) {
    $tagLinks .= '[<a class="taglink" href="showallbytag.php?tagname=' . $rowTags[$i] . '">' . $rowTags[$i] . "</a>] ";
  }

  echo <<<EOD
  <div>
    <span class="posttitle">${row['title']}</span>
    <a href="edit.php?id=${row['id']}">edit</a>
    <span class="date">${row['date']}</span>
    <pre>$contentWithLinks</pre>
    $tagLinks
    <br><br><hr>
  </div>
EOD;

}

echo "&lt; <a href=\"showallbytag.php?tagname=${_GET['tagname']}&keyword=${_GET['keyword']}&page=$prevPage\">Prev page</a> | <a href=\"showallbytag.php?tagname=${_GET['tagname']}&keyword=${_GET['keyword']}&page=$nextPage\">Next page</a> &gt;";


?>