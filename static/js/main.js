'use strict'

$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	setTimeout(function() {
		$(".loader").fadeOut(); 
		$("#preloader").delay(400).fadeOut("slow");
	}, 4000);
});