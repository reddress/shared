<?php

include "header.php";

?>

    <form action="add.php" method="post">
      Author: <input name="user" value="1" readonly><br><br>
        When: <input id="whenInput" name="when"><br><br>
      Title: <input name="title" size="72" autofocus><br><br>
      <textarea name="content" rows="15" cols="80"></textarea>
      <br><br>
      Tags: (all lowercase)<br>
      <input name="tag1"><br>
      <input name="tag2"><br>
      <input name="tag3"><br>
      <input name="tag4"><br>
      <input name="tag5"><br>
      <input type="submit">
    </form>
    <script>
     function padZero(n) {
         if (n < 10) {
             return "0" + n.toString();
         } else {
             return n.toString();
         }
     }
     
     function nowTime() {
         var n = new Date();
         
         return n.getFullYear() + "-" + padZero(n.getMonth() + 1) + "-" + padZero(n.getDate()) + " " + padZero(n.getHours()) + ":" + padZero(n.getMinutes()) + ":" + padZero(n.getSeconds());
     }

     document.addEventListener("DOMContentLoaded", function() {
         document.getElementById("whenInput").value = nowTime();
     });
    </script>
  </body>
</html>
