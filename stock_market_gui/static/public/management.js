$(document).ready(function() {
	/* 
	1.) Datatable Init
	2.) Journal Populate
	*/

	datatableInit();
    	stockCalcInit();
	importJournal();
} );

// 1.) Datatable Init
function datatableInit() {
	$('#example').DataTable({
		"ajax": "http://localhost:5000/get_journal_list",
		"columns": [
			{ "data": "trade_id" },
			{ "data": "trade_date" },
			{ "data": "symbol" },
			{ "data": "type" },
			{ "data": "quantity" },
			{ "data": "bought" },
			{ "data": "sold" },
			{ "data": "initial_risk" },
			{ "data": "commission" },
			{ "data": "profit_and_loss" },
			{ "data": "r_multiple" },
			{ "data": "percent_wins" },
			{ "data": "money_at_work" },
			{ "data": "percent_pl" },
			{ "data": "initial_percent_risk" },
			{ "data": "wl" },
			{ "data": "sum_wl" }
		]
	});
}

// 2.) Import Journal
function importJournal() {
	$("#importData").on('click',function(){
		$.ajax({
			url: "http://localhost:5000/import_data_to_table",
			type:"GET",
			success: function(html){
				console.log(html);
			}		
		});

		location.reload();
	});
}
