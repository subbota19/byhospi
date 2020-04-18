$(document).on('submit', '#post-form', function (event) {

    event.preventDefault();
    let username = $('#username').val();
    let email = $('#email').val();
    let password = $('#password').val();
    let status = $('#status option:selected').attr('value');

    if (username && email && password && email)
        $.ajax({
            type: 'POST',
            url: '/registration/login',
            data: {
                username: username,
                email: email,
                password: password,
                status: status,
                is_admin: $('#is_admin').prop('checked'),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action: 'post'
            },
            success: function (data) {
                let map = ($(data).find('.by_map'));
                if ($(map).is('.by_map')) {
                    $('.container').html($('.by_map'));
                }
                let user = ($(data).find('.user'))
                if (user.is('.user')) {
                    $('.error').html('user with this username or email already has used');
                    $('.container').html($('.user'));
                }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        })
})
