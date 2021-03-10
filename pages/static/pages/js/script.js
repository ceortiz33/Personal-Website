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
	
});
