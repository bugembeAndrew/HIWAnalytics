$(function () {
	$('#chart_container').highcharts({
		chart: {
			type: 'bar'
		},
		title: {
			text: 'Classification of Reasons for Calling'
		},
		xAxis: {
			categories: ['Classes of the Calls']
		},
		yAxis: {
			title: {
				text: 'frequency'
			}
		},
		series: [{
			name: 'HIV/AIDS',
			data: [{{data_dict.hiv}}]
		},{
			name: 'Other',
			data: [{{data_dict.other}}]
		},{
			name: 'VMMC',
			data: [{{data_dict.vmmc}}]
		},{
			name: 'Reproductive Health',
			data: [{{data_dict.reproductive}}]
		}, {
			name: 'Service Inquiry',
			data: [{{data_dict.inquiry}}]
		}]
	});
});