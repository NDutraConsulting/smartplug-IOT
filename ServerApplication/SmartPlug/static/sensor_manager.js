function getTempData(){

	
	var e = document.getElementById("date_device_key");
	var strKey = e.options[e.selectedIndex].value;

	if(test_selection(strKey)){
		return;
	}

	strData = "date_device_key="+strKey;

	document.getElementById("sensor-content").innerHTML = "DEMO";

	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
  	if (this.readyState == 4 && this.status == 200) {
   	 document.getElementById("sensor-content").innerHTML = this.responseText;
  	}
	};
	
	xhttp.open("POST", "/get_temp", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send(strData);
}


function getLightData(){

	var e = document.getElementById("date_device_key");
	var strKey = e.options[e.selectedIndex].value;

	if(test_selection(strKey)){
		return;
	}

	strData = "date_device_key="+strKey;

	document.getElementById("sensor-content").innerHTML = "DEMO";

	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
  	if (this.readyState == 4 && this.status == 200) {
   	 document.getElementById("sensor-content").innerHTML = this.responseText;
  	}
	};
	
	xhttp.open("POST", "/get_light", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send(strData);

}


function getSoundData(){

	var e = document.getElementById("date_device_key");
	var strKey = e.options[e.selectedIndex].value;

	if(test_selection(strKey)){
		return;
	}

	strData = "date_device_key="+strKey;

	document.getElementById("sensor-content").innerHTML = "DEMO";

	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
  	if (this.readyState == 4 && this.status == 200) {
   	 document.getElementById("sensor-content").innerHTML = this.responseText;
  	}
	};
	
	xhttp.open("POST", "/get_sound", true);
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhttp.send(strData);

}

function test_selection(strKey){
	if( strKey == "none" ){
		
		alert("Please select a date device key!");
		return true;
	}
	return false;
	
}