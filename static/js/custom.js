// PRELOADER

$(window).load(function(){
    $('.preloader').delay(1000).fadeOut("slow"); // set duration in brackets    
});

// HOME BACKGROUND SLIDESHOW
$(function(){
    jQuery(document).ready(function() {
		$('body').backstretch([
	 		 //"images/tm-bg-slide-1.jpg", 
	 		 //"images/tm-bg-slide-2.jpg",
			 //"images/tm-bg-slide-3.jpg"
			 Url1, Url2, Url3
	 			], 	{duration: 3200, fade: 1300});
		});
})