$(document).ready(function() {
	/* 
	1.) Datatable Init
	2.) Stock Calculator Init
	*/

	datatableInit();
    	stockCalcInit();

} );

// Datatable Init
function datatableInit() {
	$('#example').DataTable();
}

// Stock Calculator Init
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
