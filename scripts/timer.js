// Gets the remaining time of a timer
function getRemainingTime(endtime) {
  // The length of the timer in Milliseconds
  var total = endtime
  // Converts Milliseconds to Seconds
  var seconds = Math.floor((total/1000) % 60);
  // Converts Milliseconds to Minutes
  var minutes = Math.floor((total/1000/60) & 60);
  // Returns timer values
  return {
    'total': total;
    'minutes': minutes;
    'seconds': seconds;
  }
}

// Starts a new clock
function startClock(html_id, endtime){
  var clock = document.getElementBy(id);
  var timeinterval = setInterval(function(){
    car total = getRemainingTime(endtime);
    clock.innterHTML = 'Minutes:' + total.minutes + '<br>' +
    'Seconds:' + total.seconds;
    if(total.total <= 0){
      clearInterval(timeinterval);
    }
  }, 1000);
}

initializeClock('clockdiv', deadline);
