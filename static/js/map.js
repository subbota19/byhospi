$(document).ready(function () {
    $('.part_map').hover(function () {
            $('.description_window').css('display', 'block');
            $('.description_window').html(
                "<h2 class='main_text'><wbr> " + $(this).attr('name') + " область </wbr></h2>" +
                "<h5 class='simple_text'><wbr>Население:" + $(this).attr('population') + " человек</wbr></h5>" +
                "<h5 class='simple_text'><wbr>Количество поликлиник:" + $(this).attr('count') + "</wbr></h5>" +
                "<h5 class='simple_text'><wbr>Нуждающихся в помощи:" + $(this).attr('help') + "</wbr></h5>"
            )
        },
        function () {
            $('.description_window').css('display', 'none');
        });
});


