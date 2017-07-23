$(function () {
    $("#attractions-city").submit(function (e) {
        e.preventDefault();
        var city = $("#search-city").val();
        var urlPart = $("#search-city-btn").data('urlPart');
        document.location.href = urlPart + city;
    })
});