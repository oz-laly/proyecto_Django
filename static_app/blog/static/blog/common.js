$(function () {
    $(window).on("scroll touchmove", function () {
      $("header, footer").stop();
      $("header, footer").css("display", "none").delay(100).fadeIn("slow");
    });
  });