function flattenObj(obj, parentKey, newObj) {
	for (key in obj) {
		if (typeof obj[key] == 'object') {
			parentKey = parentKey == '' ? key : parentKey + '_' + key;
			flattenObj(obj[key], parentKey, newObj);
		}
		else {
			if (parentKey != '') {
				newObj[parentKey + '_' + key] = obj[key];
			}
			else {
				newObj[key] = obj[key];
			}
		}
	}
}

function flatten(obj) {
	var newObj = {};
	flattenObj(obj, '', newObj);
	console.log(newObj);
}

flatten({'t1':2});
flatten({'t1':2, 't2': 3});
flatten({
	't1':1,
	't2':{
		't3':3,
		't4':4
	}
});
flatten({
	't1':2,
	't2':{
		't3':3,
		't4':{
			't5':5
		}
	}
});