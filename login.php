<?php
$uname = filter_input(INPUT_POST, 'usernames');
$pword = filter_input(INPUT_POST, 'passwords');



$host = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "webapp";

// Create connection
$conn = new mysqli($host, $dbusername, $dbpassword, $dbname);




// Check connection
if (mysqli_connect_error()){
die('Connect Error ('. mysqli_connect_errno() .') '
. mysqli_connect_error());
}

else{

$sql = "INSERT INTO login(user_name, password)
                            values ('$uname','$pword')";
if ($conn->query($sql)){
echo "New record is inserted sucessfully";
}
else{
echo "Error: ". $sql ."
". $conn->error;
}
$conn->close();
}


?>