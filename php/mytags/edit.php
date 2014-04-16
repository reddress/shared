<?php

include "header.php";
include "db.php";

$postId = $_GET['id'];

if($postId == "") {
  $postId = 1;
}

$getPost_sth = $dbh->prepare("SELECT * FROM `post` WHERE `id` = :id");
$getPost_sth->bindParam(':id', $postId);
$getPost_sth->execute();
$getPost_result = $getPost_sth->fetchAll();

foreach($getPost_result as $row) {
  $rowStr = substr($row['tags'], 1, -1);
  $tags = explode("|", $rowStr);
  echo <<<EOT
    <form action="makeedit.php" method="post">
      <input type="hidden" name="id" value="$postId">
      <b>Edit post</b> Author: <input name="user" value="1" readonly><br>
      Title: <input name="title" size="80" value="${row['title']}"><br>
      <textarea name="content" rows="18" cols="80">${row['content']}</textarea>
      <br>
      Tags: (all lowercase)<br>
      <input name="tag1" value="$tags[0]"><br>
      <input name="tag2" value="$tags[1]"><br>
      <input name="tag3" value="$tags[2]"><br>
      <input name="tag4" value="$tags[3]"><br>
      <input name="tag5" value="$tags[4]"><br>
      <input type="submit">
    </form>
  </body>
</html>
EOT;
}

?>