 $(document).ready(function() {
  map = new OpenLayers.Map("map");
  var mapnik = new OpenLayers.Layer.OSM();
  map.addLayer(mapnik);
  map.setCenter(new OpenLayers.LonLat(24.04, 49.85)
        .transform(
          new OpenLayers.Projection("EPSG:4326"),
          new OpenLayers.Projection("EPSG:900913")
        ), 10
      );
  var layerMarkers = new OpenLayers.Layer.Markers("Markers");
  map.addLayer(layerMarkers);
  map.events.register('click', map, function (e) {
      layerMarkers.clearMarkers();
      var size = new OpenLayers.Size(30, 30);
      var offset = new OpenLayers.Pixel(-(size.w / 2), -size.h);
      var icon = new OpenLayers.Icon('maptag.png', size, offset);
      layerMarkers.addMarker(
          new OpenLayers.Marker(map.getLonLatFromPixel(e.xy)),
          icon);
    var lonlat = map.getLonLatFromPixel(e.xy).transform('EPSG:3857', 'EPSG:4326');

    $.ajax({
      dataType: "json",
      type: 'GET',
      url: '/travel_app/coord',
      data: {"lon": lonlat.lon.toFixed(6), "lat": lonlat.lat.toFixed(6)},
      success: function (response){
      $("#initial_location").val(response)
      },
    })
  });
});
