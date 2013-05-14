$(function(){
  // 文档就绪
	$("#apipaths li").bind('click',function(){
		//$("#apipaths li").removeClass("active");
		$(this).addClass("active");
		//$(this).css("font-size","36");
		//$("#homeContainer").hide();
		//$("div[id^=docdiv]").hide();
		//$("#docdiv_" +$(this).attr("id")).show();
		//return false;
	});
});