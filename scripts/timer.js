// Break Timer
var snoozes = 0;

function getTimeRemaining(endtime) {
  var t = Date.parse(endtime) - Date.parse(new Date());
  var seconds = Math.floor((t / 1000) % 60);
  var minutes = Math.floor((t / 1000 / 60) % 60);
  return {
    'total': t,
    'minutes': minutes,
    'seconds': seconds
  };
}

function initializeClock(id, endtime) {
  var clock = document.getElementById(id);
  var minutesSpan = clock.querySelector('.minutes');
  var secondsSpan = clock.querySelector('.seconds');

  function updateClock() {
    var t = getTimeRemaining(endtime);

    minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
    secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

    if (t.total <= 0) {
      clearInterval(timeinterval);
      alert("Your break is over!");
      // Rough concept of the snooze function
      var r = confirm("Do you want to extend your break?");
      if (r == true) {
        snoozes = snoozes + 1;
        breakTimer(1);
      } else {

}
    }
  }

  updateClock();
  var timeinterval = setInterval(updateClock, 1000);
}

function breakTimer(inputminutes) {
  var deadline = new Date(Date.parse(new Date()) + inputminutes * 60 * 1000);
  initializeClock('clockdiv', deadline);
}

// The value here is the amount of minutes that the timer will run for.
breakTimer(1);
