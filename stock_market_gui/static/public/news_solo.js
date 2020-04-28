$(document).ready(function() {
	/* 
	1.) Page Setup
	*/
	pageSetup();
	
} );

/* 
1.) Page Setup
*/
function pageSetup() {
	var stock = getValueAtIndex(4);

	// Set Title
	$("#title").html(stock + " News");

	// Gather individual news based on passed parameter 
	$.ajax({
			url: "http://localhost:5000/get_current_stock_news",
			method:"POST",
			contentType:"application/json",
			dataType:"json",
			data:JSON.stringify({"stocks":stock}),
			success: function(html){
				console.log(html);

				allArticles = html['allArticles'];
				articleList = "";

				for (var i = 0; i < allArticles[0]['articles'].length; i++) {			
					articleList += "<li class='list-group-item'><table><tr><td><a href=" + allArticles[0]['articles'][i]['url'] + "><img src=" + allArticles[0]['articles'][i]['urlToImage'] + " height='150px' width='150px' /></a>" + "</td><td>" + allArticles[0]['articles'][i]['title'] + "</td><td></td></tr><tr><td></td><td>Date Published: " + allArticles[0]['articles'][i]['publishedAt'] + "</td><td>Source: " + allArticles[0]['articles'][i]['source']['name'] + "</td></tr></table>" + "</li>";
				}

				$('#stockListGroup').html(articleList);
			}		
		});
}

function getValueAtIndex(index) {
	var str = window.location.href;
	return str.split("/")[index];
}
