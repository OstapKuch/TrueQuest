console.log("JS file is working");

function changePrice(element) {
    var c = element.options[element.selectedIndex].id
    var price_option = document.getElementById("quest_price" + c.substr(c.length - 1));
    price_option.innerHTML = (element.value + " ₴");
}

function changePriceRoom(element) {
    var price_option = document.getElementById("quest_price");
    price_option.innerHTML = (element.value + " ₴");
}


function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

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

function contact_data(data) {
    console.log(data);
    element = document.getElementById("input-feedback");
    element.setAttribute("value", data)
    // $(".input-feedback").attr("value", data)
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

// ------------------ Slider End ---------------

// Scroll Code

var scrollToElement = function (el, ms) {
    var speed = (ms) ? ms : 600;
    $('html,body').animate({
        scrollTop: $(el).offset().top
    }, speed);
}

// ------------------ Changing the hour selection buttons state
$(document).on('click', 'button', function () {
    $(this).addClass('hour-selector selected').siblings().removeClass('selected')
})