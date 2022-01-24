<?php
$id = filter_input(INPUT_POST, 'idnum');
$lastname = filter_input(INPUT_POST, 'lname');
$firstname = filter_input(INPUT_POST, 'fname');
$mname = filter_input(INPUT_POST, 'minitial');
$address = filter_input(INPUT_POST, 'address');
$contact = filter_input(INPUT_POST, 'contact');
$email = filter_input(INPUT_POST, 'email');
$gender = filter_input(INPUT_POST, 'gender');
$age = filter_input(INPUT_POST, 'age');
$birthday = filter_input(INPUT_POST, 'bdate');
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

$sql = "INSERT INTO registration(idnum, surename, firstname, middle, address, contact, email, gender, age, birthday, password)
                            values ('$id','$lastname','$firstname','$mname','$address','$contact','$email','$gender','$age','$birthday','$password' )";
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