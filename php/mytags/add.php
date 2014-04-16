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
  $add_stmt = $dbh->prepare("INSERT INTO post (date, user, title, content, tags) VALUES (NOW(), :user, :title, :content, :tags)");
  $add_stmt->bindParam(':user', $_POST['user']);
  $add_stmt->bindParam(':title', $_POST['title']);
  $add_stmt->bindParam(':content', htmlspecialchars($_POST['content'], ENT_QUOTES));
  $add_stmt->bindParam(':tags', $taglist);
  $add_stmt->execute();
}

$dbh = null;

?>