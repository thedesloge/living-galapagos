// JavaScript Document
						
$(function() {
	var access_token = location.hash.split('=')[1];
		$.ajax({
			type: "GET",
			dataType: "jsonp",
			cache: false,
			url: "https://api.instagram.com/v1/tags/galapagos/media/recent?access_token=14360956.f59def8.e74b2cfb7e7e42ceab31d26683567365",
			
				
			
			success: function(data) {
				for (var i = 0; i < 9; i++) {
					$("#instafeed").append("<a href='"+data.data[i].images.standard_resolution.url +"' class='lightview' data-lightview-title='" + data.data[i].user.username + "' data-lightview-caption='" + data.data[i].caption.text + "'><img class='instaframe' src='" + data.data[i].images.standard_resolution.url +"' /></a>"
					);
				 
				}
			}
		});
});
		
