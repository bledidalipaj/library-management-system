"use strict";

/*------------------------------------
		Utilities
  --------------------------------------*/

const SPINNER = `
<tr>
  <td colspan="3">
    <div class="d-flex justify-content-center">
      <div class="spinner-border" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </div>
  </td>
</tr>
`;

function generateAvailableCopiesBadgeTemplate(numberOfAvailableCopies) {
  let template;
  if (numberOfAvailableCopies > 0) {
    template = `
    <div class="available-copies-badge bg-success" id="available-copies">
      <span title="Available copies">
        ${numberOfAvailableCopies}
      </span>
      <span class="sr-only">Available copies</span>
    </div>
    `;
  } else {
    template = `
    <div class="available-copies-badge bg-danger" id="available-copies">
      <span title="Available copies">0</span>
      <span class="sr-only">Available copies</span>
    </div>
    `;
  }

  return template;
}

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
    // $(".alert").alert("close");
    $("#messages-container").remove();
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
    const PK = $("#checkin-btn").data("pk");
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
        updateCheckoutHistory(PK);
        updateHolds(PK);
        updateAssetMetadata(PK);
      })
      .fail(function () {
        console.log("error");
      });
  });
}

function updateCheckoutHistory(pk) {
  const URL = `/checkout-history/${pk}`;
  let $checkoutHistoryTableBody = $("#checkout-history-table tbody");
  $checkoutHistoryTableBody.html(SPINNER);

  $.get(URL, function (data) {
    $checkoutHistoryTableBody.html(data);
  })
    .done(function () {
      console.log("done");
    })
    .fail(function () {
      console.log("error");
    });
}

function updateHolds(pk) {
  const URL = `/holds/${pk}`;
  let $holdsTableBody = $("#holds-table tbody");
  $holdsTableBody.html(SPINNER);

  $.get(URL, function (data) {
    $holdsTableBody.html(data);
  })
    .done(function () {
      console.log("done");
    })
    .fail(function () {
      console.log("error");
    });
}

function updateAssetMetadata(pk) {
  const URL = `/metadata/${pk}`;
  let $itemStatus = $("#item-status");
  let $availableCopies = $("#available-copies");

  $.get(URL, function (data) {
    // $holdsTableBody.html(data);
    console.log(data);
    $itemStatus.text(data.status);
    $availableCopies.replaceWith(
      generateAvailableCopiesBadgeTemplate(parseInt(data.available_copies))
    );
  })
    .done(function () {
      console.log("done");
    })
    .fail(function () {
      console.log("error");
    });
}

/*------------------------------------
		Making table rows clickable
  --------------------------------------*/

function redirectToDataUrl(event) {
  let url = event.target.parentElement.dataset.url;
  window.location = url;
}
