$(document).ready(setup);
function setup() {
  var isValid = true;
  $('#mainform').each(function() {
    if ( $(this).val() === '' )
        isValid = false;
  });
  return isValid;
}
