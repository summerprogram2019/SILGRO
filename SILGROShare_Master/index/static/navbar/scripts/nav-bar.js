$(function(){
    $( "#start-time" ).datepicker();
    $( "#end-time" ).datepicker();
})

function initMapService() {
    //Map autocomplete code taken from https://developers.google.com/maps/documentation/javascript/examples/places-autocomplete
    var input = document.getElementById('nav-location');
    var autocomplete = new google.maps.places.Autocomplete(input);

    // Set the data fields to return when the user selects a place.
    autocomplete.setFields(
        ['address_components', 'geometry', 'icon', 'name']);

    var infowindow = new google.maps.InfoWindow();
    var infowindowContent = document.getElementById('infowindow-content');
    infowindow.setContent(infowindowContent);
}