$(document).on('submit', '#cntform', function (e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '',
        data: {
            firstname: $('#fname').val(),
            lastname: $('#lname').val(),
            email: $('#email').val(),
            phone: $('#phone').val(),
            message: $('#message').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),

        },
        success: function (data) {
            $('h5').html(data);
            // alert("Successfully sent")
        }
    });
});
