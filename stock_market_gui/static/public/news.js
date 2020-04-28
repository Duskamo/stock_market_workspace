$(document).ready(function() {
	/* 
	1.) Find News
	*/

	findNews();
} );

function findNews() {
	$('#findNews').on('click', function() {
		var stocks = $('#stocks').val();

		$.ajax({
			url: "/get_current_stock_news",
			method:"POST",
			contentType:"application/json",
			dataType:"json",
			data:JSON.stringify({"stocks":stocks}),
			success: function(html){
				console.log(html);

				allArticles = html['allArticles'];
				articleList = "";

				for (var i = 0; i < allArticles.length; i++) {			
					articleList += "<li class='list-group-item'><a href=/news/" + allArticles[i]['stock'] + ">Stock: " + allArticles[i]['stock'] + ", Total Results: " +allArticles[i]['totalResults'] + "</a></li>";
				}

				$('#stockListGroup').html(articleList);
			}		
		});
	});
}
