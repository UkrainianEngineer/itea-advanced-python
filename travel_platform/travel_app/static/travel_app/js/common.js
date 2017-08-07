$(function () {
    function redirectToCityUrl(elementId) {
        $(elementId).submit(function (e) {
            e.preventDefault();
            var city = $("#search-city").val();
            var urlPart = $("#search-city-btn").data('urlPart');
            document.location.href = urlPart + city;

        })

    }

    redirectToCityUrl("#search-attractions-form");
    redirectToCityUrl("#search-museums-form");
    redirectToCityUrl("#search-foursquare-form");

});