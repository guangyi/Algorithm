/* Merge K sorted array
  [
    [1, 4]
    [2, 6, 7]
    [3, 5, 8]
  ]
  result: [1, 2, 3, 4, 5, 6, 7, 8]

*/

function minimal(array) {
  // array = [[arrayIndex, elemIndex, arrList[arrayIndex][elemIndex]], ...]
  if (array == []) return 
  array.sort(function(a, b) {
     if (a[2] < b[2]) return -1;
     if (a[2] > b[2]) return 1;
    else return 0;
  });
  var min = array.shift();
  return min;
}

function merge(arrayList) {
  var length = arrayList.length;
  var temp = [];
  var result = []
  var elemIndex = 0;
  for (var arrayIndex = 0; arrayIndex < length; arrayIndex++) {
    temp.push([arrayIndex, elemIndex, arrayList[arrayIndex][elemIndex]]);
  }
  while (temp.length != 0) {
    var tempMin = minimal(temp);
    var arrIndex = tempMin[0];
    var elemIndex = tempMin[1];
    var minValue = tempMin[2];
    result.push(minValue);
    elemIndex++;
    if (elemIndex < arrayList[arrIndex].length) {
      temp.push([arrIndex, elemIndex, arrayList[arrIndex][elemIndex]]);
    }
  }
  return result;
}

function mergeSort(arrayList) {
  return mergeSortHelper(arrayList, 0, arrayList.length - 1);
}

function mergeSortHelper(arrayList, start, end) {
  if (start >= end) return arrayList[start]; 
  var mid = Math.floor(start + (end - start) / 2);
  var array1 = mergeSortHelper(arrayList, start, mid);
  var array2 = mergeSortHelper(arrayList, mid + 1, end);
  var sorted = mergeArray(array1, array2);
  return sorted;
}
 function mergeArray(array1, array2) {
   var result = [];
   var index1 = 0;
   var index2 = 0;
   while (index1 < array1.length || index2 < array2.length) {
     if (index1 >= array1.length) result.push(array2[index2++]);
     else if (index2 >= array2.length) result.push(array1[index1++]);
     else if (array1[index1] <= array2[index2]) {
       result.push(array1[index1++]);
     } 
     else result.push(array2[index2++])
   }
   return result;
 }

function assert(isTrue) {
  if (isTrue) console.log('assert pass!!');
  else console.log('Oh..No...sth is wrong');
}

function test1() {
  var arrayList = [ 
    [1, 4, 9],
    [2, 6, 7],
    [3, 5, 8, 10],
  ];
  var result = merge(arrayList);
  assert(result.toString() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].toString());
  var result2 = mergeSort(arrayList);
  assert(result2.toString() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].toString());
}

function test2() {
  var arrayList = [[1,2,3]];
  assert(merge(arrayList).toString() == [1,2,3].toString());
  assert(mergeSort(arrayList).toString() == [1,2,3].toString());
}
test1();
test2();

