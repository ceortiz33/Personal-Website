$(document).ready(function(){
	$(window).scroll(function(){
		(this.scrollY > 20) ? $('.navbar').addClass("sticky") : $('.navbar').removeClass("sticky");
		(this.scrollY > 500) ? $('.scroll-up-btn').addClass("show") : $('.scroll-up-btn').removeClass("show");

	});


	//Slide-up script
	$('.scroll-up-btn').click(function(){
		$('html').animate({scrollTop: 0});
	});

	//Toggle menu/navbar Script
	$('.menu-btn').click(function(){
		$('.navbar .menu').toggleClass("active");
		$('.menu-btn i').toggleClass("active");
	});

	// Typing Animation Script

	let typed = new Typed(".typing",
	 {strings: ["a Hacker", "a Developer", "an Engineer", "a Freelancer"],
	  typeSpeed: 100,
	  backSpeed: 60,
	  loop: true 
	 });
	let typed2 = new Typed(".typing-2",
	 {strings: ["a Hacker", "a Developer", "an Engineer", "a Freelancer"],
	  typeSpeed: 100,
	  backSpeed: 60,
	  loop: true 
	 });


	//owl Carousel Script
	$('.carousel').owlCarousel({
		margin: 20,
		loop: true,
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
