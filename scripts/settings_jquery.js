$(document).ready(setup);
function setup() {
  $("input:checkbox[id=half_reminder]").click(function() {
    var half = $(this).prop('checked')
    console.log(half)
  });
  $("input:checkbox[id=third_reminder]").click(function() {
    var third = $(this).prop('checked')
    console.log(third)
  });
  $("input:checkbox[id=fourth_reminder]").click(function() {
    var fourth = $(this).prop('checked')
    console.log(fourth)
  });
  $("input:checkbox[id=no_reminder]").click(function() {
    var no_reminder = $(this).prop('checked')
    console.log(no_reminder)
  });
  $("input:radio[name=message_type]").click(function() {
    var message_type = $(this).val();
    console.log(message_type)
  });
  $("input:radio[name=snoozes]").click(function() {
    var snoozes = $(this).val();
    console.log(snoozes)
  });
}
function validateForm() {
  $('.form-field').each(function() {
    if ( $(this).val() === '' ) {
      return false
    }
    else {
      return true;
    }
  });
}
