<?php

include "header.php";
include "db.php";

$tag_stmt = "SELECT * FROM `tag`";
$taglist = "|";

for($i = 1; $i <= 5; $i++) {
  $tag = trim($_POST['tag'.$i]);
  if($tag != "") {
    $addTag = true;

    $tag_sth = $dbh->query($tag_stmt);
    foreach($tag_sth as $row) {
      echo $row['name'], "\n";
      if($tag == $row['name']) {
        echo "Match ${row['id']}";
        $addTag = false;
        break;
      }
    }

    if($addTag) {
      $addTag_stmt = $dbh->prepare("INSERT INTO `tag` (name) VALUES (:name)");
      $addTag_stmt->bindParam(':name', $tag);
      $addTag_stmt->execute();
    }

    $taglist .= $tag . "|";
    echo "<br><br>";
  }
}

echo $taglist;

// trim tags
// convert tags to numbers


if(true) {
  $edit_sth = $dbh->prepare("UPDATE `post` SET `title` = :title, `content` = :content, `tags` = :tags WHERE `id` = :id");
  $edit_sth->bindParam(':title', $_POST['title']);
  $edit_sth->bindParam(':content', htmlspecialchars($_POST['content'], ENT_QUOTES));
  $edit_sth->bindParam(':tags', $taglist);
  $edit_sth->bindParam(':id', $_POST['id']);
  $edit_sth->execute();
}

$dbh = null;

?>