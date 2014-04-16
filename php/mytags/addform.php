<?php

include "header.php"

?>

    <form action="add.php" method="post">
      Author: <input name="user" value="1" readonly><br>
      Title: <input name="title"><br>
      <textarea name="content" rows="18" cols="80"></textarea>
      <br>
      Tags: (all lowercase)<br>
      <input name="tag1"><br>
      <input name="tag2"><br>
      <input name="tag3"><br>
      <input name="tag4"><br>
      <input name="tag5"><br>
      <input type="submit">
    </form>
  </body>
</html>
