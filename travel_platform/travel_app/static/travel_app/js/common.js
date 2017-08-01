$(function () {
    $("#search-city-form").submit(function (e) {
        e.preventDefault();
        var city = $("#search-city").val();
        var urlPart = $("#search-city-btn").data('urlPart');
        document.location.href = urlPart + city;
    })
});
