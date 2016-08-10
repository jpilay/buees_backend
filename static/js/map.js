var markers = [];
var bus_stops = [];
var results = [];
var route_selected = "";
var map;

// Remove all markers on the map
function removeMarkers(points) {
  for (var i in points) {
      points[i].setMap(null);
  }
  points = []
}

//Marking my location on the map
function markerLocation(position) {

  var latCurrent = position.coords.latitude;
  var lonCurrent = position.coords.longitude;
  var location = new google.maps.LatLng(latCurrent, lonCurrent);
  var mapOptions = {
    center: new google.maps.LatLng(latCurrent,lonCurrent),
    zoom: 13
  };
  map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
  var marker = new google.maps.Marker({
    map: map,
    position: location,
    title: "This is your location",
    icon: "img/mi_ubicacion.png'",
    animation: google.maps.Animation.DROP
  });
}

// Show error getting location
function showError() {
  alert("Conexión GPS desactivada!");
}

// Getting location
function myLocation(){
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(markerLocation, showError);
  }else {
    alert("El navegador no soporta Geolocalización.");
  }
}

// Marking Bus Stops on the map
function markerBusStops(route){
  var img = "{% static 'img/stop" + route_selected.replace(/ /g,'') + ".png'";
  $.getJSON("/points/?stop_name=" + route + route_selected.replace(/ /g,'') +".json'",
    function(dataBusStops) {
      quantityBusStops = dataBusStops.length;
      for (var i = 0; i < quantityBusStops; i++) {
        var stop = dataBusStops[i].stop;
        var longitude = dataBusStops[i].lng;
        var latitude = dataBusStops[i].lat;
        var address = dataBusStops[i].dir;
        var hour = dataBusStops[i].hour;
        var currentLocation = new google.maps.LatLng(latitude, longitude);
        var title = stop + ': ' + address + '<br>' + 'Ruta: ' + route_selected;
        var marker = new google.maps.Marker({
          position: currentLocation,
          map: map,
          icon: img,
          animation: google.maps.Animation.DROP
        });
        var infoWindow = new google.maps.InfoWindow({
          content: title,
          maxWidth: 1000,
          maxHeight: 1000
        });
        marker.addListener('click', function(){
          infoWindow.open(map,marker);
        });
        busStops.push(marker);
      }
  });
}

// Marking Bus on the map
function markerBus(){
  var tmp = []
  removeMarkers(markers);

  $.getJSON("/bus_location/?bus_route=" + route_selected,
    function(result){
      if (!$.isEmptyObject(result)){
	      var plate = result.plate;
        var longitude = result.longitude;
        var latitude = result.latitude;
        var route = result.route;
        var currentLocation = new google.maps.LatLng(latitude, longitude);
        var img = "{% static 'img/buees' %}" + route.replace(/ /g,'') + ".png";
        var marker = new google.maps.Marker({
            position: currentLocation,
            map: map,
            icon: img,
            title: plate
        });
        markers.push(marker);
      }
  });
}

function intervalStart() {
  setInterval(markerBus, 3000);
}

function initialize() {
  var mapOptions = {
      center: new google.maps.LatLng("-2.181265", "-79.867201"),
      zoom: 13
  };

  map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

  myLocation();
  chooseRoute();
}

// Marking way stops
function wayStops() {
    removeMarkers(paradas);
    markerBusStops('ida');
}

// Marking return stops
function returnStops() {
    removeMarkers(paradas);
    markerBusStops('regreso');
}

google.maps.event.addDomListener(window, 'load', initialize);
$(document).ready(function(){});
