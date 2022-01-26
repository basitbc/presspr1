// Fa Bars
const barleft = document.querySelector(".barleft");
const navbar = document.querySelector(".navbar");
const links = document.querySelectorAll(".navbar li");


barleft.addEventListener("click", () => {
    navbar.classList.toggle("open");
});

// Sticky Navbar
$(document).ready(function () {
    $(window).scroll(function () {
        if (this.scrollY > 20) {
            $('.navbar1').addClass("sticky");
        } else {
            $('.navbar1').removeClass("sticky");
        }
        if (this.scrollY > 500) {
            $('.scroll-up-btn').addClass("show");
        } else {
            $('.scroll-up-btn').removeClass("show");
        }
    }
    )
});


// Hemburger

const menuBtn = document.querySelector('.menubtn');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if (!menuOpen) {
        menuBtn.classList.add('opn');
        menuOpen = true;
    } else {
        menuBtn.classList.remove('opn');
        menuOpen = false;
    }

});


// Blink Function of Back to Top
(function blink() {
    $('.blink_me').fadeOut(500).fadeIn(500, blink);
})();