<?php

$dbname = 'id2279115_my_database';
$dbuser = 'id2279115_matheusfterra';  
$dbpass = '2UYDf=V>4v[LPAU6'; 
$dbhost = 'localhost'; 

$connect = @mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

function getUserIpAddr(){
    if(!empty($_SERVER['HTTP_CLIENT_IP'])){
        //ip from share internet
        $ip = $_SERVER['HTTP_CLIENT_IP'];
    }elseif(!empty($_SERVER['HTTP_X_FORWARDED_FOR'])){
        //ip pass from proxy
        $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
    }else{
        $ip = $_SERVER['REMOTE_ADDR'];
    }
    return $ip;
}


function insert_data(){
	$connect=$GLOBALS['connect'];

	if(!$connect){
		echo "Error: " . mysqli_connect_error();
		exit();
	}else{
		echo "Connection Successful!<br>";
	}

	$ip=getUserIpAddr();
	echo "User Real IP= {$ip}<br>";
	$query = "INSERT INTO access (ip) VALUES ('$ip')";
	$result = mysqli_query($connect,$query);
	if(!$result){
		echo "Error: " . mysqli_connect_error();
		exit();
	}else{
		//echo "Insertion Success!";
		$query = "SELECT * FROM views";
		$result = mysqli_query($connect,$query);
		if ($result->num_rows > 0) {
	    	// output data of each row
	    	while($row = $result->fetch_assoc()) {
	        	$views=$row["views"];
	    	}
		} else {
		    echo "0 results";
		}
		$new_views=$views+1;
		$query = "UPDATE views SET views=$new_views WHERE id=1";
		$result = mysqli_query($connect,$query);
		if($result){
			echo"<br>Views: ".$new_views;
		}
	}
}
insert_data();
//$query = "INSERT INTO medicao (corrente, tensao, potencia) VALUES ('$corrente', '$tensao','$potencia')";
//$result = mysqli_query($connect,$query);

//echo "Insertion Success!";

?>
