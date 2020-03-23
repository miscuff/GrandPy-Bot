let lat = 0;
let lng = 0;

function initMap(){
    let map = new google.maps.Map(document.getElementById("map"), {
    center: new google.maps.LatLng(lat, lng),
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

$('#go_button').click(function(e) {
    e.preventDefault();
    let input_value = $('#input_user').val();
    $('#conversation').append('<div class="row"> <div class="col-1"> <div id="image_enfant"> <img src="static/img/petit.png")> </div> </div> <div class="offset-2 col-8"> <div class="answer">' + input_value + '</div> </div> </div>');
    $('#googlemap').css('visibility', 'visible');
     $.post("/grandpy/", { user_text: input_value }).done(function(response){
            if(response['answer']['location'] !== ""){
                // Initialize and display the map
               lat = response['answer']['location']['lat'];
               lng = response['answer']['location']['lng'];
               console.log(lat);
               console.log(lng);
               initMap();
            };
            if(response['answer']['story'] !== "" && response['answer']['url'] !== ""){
            // Display Story and URL
            let story = response['answer']['story']
            let url = response['answer']['url']
            $("#conversation").append('<div class="row"> <div class="col-1"> <div id="image_papy"> <img src="static/img/reponse.png")> </div> </div> <div class="offset-2 col-8"> <div class="answer"> '+ story +' Tu pourras trouver plus de renseignement en visitant la page suivante :<a href='+ url +' title="url_wiki">'+ url +' </a> </div> </div> </div>');
            };
    }).fail(function() {
        let error_value = "Papy est fatigué, il te répondra plus tard";
        $("#conversation").append('<div class="row"> <div class="col-1"> <div id="image_papy"> <img src="static/img/reponse.png")> </div> </div> <div class="offset-2 col-8"> <div class="answer">' + error_value + '</div> </div> </div>');
    });
});