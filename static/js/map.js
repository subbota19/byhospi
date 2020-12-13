$(document).ready(function () {
    $('.part_map').hover(function () {
            let win = $('.description_window').css('display', 'block');

            win.html(
                "<h2 class='main_text'><wbr> " + $(this).attr('name') + " область </wbr></h2>" +
                "<h5 class='simple_text'><wbr>Население:" + $(this).attr('population') + " человек</wbr></h5>" +
                "<h5 class='simple_text'><wbr>Количество поликлиник:" + $(this).attr('count') + "</wbr></h5>" +
                "<h5 class='simple_text'><wbr>Нуждающихся в помощи:" + $(this).attr('help') + "</wbr></h5>" +
                "<a class='simple_text' id='region_href'>Официальная страница</a>")
            win.add($('a.simple_text').attr("href", $(this).attr('official_link')))

        },
        function () {
            $('.description_window').css('display', 'none');
        });
});


