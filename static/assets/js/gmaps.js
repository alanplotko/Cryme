var map;
var global_markers = [];
var infowindow = new google.maps.InfoWindow({});
var count = 0;
var input = document.getElementById("gmaps-input");
var searchBox = new google.maps.places.SearchBox(input);

function codeLatLng(latlng, marker) {
  var geocoder = new google.maps.Geocoder();
  geocoder.geocode({ 'latLng': latlng }, function (results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      var found = false;
      if (results[1]) {
        for(var i = 0; i < results[1].address_components.length; i++) {
          if(results[1].address_components[i].types[0] === "administrative_area_level_1") {
            if(results[1].address_components[i].short_name === "DC") {
              addMarker(marker);
              found = true;
              return;
            }
          }
        }
      }
      if(!found) {
        alert(marker.title + " is out of bounds!");
      }
    }
    else
    {
      alert("Error: Could not connect to Google Maps API. Try again later.")
    }
  });
}

function initialize() {
  var markers = [];
  geocoder = new google.maps.Geocoder();
  var latlng = new google.maps.LatLng(38.889931, -77.009003);
  var myOptions = {
    zoom: 15,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }

  map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
  var defaultBounds = new google.maps.LatLngBounds(
    new google.maps.LatLng(38.995817, -77.04106),
    new google.maps.LatLng(38.790399, -77.040591)
  );
  map.fitBounds(defaultBounds);

  // Create the search box and link it to the UI element.
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

  // Listen for the event fired when the user selects an item from the
  // pick list. Retrieve the matching places for that item.
  google.maps.event.addListener(searchBox, 'places_changed', function() {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }
    for (var i = 0, marker; marker = markers[i]; i++) {
      marker.setMap(null);
    }

    // For each place, get the icon, place name, and location.
    markers = [];
    for (var i = 0, place; place = places[i]; i++) {
      var image = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

      // Create a marker for each place.
      var marker = new google.maps.Marker({
        map: map,
        icon: image,
        title: place.name,
        position: place.geometry.location
      });

      var pos = new google.maps.LatLng(marker.position.lat(), marker.position.lng());
      codeLatLng(pos, marker);
    }
  });
}

function addMarker(marker) {
  var lat = marker.position.lat();
  var lng = marker.position.lng();
  var name = marker.title;
  var myLatlng = new google.maps.LatLng(lat, lng);
  var contentString = "<html><body><div><p class='gmaps-name'>" + name + "</p></div></body></html>";

  var marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      title: "Coordinates: " + lat + " , " + lng + " | Name: " + name
  });

  marker['infowindow'] = contentString;

  global_markers[count] = marker;

  google.maps.event.addListener(global_markers[count], 'click', function() {
      infowindow.setContent(this['infowindow']);
      infowindow.open(map, this);
  });
  count++;
}

google.maps.event.addDomListener(window, 'load', initialize);