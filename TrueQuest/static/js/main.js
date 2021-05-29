console.log("JS file is working");

function doWithThisElement(button) {
    button.className = 'hour-selector selected';
}


function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}
// // TODO: Remove
// dycalendar.draw({
//    target: '#dycalendar',
//    type: 'month',
//    dayformat: "full",
//    monthformat: "full",
//    highlighttargetdate: true,
//    prevnextbutton: 'show'
// });

// ------------------  Slider Start ---------------
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
// ------------------ Slider End ---------------

// Scroll Code

var scrollToElement = function(el, ms){
    var speed = (ms) ? ms : 600;
    $('html,body').animate({
        scrollTop: $(el).offset().top
    }, speed);
}

// specify id of element and optional scroll speed as arguments
// scrollToElement('#timeindicatordiv', 600);