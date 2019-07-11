$(function initMap() {
    $( "#start-time" ).datepicker();
    $( "#end-time" ).datepicker();
    //Map autocomplete code taken from https://developers.google.com/maps/documentation/javascript/examples/places-autocomplete
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -33.8688, lng: 151.2195},
        zoom: 13
      });
  } );