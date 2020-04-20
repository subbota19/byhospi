$(document).ready(function () {
    $('#description-form').submit(function () {
        let description = $('#description').val();
        $.ajax({
            type: 'POST',
            url: window.location.href.url,
            data: {
                description: description,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            success: function (data) {

            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        })
        return false
    })
    $('#comment-form').submit(function () {
        let comment = $('#comment').val();
        $.ajax({
            type: 'POST',
            url: window.location.href.url,
            data: {
                comment: comment,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            success: function (data) {
                let user = $('i:last').text();
                $('#comment').val('');
                $('.comments_win').append('<div class="comment">' + user + '<br>' + comment + '</div>')
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        })
        return false
    })
})
