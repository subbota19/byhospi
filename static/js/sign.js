$(document).on('submit', '#post-form', function (event) {
    event.preventDefault();
    let username = $('#username').val();
    let password = $('#password').val();
    let is_admin = $('#is_admin').prop('checked');
    if (username && password) {
        $.ajax({
            type: 'POST',
            url: '/registration/sign/',
            data: {
                username: username,
                password: password,
                is_admin: is_admin,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            success: function (data) {
                console.log(username);
                let map = ($(data).find('.by_map'));
                if ($(map).is('.by_map')) {
                    $('.container').html(map);
                }
                let user = ($(data).find('.user'))
                if (user.is('.user')) {
                    $('.error').html('incorrect password or username')
                    $('.container').html($('.user'))
                }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        })
    }
})
