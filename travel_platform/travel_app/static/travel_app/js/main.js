$(document).ready(function () {
    $(".easy-autocomplete").removeAttr("style");
    $.getJSON("http://ip-api.com/json/?callback=?", function (data) {
        var city = data["city"];
        $("#initial-location").val(city).trigger('change');
    });

});

$(document).ready(function () {
    $(".common-img-link").css("opacity", 0.4);
    $(".choose > a").addClass("inactive-link");

    $("#initial-location").change(function () {
        var city = $(this).val();
        var links = {
            "#museums-link": 'museums',
            "#attractions-link": 'attractions',
            "#entertainment-link": 'entertainment',
            "#hotels-link": 'hotels',
            "#restaurants-link": 'hotels',
            "#transport-link": 'transport'
        };
        if (city) {
            $(".common-img-link").css("opacity", "");
            $(".choose > a").removeClass("inactive-link");
        }
        else {
            $(".choose > a").addClass("inactive-link");
            $(".common-img-link").css("opacity", 0.4);
        }

        Object.keys(links).forEach(function (objId) {
            if (city) {
                $(objId).attr("href", links[objId] + '/search?' + $.param({"search-city": city}))
            }
            else {
                $(objId).attr("href", 'javascript: {};')

            }
        });
    })

});
