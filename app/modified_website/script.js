$(document).ready(function(){
    $(window).scroll(function(){
        // sticky navbar on scroll script
        if(this.scrollY > 20){
            $('.navbar').addClass("sticky");
        }else{
            $('.navbar').removeClass("sticky");
        }
        
        // scroll-up button show/hide script
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
        }else{
            $('.scroll-up-btn').removeClass("show");
        }
    });

// share on twitter
const myshareButton = document.getElementById("share-twitter");

myshareButton.addEventListener("click", () => {
  const twitterShareUrl = "https://twitter.com/intent/tweet";
  const shareText = encodeURIComponent("Check out this great work that we are doing!");
  const shareUrl = encodeURIComponent("http://example.com");
  const share = `${twitterShareUrl}?text=${shareText}&url=${shareUrl}`;
  window.open(share);
});

// share on facebook

const shareButton = document.getElementById("share-facebook");

shareButton.addEventListener("click", () => {
  const facebookShareUrl = "https://www.facebook.com/sharer/sharer.php";
  const shareUrl = encodeURIComponent("http://example.com");
  const share = `${facebookShareUrl}?u=${shareUrl}`;
  const shareTitle = encodeURIComponent("Check out this great work that we are doing!");
  window.open(share, "Facebook Share", "height=400,width=600");
});

// linkedIN share

const linkshareButton = document.getElementById("share-linkedin");

linkshareButton.addEventListener("click", () => {
    const linkedinShareUrl = "https://www.linkedin.com/sharing/share-offsite/";
    const shareUrl = encodeURIComponent("http://example.com");
    const shareTitle = encodeURIComponent("Check out this great work that we are doing!");
    const share = `${linkedinShareUrl}?url=${shareUrl}&title=${shareTitle}&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET`;
    window.open(share, "LinkedIn Share", "height=450,width=550,resizable,scrollbars=yes");
});



    // slide-up script
    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0});
        // removing smooth scroll on slide-up button click
        $('html').css("scrollBehavior", "auto");
    });

    $('.navbar .menu li a').click(function(){
        // applying again smooth scroll on menu items click
        $('html').css("scrollBehavior", "smooth");
    });

    // toggle menu/navbar script
    $('.menu-btn').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.menu-btn i').toggleClass("active");
    });

    // typing text animation script
    var typed = new Typed(".typing", {
        strings: ["Welcome!"," ","This is a Data-driven Modelling and Simulation Collaboration Tool!", " ", "This is where you can find tools to help you with the field!", " "],
        typeSpeed: 80,
        backSpeed: 60,
        loop: true
    });

    var typed = new Typed(".typing-2", {
        strings: [" Data.''", " ", " The new gold.''", " ", "We are Data-driven.''"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

    // owl carousel script
    $('.carousel').owlCarousel({
        margin: 20,
        loop: true,
        autoplay: true,
        autoplayTimeOut: 2000,
        autoplayHoverPause: true,
        responsive: {
            0:{
                items: 1,
                nav: false
            },
            600:{
                items: 2,
                nav: false
            },
            1000:{
                items: 3,
                nav: false
            }
        }
    });
});