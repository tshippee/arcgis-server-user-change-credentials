/**
 * Created by joel5174 on 12/17/13.
 */
$("#update_username_form").validate({
    debug: true,
    rules: {
        username: "required",
        old_password: "required",
        new_password: "required",
        new_password_confirm: {
            equalTo: "#new_password"
        }
    },
    messages: {
        username: "please enter your username",
        old_password: "please enter your current password",
        new_password: "please enter your new password",
        new_password_confirm: "please ensure your new passwords match"
    },
    invalidHandler: function (event, validator) {
        var errors = validator.numberOfInvalids();
        if (errors) {
            var message = errors == 1
                ? 'One field is invalid. Please correct the error and resubmit.'
                : 'There are ' + errors + ' invalid fields. Please correct the errors and resubmit.';
            var $div_alert = $('div.alert');
            $div_alert.html(message);
            $div_alert.fadeIn();
        } else {
            $('div.alert').fadeOut();
        }
    }
});
$('#change_password_submit').click( function () {
    var restUrl = 'http://gis1:6080/arcgis/rest'
    $.post(url, 
        {
            'username': $('#username').val(),
            'old_pass': $('#old_password').val(), 
            'new_pass': $('#new_password').val()
        },
        success(data, textStatus, jqXHR),
        'dataType': 'json'
    );
});
