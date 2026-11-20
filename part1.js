let x = document.getElementById("demo");

function myFunction() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success,error);
    } else {
        x.innerHTML = "Geolocation is not supported in this devise";
    }
}

function success(position){
    x.innerHTML="latitude:-"+ position.coords.speed
    +
    "<br>longitude:-"+ position.coords.longitude
}

function error(){
    alert("Geolocation is denied by User");
}

