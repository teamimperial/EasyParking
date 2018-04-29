/**
 * Created by Antonina on 29.04.2018.
 */
var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 49.8382600, lng: 24.0232400},
        zoom: 13
    });
    var image = '/static/img/car.png';
    var parkings = [
        {
            position: {lat: 49.808653, lng: 24.015698},
            url: "plvilion.html"
        },
        {
            position: {lat: 49.850037, lng:  24.024078},
            url: "forum.html"
        }
    ];

    parkings.forEach(function(parkings) {
        var marker = new google.maps.Marker({
            position: parkings.position,
            icon: image,
            map: map,
            url: parkings.url
        });
        google.maps.event.addListener(marker, 'click', function() {
            window.location.href = this.url;
        });
    });
}