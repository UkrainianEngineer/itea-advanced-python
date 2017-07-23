$(document).ready(function() {
    var options = {
        url: function (phrase) {
            return "/travel_app/cities?search=" + phrase;
        },

        getValue: "title",

        list: {
            match: {
                enabled: false
            }
        }
    };
    $("#desired-location").easyAutocomplete(options);
    $("#search-city").easyAutocomplete(options);
});


