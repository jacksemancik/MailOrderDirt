$(document).ready(function(){
      $(window).scroll(function() {
        if ($(document).scrollTop() > 50) {
          $('li a').addClass('shrink');
        } else {
          $('li a').removeClass('shrink');
        }
      });
    });
