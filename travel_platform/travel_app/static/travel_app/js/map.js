map = new OpenLayers.Map("map");//инициализация карты
var mapnik = new OpenLayers.Layer.OSM();//создание слоя карты
map.addLayer(mapnik);//добавление слоя
map.setCenter(new OpenLayers.LonLat(24.04, 49.85) //(широта, долгота)
      .transform(
        new OpenLayers.Projection("EPSG:4326"), // переобразование в WGS 1984
        new OpenLayers.Projection("EPSG:900913") // переобразование проекции
      ), 10 // масштаб
    );
var layerMarkers = new OpenLayers.Layer.Markers("Markers");//создаем новый слой маркеров
map.addLayer(layerMarkers);//добавляем этот слой к карте
map.events.register('click', map, function (e) {
    layerMarkers.clearMarkers();
    var size = new OpenLayers.Size(30, 30);//размер картинки для маркера
    var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h); //смещение картинки для маркера
    var icon = new OpenLayers.Icon('maptag.png', size, offset);//картинка для маркера
    layerMarkers.addMarker(//добавляем маркер к слою маркеров
        new OpenLayers.Marker(map.getLonLatFromPixel(e.xy)), //координаты вставки маркера
        icon);//иконка маркера
	var lonlat = map.getLonLatFromPixel(e.xy).transform('EPSG:3857', 'EPSG:4326');
	alert("You clicked near " + (lonlat.lat.toFixed(4) + " N, " +
                              + lonlat.lon.toFixed(4) + " E"));
}); //добавление событие клика по карте
