$(document).ready(function () {
    $('.part_map').hover(function () {
            $('.description_window').css('display', 'block');
            $('.description_window').html("<h2 class='main_text'> " + $(this).attr('name') + "</h2>" +
                "<wbr>Население:" + $(this).attr('population') + "</wbr>")
        },
        function () {
            $('.description_window').css('display', 'none');
        });
});


