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

  /*------------------------------------
		AJAX Requests
	--------------------------------------*/
  $("a.checkin").click(function (e) {
    e.preventDefault();

    const URL = $("a.checkin").data("url");

    $.get(URL, function (data) {
      $("#modal").modal("show");
      $(".modal-content").html(data);
    })
      .done(function () {
        console.log("done");
        checkin();
      })
      .fail(function () {
        console.log("error");
      });
    //
  });
});

function checkin() {
  $("#checkin-btn").click(function (e) {
    const URL = $("#checkin-btn").data("url");
    let checkout_ids = [];

    $.each($(".return-item-checkbox:checked"), function () {
      checkout_ids.push($(this).val());
    });

    let data = {
      checkout_ids: checkout_ids.join(),
    };

    if (data.checkout_ids.length === 0) {
      $("#modal").modal("hide");
      return;
    }

    $.get(
      URL,
      data,
      function (data) {
        $("#modal").modal("hide");
        // $(".modal-content").html(data);
      },
      "json"
    )
      .done(function () {
        console.log("done");
      })
      .fail(function () {
        console.log("error");
      });
  });
}
