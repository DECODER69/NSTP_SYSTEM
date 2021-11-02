<?php
$id = filter_input(INPUT_POST, 'id-numbers');
$fname = filter_input(INPUT_POST, 'first_name');
$lname = filter_input(INPUT_POST, 'last_name');
$mname = filter_input(INPUT_POST, 'middle_initial');
$email = filter_input(INPUT_POST, 'email');
$bmonth = filter_input(INPUT_POST, 'months');
$bdate = filter_input(INPUT_POST, 'birthdate');
$byear = filter_input(INPUT_POST, 'birthyear');
$address = filter_input(INPUT_POST, 'address');
$gender = filter_input(INPUT_POST, 'gender');
$age = filter_input(INPUT_POST, 'age');
$contact = filter_input(INPUT_POST, 'contact_number');
$password = filter_input(INPUT_POST, 'password');
$confirm = filter_input(INPUT_POST, 'con-password');


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

$sql = "INSERT INTO registration(id_number, first_name, last_name, middle_initial, email_add, birth_month, birth_date, birth_year, address, gender, age, phone, password, password_confirmation)
                            values ('$id','$fname','$lname','$mname','$email','$bmonth','$bdate','$byear','$address','$gender','$age','$contact','$password','$confirm' )";
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