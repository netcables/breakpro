$(document).ready(setup);
function setup() {
}
function validateForm() {
  var isValid = true;
  $('.form-field').each(function() {
    if ( $(this).val() === '' )
        isValid = false;
  });
  return isValid;
}
