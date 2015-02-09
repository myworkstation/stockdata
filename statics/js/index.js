var daybtn=$('#daybtn');
var weekbtn=$('#weekbtn');
var monthbtn=$('#monthbtn');
var minbtn=$('#minbtn');
var choosebtn=$('.choosebtn');

var stockpic=$('.stockpic');
var daypic=$('#daypic');
var weekpic=$('#weekpic');
var monthpic=$('#monthpic');
var minpic=$('#minpic');

var bigpic=$('#bigstockpic');


daybtn.click(function(){
	stockpic.hide();
	daypic.show();
	choosebtn.css('background-color','black');
	daybtn.css('background-color','#88ff99');
});

weekbtn.click(function(){
	stockpic.hide();
	weekpic.show();
	choosebtn.css('background-color','black');
	weekbtn.css('background-color','#88ff99');
});

monthbtn.click(function(){
	stockpic.hide();
	monthpic.show();
	choosebtn.css('background-color','black');
	monthbtn.css('background-color','#88ff99');
});

minbtn.click(function(){
	stockpic.hide();
	minpic.show();
	choosebtn.css('background-color','black');
	minbtn.css('background-color','#88ff99');
});

stockpic.click(function(){
	bigpic.append('<img src="stockinfo.dayurl">');
	bigpic.show();
});