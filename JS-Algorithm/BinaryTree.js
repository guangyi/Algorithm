$(document).ready(function(){
	var tree = [3, 9, 20, '#', '#', 5, 17];
	//console.log(13 % 12);
	function TreeNode(val, left, right){
		this.val = val;
		this.left = left;
		this.right = right;
	};
	var nod5 = new TreeNode(2, null, null);
	var nod6 = new TreeNode(8, null, null);
	var nod7 = new TreeNode(4, null, null);
	var nod1 = new TreeNode(9, nod5, nod6);
	var nod2 = new TreeNode(7, null, nod7);
	var root = new TreeNode(3, nod1 , nod2);
	
	var res = BinaryTree(root);
	for (var i = 0; i < res.length ; i++) {
		console.log(res[i]);
	};
	function BinaryTree(root) {
		if(!root) {return [];};
		var result = [];
		var thisLevel = [root];
		result.push([root.val]);

		/*
			sdfsadfsdfs
			sdfasdfsadfssdf
		*/
		while(thisLevel.length != 0) {
			var nextLevel = [];
			temp = []
			for (var i = 0; i < thisLevel.length; i++) {
				if (thisLevel[i].left ) nextLevel.push(thisLevel[i].left);
				if (thisLevel[i].right) nextLevel.push(thisLevel[i].right);
				temp.append(node.val);
			};
			result.push(temp);
			// or result.unshift(temp);// this is for bottom up requirment
			thisLevel = nextLevel;
		}
		return result;
	}
	function partition(arr, lo, hi) {
		var i = lo + 1;
		var j = hi;
		while(i < j) {
			while(arr[i] < arr[lo] && i <= hi) {
				i++;
			}
			while(arr[j] > arr[lo] && j >= lo) {
				j--;
			}
			if (j < i) {
				exchange(arr, lo, j);
			}
			else {
				exchange(arr, i ,j);
			}
		}
		return j;// j points to mid
	}
	var arr = ['k','a','r','t','e','l','e','p','u','i','q','c','x','o','s'];
	partition(arr, 0, arr.length-1);
	arr.forEach(function(a){
		console.log(a);
	});
});
function exchange(arr, i, j) {
	var temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}
function storeVal(arr){
	var value = [];
	for (var i = 0; i < arr.length; i++) {
		value.push(arr[i].val);
	}
	return value;
}
var ary = Array(3);
ary[0]=2
arr = ary.filter(function(elem) { return elem == 2; })
console.log( arr.length );
console.log( 2 === [2] );
console.log( 2 === [[2]] );
console.log( 2 === [[[2]]] );
console.log( [] == []);
var temp = function(x){
	var bar = 1;
	return function(y){
		console.log(x + y +(++bar));
	}
}
var t = temp(1);
var t2 = temp(2);
t(1);
t(2);
t2(1);
var arr = [1,2,3];
for(var i =0; i < arr.length; i++){
	// problem is i is changing.
	console.log("length" + arr.length);
	console.log(arr.pop());
}
a = [1,2,3];
b = [4]
console.log(a.concat(b));