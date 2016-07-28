var new_modal = document.getElementById('New_modal');

// Get the button that opens the modal
var new_btn = document.getElementById("final_alert");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var okayButton = document.getElementById("ok");

// When the user clicks on the button, open the modal
function runAlert() {
    modal.style.display = "block";
    var snd = new Audio("alien_buzzer.wav"); // buffers automatically when created
    snd.play();
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == new_modal) {
        modal.style.display = "none";
    }
};

}
okayButton.onclick = function() {
  modal.style.display = "none";
}
