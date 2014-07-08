/* Merge Sort */
$(document).ready(function(){
	function mergeSort(arr){
		var aux = [];
		for (var k = 0; k <= arr.length-1; k++){
		// copy arr. obj can not use aux = arr
			aux.push(arr[k]);
		}
		mergeSortMain(arr, aux, 0, arr.length - 1);
		return arr
	}
	function mergeSortMain(arr, aux, start, end){
		if (start >= end){
			return
		}
		else{
			var mid = Math.floor((end + start)/2);
			mergeSortMain(arr,aux,start, mid);
			mergeSortMain(arr,aux, mid+1, end);
			merge(arr,aux, start, mid, end);
		}
	}
	function merge(arr, aux, low, mid, high){
		/*AUX must be the same as arr!!!*/
		for (var k = 0; k <= arr.length-1; k++){
		// copy arr. obj can not use aux = arr
			aux[k] = arr[k];
		}
	var i = low,j = mid+1;
	for (var k = low; k <= high; k++){
		if ( i > mid ) {arr[k] = aux[j++];}
		else if ( j > high) {arr[k] = aux[i++];}
		else if (aux[i] <= aux[j]) {arr[k] = aux[i++];}
		else if (aux[i] > aux[j] ) {arr[k] = aux[j++];}
		console.log(arr);
	}
	return arr;
}
	var arr = [5,6,1,2];
	//var arr2 = [5,6,1,2,4]
	//arr = merge(arr, arr2, 0, 2,4);
	//console.log(arr);
	arr2 = [8,3,6,0,7,1,2];
	//console.log(mergeSort(arr2));
	function quickSort(arr, low, high){

	}
})
