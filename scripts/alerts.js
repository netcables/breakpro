// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("alert");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var snoozeButton = document.getElementById("snooze");
var okayButton = document.getElementById("ok");
var snd;

// When the user clicks on the button, open the modal
function runAlert() {
    modal.style.display = "block";
    snd = new Audio("/sounds/annoying_alarm.wav"); // buffers automatically when created
    snd.play();
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
    snd.pause();
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        snd.pause();
    }
}
snoozeButton.onclick = function() {
  breakTimer(4, 1, 2);
  modal.style.display = "none";
  snd.pause();
}
okayButton.onclick = function() {
  modal.style.display = "none";
  snd.pause();
}
