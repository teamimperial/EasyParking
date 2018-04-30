/**
 * Created by Antonina on 29.04.2018.
 */
var map;

var Parkings = [
    {
        name: 'PLVision',
        lat: 49.808653,
        lng: 24.015698,
        url: "plvilion.html"
    },
    {
        name: 'Forum Lviv',
        lat: 49.850037,
        lng: 24.024078,
        url: "forum.html"
    }
];

var Locations;
$.ajax({
    url: 'https://my-json-server.typicode.com/podorozhnik/testapi/location',
    type: "get",
    dataType: "json",
    async: false,

    success: function(data) {
        Locations = data;
    }
});
console.log(Locations);

function addYourLocationButton(map, marker) {
    var controlDiv = document.createElement('div');

    var firstChild = document.createElement('button');
    firstChild.style.backgroundColor = '#fff';
    firstChild.style.border = 'none';
    firstChild.style.outline = 'none';
    firstChild.style.width = '28px';
    firstChild.style.height = '28px';
    firstChild.style.borderRadius = '2px';
    firstChild.style.boxShadow = '0 1px 4px rgba(0,0,0,0.3)';
    firstChild.style.cursor = 'pointer';
    firstChild.style.marginRight = '10px';
    firstChild.style.padding = '0px';
    firstChild.title = 'Your Location';
    controlDiv.appendChild(firstChild);

    var secondChild = document.createElement('div');
    secondChild.style.margin = '5px';
    secondChild.style.width = '18px';
    secondChild.style.height = '18px';
    secondChild.style.backgroundImage = 'url(https://maps.gstatic.com/tactile/mylocation/mylocation-sprite-1x.png)';
    secondChild.style.backgroundSize = '180px 18px';
    secondChild.style.backgroundPosition = '0px 0px';
    secondChild.style.backgroundRepeat = 'no-repeat';
    secondChild.id = 'you_location_img';
    firstChild.appendChild(secondChild);

    firstChild.addEventListener('click', function () {

        var imgX = '0';
        var animationInterval = setInterval(function () {
            if (imgX == '-18') imgX = '0';
            else imgX = '-18';
            $('#you_location_img').css('background-position', imgX + 'px 0px');
        }, 500);

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(position) {
                var pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                marker.setPosition(pos);
                map.setCenter(pos);
                clearInterval(animationInterval);
                $('#you_location_img').css('background-position', '-144px 0px');
            }, function() {
                console.log("error");
            });
        } else {
            // Browser doesn't support Geolocation
            console.log("Browser doesn't support Geolocation");
            clearInterval(animationInterval);
            $('#you_location_img').css('background-position', '0px 0px');
        }
    });
    controlDiv.index = 1;
    map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(controlDiv);
}

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 49.8382600, lng: 24.0232400},
        zoom: 13
    });

    var myloc = new google.maps.Marker({
        clickable: false,
        icon: new google.maps.MarkerImage('//maps.gstatic.com/mapfiles/mobile/mobileimgs2.png',
            new google.maps.Size(22,22),
            new google.maps.Point(0,18),
            new google.maps.Point(11,11)),
        shadow: null,
        zIndex: 999,
        map: map
    });
    addYourLocationButton(map, myloc);

    var image = '/static/img/car.png';

    // Add some markers to the map.
    var markers = Locations.map(function (location, i) {
        return new google.maps.Marker({
            position: { lat: location.lat, lng: location.lng},
            icon: new google.maps.MarkerImage(image,
                new google.maps.Size(32, 32),
                new google.maps.Point(0,0),
                new google.maps.Point(16,16)),
            url: location.url,
            title: location.name
        });
    });
    markers.forEach(function (marker) {
        google.maps.event.addListener(marker, 'click', function () {
            window.location.href = this.url;
        });
    });
    // Add a marker clusterer to manage the markers.
    var markerCluster = new MarkerClusterer(map, markers,
        {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}

