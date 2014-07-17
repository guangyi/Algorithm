function callBackIfDone(funcList, done) {
	var counter = 0;
	function callBack(name) {
		console.log(name);
		counter++;
		if (counter == funcList.length) done();
	}
	funcList.forEaach(function(func) {
		func(callBack);
	})
}

function test() {
	var a = function(callBack) {
		setTimeout(callBack(this.name), 1000);
	}
	var b = function(callBack) {
		setTimeout(callBack(this.name), 2000);
	}
	var c = function(callBack) {
		setTimeout(callBack(this.name), 3000);
	}

}