$(document).ready(function() {
	/* 
	1.) Datatable Init
	2.) Stock Calculator Init
	3.) Journal Populate
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

// 2.) Stock Calculator Init
function stockCalcInit() {
	$('#calcStockPrice').on('click',function() {
		// Gather data and make calculations
		var buyPrice = $("#buyPrice").val();
		var profitRiskRatio = $('#profitRiskRatio').val();
		var portfolioAmt = $('#portfolioAmt').val();
		var riskPercent = $('#riskPercent').val();
		var commPerTrade = $('#commPerTrade').val();
		var commPerShare = $('#commPerShare').val();

		var stopLossCalc = buyPrice - (buyPrice * 0.01);
		var sellPriceCalc = ((buyPrice - stopLossCalc) * profitRiskRatio) + parseFloat(buyPrice);
		var reavaluate = ((sellPriceCalc - buyPrice) / 2) + parseFloat(buyPrice);
		var sharesToBuy = (portfolioAmt * riskPercent) / (parseFloat(buyPrice) - stopLossCalc); 
		var riskAmt = ((buyPrice - stopLossCalc) * sharesToBuy) + (commPerTrade * 2) + (commPerShare * sharesToBuy * 2);
		var profitAmt = ((sellPriceCalc - buyPrice) * sharesToBuy) - (commPerTrade * 2) + (commPerShare * sharesToBuy * 2);
		var costForShares = buyPrice * sharesToBuy;

		// Calculate all stop loss %
		$("#onePer").html("$" + (buyPrice * 0.01).toFixed(2));
		$("#twoPer").html("$" + (buyPrice * 0.02).toFixed(2));
		$("#twoHalfPer").html("$" + (buyPrice * 0.025).toFixed(2));
		$("#threePer").html("$" + (buyPrice * 0.03).toFixed(2));
		$("#fourPer").html("$" + (buyPrice * 0.04).toFixed(2));
		$("#fivePer").html("$" + (buyPrice * 0.05).toFixed(2));
		$("#sixPer").html("$" + (buyPrice * 0.06).toFixed(2));
		$("#sevenPer").html("$" + (buyPrice * 0.07).toFixed(2));
		$("#eightPer").html("$" + (buyPrice * 0.08).toFixed(2));
		$("#ninePer").html("$" + (buyPrice * 0.09).toFixed(2));
		$("#tenPer").html("$" + (buyPrice * 0.1).toFixed(2));

		// Trade Position Points
		$('#stopLoss').html("$" + stopLossCalc.toFixed(2));
		$('#sellPrice').html("$" + sellPriceCalc.toFixed(2));
		$('#reavaluate').html("$" + reavaluate.toFixed(2))
		$('#riskAmt').html('$' + riskAmt.toFixed(2));
		$('#sharesToBuy').html(sharesToBuy.toFixed(0));
		$('#profitAmt').html('$' + profitAmt.toFixed(2));
		$('#costForShares').html('$' + costForShares.toFixed(2));
	});
}

// 3.) Import Journal
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
