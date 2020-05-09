"use strict";

$(window).on("load", function () {
  /*------------------------------------
		Preloder
	--------------------------------------*/
  setTimeout(function () {
    $(".loader").fadeOut();
    $("#preloader").delay(400).fadeOut("slow");
  }, 1000);

  /*------------------------------------
		Alerts
		Automatically close alerts after 5s.
	--------------------------------------*/
  setTimeout(function () {
    $(".alert").alert("close");
  }, 5000);
});
