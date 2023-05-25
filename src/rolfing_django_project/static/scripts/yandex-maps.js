var query = document.getElementById('assoc_location').getAttribute('geolocation_query')

function init() {
    var myGeocoder = ymaps.geocode(query);
    myGeocoder.then(
    function (res) {
        var coords = res.geoObjects.get(0).geometry.getCoordinates();

        let map = new ymaps.Map('assoc_location', {
		    center: coords,
		    zoom: 16
	    });

	    let placemark = new ymaps.Placemark(coords, {}, {
		    iconLayout: 'default#image',
		    iconImageSize: [40, 40],
		    iconImageOffset: [-19, -44]
	    });

        map.controls.remove('geolocationControl');
        map.controls.remove('searchControl');
        map.controls.remove('trafficControl');
        map.controls.remove('typeSelector');
        map.controls.remove('fullscreenControl');
    //	map.controls.remove('zoomControl');
        map.controls.remove('rulerControl');
    //	map.behaviors.disable(['scrollZoom']);

	    map.geoObjects.add(placemark);
    });
};

ymaps.ready(init);