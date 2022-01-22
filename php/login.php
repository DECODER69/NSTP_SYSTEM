<?php



$host = "localhost";
$dbusername = "root";
$dbpassword = "";
$dbname = "nstp";

// Create connection
$conn = new mysqli($host, $dbusername, $dbpassword, $dbname);

if (isset($_POST['username']) && isset($_POST['password'])) {

	function test_input($data) {
	  $data = trim($data);
	  $data = stripslashes($data);
	  $data = htmlspecialchars($data);
	  return $data;
	}

	$username = test_input($_POST['username']);
	$password = test_input($_POST['password']);


	if (empty($username)) {
		echo"";
	}else if (empty($password)) {
		echo"";
	}else {

		// Hashing the password
		$password = md5($password);
        
        $sql = "SELECT * FROM registration WHERE idnum='$username' AND password='$password'";
        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) === 1) {
        	// the user name must be unique
        	$row = mysqli_fetch_assoc($result);
        	
        }else {
        	header("Location: ../index.php?error=Incorect User name or password");
        }

	}
	
}else {
	header("Location: ../index.php");



?>