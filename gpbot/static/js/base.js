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
/**
let lat = 49.852969;
let lon = 2.349903;
GPMap = new GPMap(lat,lon);

window.onload = function() {
    GPMap.initMap();
};
**/

$('#go_button').click(function(e) {
    e.preventDefault();
    let input_value = $('#input_user').val();
    $('#conversation').append('<div class="row"> <div class="col-lg-1"> <div id="image_enfant"> <img src="static/img/petit.png")> </div> </div> <div class="offset-lg-1 col-lg-9"> <div class="answer">' + input_value + '</div> </div> </div>');
    $('#conversation').scrollTop($('#conversation').prop("scrollHeight"));

    $.post("/grandpy/", { 'answer': input_value }).done(function(response){
        //$("#loading").hide();
            // Send address
           // $("#chat ul").append('<li class="answer"><div class="speech-bubble">' + response['answer']['address'] + '</div></li>');
            if(response['answer']['location'] !== ""){
                // Initialize and display the map
                 lat = response['answer']['location']['lat'];
                 lon = response['answer']['location']['lon'];
                 Map_user = new map(lat, lon);
                 window.onclick = function() {
                    Map_user.initMap();
                                            };
            };
    }).fail(function() {
        error_value = "Papy est fatigué, il te répondra plus tard";
        $("#conversation").append('<div class="row"> <div class="col-lg-1"> <div id="image_papy"> <img src="static/img/reponse.png")> </div> </div> <div class="offset-lg-1 col-lg-9"> <div class="answer">' + error_value + '</div> </div> </div>');
    });
});