// JavaScript Document


$(document).ready(function() {
	$(".start_button").click(function(){
		$(".start_content").slideDown("slow");	
	});	
	
	
	
	  $('#particles').particleground({
    dotColor: '#FFF',
    lineColor: '#FFF'
  });
  $('.intro').css({
    'margin-top': -($('.intro').height() / 2)
  });
  

	


	$(".start_content ul li:first").click(function(){
		$("html,body").animate({scrollTop: $("#content").offset().top}, 400), 
		$("#content_form").fadeIn(1500);
		$("#content_form ul").animate({left: "130px"},1000,'linear');
	
	});
	
	




function showNextPanel() {
		$("#content_form").fadeIn(1500);
		$("#content_form ul").animate({left: "130px"},1000,'linear');
 
	}
	
	
	
	
	var nav = $('.navMenu');
	var banner = $('header h1');
	var pos = nav.position();
	
	$(window).scroll(function() {

		var windowpos = $(window).scrollTop();
		
		if (windowpos>=banner.outerHeight()) {
			nav.addClass('fixedTop');
			$("#content_form").fadeIn(1500);
			$("#content_form ul").animate({left: "130px"},1000,'linear');
 
		}
		
		else {
			nav.removeClass('fixedTop');
		}
		
	});
  
});


