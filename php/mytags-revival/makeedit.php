<?php

// include "header.php";
include "db.php";

$tag_stmt = "SELECT * FROM `tag`";
$taglist = "|";

for($i = 1; $i <= 5; $i++) {
  $tag = trim($_POST['tag'.$i]);
  if($tag != "") {
    $addTag = true;

    $tag_sth = $dbh->query($tag_stmt);
    foreach($tag_sth as $row) {
        // echo $row['name'], "\n";
      if($tag == $row['name']) {
        // echo "Match ${row['id']}";
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
    // echo "<br><br>";
  }
}

// trim tags
// convert tags to numbers


if(true) {
  $edit_sth = $dbh->prepare("UPDATE `post` SET `title` = :title, `content` = :content, `tags` = :tags WHERE `id` = :id");
    $edit_sth->bindParam(':title', $_POST['title']);
    $new_content = htmlspecialchars($_POST['content'], ENT_QUOTES);
  $edit_sth->bindParam(':content', $new_content);
  $edit_sth->bindParam(':tags', $taglist);
  $edit_sth->bindParam(':id', $_POST['id']);
  $edit_sth->execute();
}

$dbh = null;

// echo "<br>&lt; <a href='showpost.php?id={$_POST['id']}'>Back to post</a><br><br>";

// echo "Saved new content: " . $new_content;
// echo "<br><br>";
// echo str_replace("|", " ", $taglist);

header("Location: showpost.php?id={$_POST['id']}");


?>
