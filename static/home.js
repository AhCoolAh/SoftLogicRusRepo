ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [55.76, 37.64],
            zoom: 7
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            // ObjectManager принимает те же опции, что и кластеризатор.
            gridSize: 64,
            clusterDisableClickZoom: true
        });

    // Чтобы задать опции одиночным объектам и кластерам,
    // обратимся к дочерним коллекциям ObjectManager.
    objectManager.objects.options.set('preset', 'islands#lightBlueCircleDotIcon');
    objectManager.clusters.options.set('preset', 'islands#invertedLightBlueClusterIcons');
    myMap.geoObjects.add(objectManager);

   $.ajax({
       url: "http://127.0.0.1:8000/points/",
       method: "GET",
       beforeSend: function() {
           $("#loader").show();
       },
       complete: function() {
            $("#loader").hide();
        },
   }).done(function(response) {
       console.log(response);
       objectManager.add(response.data);
   });
   

}