//Display Map

var lat = 48.852969;
var lon = 2.349903;
var map = null;
// Fonction d'initialisation de la carte
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(lat, lon),
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
window.onload = function(){
    // Fonction d'initialisation qui s'exécute lorsque le DOM est chargé
    initMap();
};


//Get the input from the user
function conversation(){
    var user_input = document.getElementById("user_input");
    var user_input_value = user_input.value;
    $("#conversation ul").append('<li class="question"><div class="speech-bubble">' + user_input_value + '</div></li>');
    user_input.value = "";
    $("#attente").show();
    $("#conversation").scrollTop($('#conversation').prop("scrollHeight"));

    $.post('/grandpy', {
        user_raw_text: user_input_value,

    }).done(function(response){
        $("#loading").hide();
        if(response['answer']['address'] !== ""){
            // Send address
            $("#conversation ul").append('<li class="answer"><div class="speech-bubble">' + response['answer']['address'] + '</div></li>');
            if(response['answer']['location'] !== ""){
                // Initialize and display the map
                var mapId = Math.random().toString(36).substring(2, 15);
                $("#conversation ul").append('<div class="answer"><div class="speech-bubble"><div id="' + mapId + '" class="map"></div></div></div>');
                initMap(
                    response['answer']['location']['lat'],
                    response['answer']['location']['lng'],
                    mapId
                );
            }
        }
        // Send extract
        if(response['answer']['extract'] !== "" && response['answer']['extract'] !== null){
            $("#conversation ul").append('<li class="answer"><div class="speech-bubble">' + response['answer']['extract']
                + ' [<a href='+ response['answer']['lien'] +'>En savoir plus sur Wikipedia</a>]</div></li>');
        }
        $("#chat").scrollTop($('#chat').prop("scrollHeight"));

    }).fail(function() {
        $("#chat ul").append('<li class="answer"><div class="speech-bubble">Grandpybot est fatigué, il répondra à tes questions une autre fois.</div></li>');
    });
}