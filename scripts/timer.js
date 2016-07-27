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
function initializeClock(id, endtime, reminderinterval, remindercount) {
  // The html element that the clock is shown within.
  var clock = document.getElementById(id);
  // Location of minutes.
  var minutesSpan = clock.querySelector('.minutes');
  // Location of seconds.
  var secondsSpan = clock.querySelector('.seconds');
  // The amount of time between reminders.
  var reminder_separation = reminderinterval;
  // The amount of reminders remaining.
  var reminders_remaining = remindercount;
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
        alert("Alright! Enjoy your work!  Remember to take productive breaks!");
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

function breakTimer(inputminutes, reminderinterval, remindercount) {
  var deadline = new Date(Date.parse(new Date()) + inputminutes * 60 * 1000);
  initializeClock('clockdiv', deadline, reminderinterval, remindercount);
}

// The value here is the amount of minutes that the timer will run for.
