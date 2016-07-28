 // Break Timer

// This function gets the amount of time remaining.
function getTimeRemaining(endtime) {
  // Difference between the ending time and the current time.
  var t = Date.parse(endtime) - Date.parse(new Date());
  var seconds = Math.floor((t / 1000) % 60);
  var minutes = Math.floor((t / 1000 / 60) % 60);
  return {
    'total': t,
    'minutes': minutes,
    'seconds': seconds
  };
}

// This function starts up a countdown clock.
function initializeClock(id, endtime, snooze_length, snoozes) {
  // The html element that the clock is shown within.
  var clock = document.getElementById(id);
  // Location of minutes.
  var minutesSpan = clock.querySelector('.minutes');
  // Location of seconds.
  var secondsSpan = clock.querySelector('.seconds');
  // The amount of time between reminders.
  var reminder_separation = snooze_length;
  // The amount of reminders remaining.
  var reminders_remaining = snoozes;
  // Check if the user has gone over their initial time.
  var overtime = false;
  // The total amount of time that the user has gone over their limit.
  var total_time_over = 0;


  // This function updates the clock every second.
  function updateClock() {
    var t = getTimeRemaining(endtime);


    minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
    secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

    if (t.total <= 0) {
      clearInterval(timeinterval);
      if (reminders_remaining === 0) {
        alert("Alright! Time to get back to work!  Remember to take productive breaks!");
      }
      else if (reminders_remaining === 1) {
        alert("This is your final reminder! YOUR BREAK IS OVER!");
      }
      else {
        alert("Your break is over!");
      }
      runAlert();
    }
  }

  updateClock();
  var timeinterval = setInterval(updateClock, 1000);
}

function setreminder(deadline, reminder_type) {
  alert_deadline = deadline;
  reminder_point = reminder_type;
  if (reminder_point=="half"){
    setTimeout(function(){ alert("Your break is half way over!"); }, alert_deadline);
  }
  else if (reminder_point=="third") {
    setTimeout(function(){ alert("You only have a third of your break left!"); }, alert_deadline);
  }
  else if (reminder_point=="fourth"){
    setTimeout(function(){ alert("You only have a fourth of your break left!"); }, alert_deadline);
  }
  else {

  }
}

function breakTimer(inputminutes, snooze_length, snoozes) {
  var deadline = new Date(Date.parse(new Date()) + inputminutes * 60 * 1000);
  initializeClock('clockdiv', deadline, snooze_length, snoozes);
  var snooze = {
    half : false,
    third : false,
    fourth: true
  };

  if (snooze.half) {
      var deadline2 = inputminutes * 60 * 1000/2;
      setreminder(deadline2,"half");
  }
  if (snooze.third){
      var deadline3 = 2 * (inputminutes * 60 * 1000/3);
      setreminder(deadline3,"third");
  }
  if (snooze.fourth){
      var deadline4 = 3 * (inputminutes * 60 * 1000/4);
      setreminder(deadline4,"fourth");

  }
}

// The value here is the amount of minutes that the timer will run for.
