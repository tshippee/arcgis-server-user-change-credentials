/**
 * Created by joel5174 on 12/17/13.
 */

// submit handler for form
function submit_form () {

    // url of the rest endpoint created when publishing the Python tool
    var restUrl = 'http://gis1:6080/arcgis/rest/services/ChangeUserPassword/GPServer/Change%20User%20Password/execute'

    // extract data from form for posting in header
    var username = $("input#username").val();
    var password_old = $("input#old_password").val();
    var password_new = $("input#new_password").val();
    console.log('submit');

    // if there, remove the alert-danger class
    $("div.alert[class~='alert-danger']").removeClass('alert-danger');

    // set alert div to alert-info
    $("div.alert:not([class~='alert-info'])").addClass('alert-info');

    // single find for div.alert
    var $div_alert = $("div.alert");

    // add progress bar and message to alert div
    $div_alert.html(
        '<div class="progress progress-striped active">\n    <div class="progress-bar" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"\n         style="width: 100%">\n    </div>\n</div>\n<div>Submitting new credentials to server</div>\n'
    );

    // fade in the alert div
    $div_alert.fadeIn();

    // post to REST endpoint
//    $.post(restUrl, )
};

// use jquery validate to configure form validation
$("#update_username_form").validate({

    // apply rules to fields, most are required and the confirm field must match the new password
    rules: {
        username: "required",
        old_password: "required",
        new_password: "required",
        new_password_confirm: {
            equalTo: "#new_password"
        }
    },

    // custom messages for each field if failing validation
    messages: {
        username: "please enter your username",
        old_password: "please enter your current password",
        new_password: "please enter your new password",
        new_password_confirm: "please ensure your new passwords match"
    },

    // if the form fails validation
    invalidHandler: function (event, validator) {

        // get and store the number of invalid fields
        var errors = validator.numberOfInvalids();

        // if errors exist
        if (errors) {

            // create a variable for messages
            var message = errors == 1

                // if only one error, present this message
                ? 'One field is invalid. Please correct the error and resubmit.'

                // if multiple errors, present this message
                : 'There are ' + errors + ' invalid fields. Please correct the errors and resubmit.';

            // query the DOM for the alert div and save as a variable
            var $div_alert = $('div.alert');

            // populate the error message in the alert div
            $div_alert.html(message);

            // set class on alert box to alert-danger if it does not already exist
            $("div.alert:not([class~='alert-danger'])").addClass('alert-danger');
            $("div.panel:not([class~='panel-danger'])").addClass('panel-danger');

            // fade in the alert div
            $div_alert.fadeIn();

        } else {

            // if the form is valid, fade the alert div out if it is not already hidden
            $('div.alert').fadeOut();

            // remove the alert-danger class
            $("div.alert[class~='alert-danger']").removeClass('alert-danger');
            $("div.panel[class~='panel-danger']").remoteClass('panel-danger');
        }
    },

    submitHandler: submit_form()

    // tag fields as errors when invalid
//    showErrors: function(errorMap, errorList) {
//        for (var error in errorList) {
//            console.log(error['element']);
////            errorElement.element.parent('div.form-group').addClass('has-error');
//        }
//    }
});
