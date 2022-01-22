<?php
$id = filter_input(INPUT_POST, 'idnum');
$lastname = filter_input(INPUT_POST, 'surename');
$firstname = filter_input(INPUT_POST, 'firstname');
$mname = filter_input(INPUT_POST, 'middle');
$address = filter_input(INPUT_POST, 'address');
$contacts = filter_input(INPUT_POST, 'contact');
$email = filter_input(INPUT_POST, 'email');
$gender = filter_input(INPUT_POST, 'gender');
$age = filter_input(INPUT_POST, 'age');
$birthday = filter_input(INPUT_POST, 'birthday');
$password = filter_input(INPUT_POST, 'password');



$host = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "nstp";

// Create connection
$conn = new mysqli($host, $dbusername, $dbpassword, $dbname);




// Check connection
if (mysqli_connect_error()){
die('Connect Error ('. mysqli_connect_errno() .') '
. mysqli_connect_error());
}

else{

$sql = "INSERT INTO registration(idnum, lname, fname, minitial, address, cpnumber, email, gender, age, bdate, password)
                            values ('$id','$lastname','$firstname','$mname','$address','$contacts','$email','$gender','$age','$birthday','$password' )";
if ($conn->query($sql)){

header("Location: ../html/index.html");



}
else{
echo "Error: ". $sql ."
". $conn->error;
}
$conn->close();
}


?>