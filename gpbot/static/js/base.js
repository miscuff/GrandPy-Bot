//Create the class GPMap

class GPMap{
    constructor(lat, lon){
    this.lat = lat;
    this.lon = lon;
    this.map = null;
    }

    initMap() {
        this.map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(this.lat, this.lon),
        zoom: 11,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: true,
        scrollwheel: false,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR
        },
        navigationControl: true,
        navigationControlOptions: {
            style: google.maps.NavigationControlStyle.ZOOM_PAN
        }
    });
}
};

let lat = 48.852969;
let lon = 2.349903;
GPMap = new GPMap(lat,lon);

window.onload = function() {
    GPMap.initMap();
};


$('#go_button').click(function(e) {
    e.preventDefault();
    let input_value = $('#input_user').val();
    $('#conversation').append('<div class="row"> <div class="col-lg-1"> <div id="image_enfant"> <img src="static/img/petit.png")> </div> </div> <div class="offset-lg-1 col-lg-9"> <div class="answer">' + input_value + '</div> </div> </div>');
    $('#conversation').scrollTop($('#conversation').prop("scrollHeight"));
});

/**
// init function for the google map api
function initMap(lat, lng, mapId){
    var location = {lat: lat, lng: lng};
    var map = new google.maps.Map(
        document.getElementById(mapId), {zoom: 10, center: location});
    var marker = new google.maps.Marker({position: location, map: map});
}
*//