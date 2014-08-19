/**
  Flag sort
  
  [1, 0, 0, 1, 2, 2, 0]
  
  [0, 0, 0, 1, 1, 2, 2]

  haha
*/
function swap(array, start, end) {
  var temp = array[start];
  array[start] = array[end];
  array[end] = temp;
}

function flag(array) {
  if (Object.prototype.toString.call(array) != '[object Array]') {
    return
  }
  var length = array.length;
  if (length == 0) return;
  var start = 0;
  var end = length - 1;
  
  while (start < end) {
    if (array[start] == 0) start++;
    else if (array[start] == 1) {
      var temp = start + 1;
      while (temp < length && array[temp] != 0) {
        temp++;
      }
      if (temp < length) swap(array, start, temp);
      start++;
    }
    else {
      while (end > start && array[end] == 2) end--;
      if (end > start) swap(array, start, end);
    }
  }
}


// Test here
function assert(isTrue) {
  if (isTrue) console.log('assert pass!!!');
  else console.log('Ooooo.....Noooooo...');
}
function test1() {
  var arr1 = [1, 0, 0, 1, 2, 2, 0];
  flag(arr1);
  assert(arr1.toString() == [0, 0, 0, 1, 1, 2, 2].toString());
}

function test2() {
  var arr2 = [1, 1, 2, 2, 0, 0, 0, 1, 2, 1, 0, 2, 0, 1];
  flag(arr2);
  assert(arr2.toString() == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2].toString());
}

function test3() {
  var arr3 = [0, 1, 2];
  flag(arr3);
  assert(arr3.toString() == [0, 1, 2].toString());
}

function test4() {
  var arr4 = [2, 1, 0];
  flag(arr4);
  assert(arr4.toString() == [0, 1, 2].toString());
}

function test5() {
  var arr5 = [0, 2];
  flag(arr5);
  assert(arr5.toString() == [0, 2].toString());
}

function test6() {
  var arr6 = [2, 1];
  flag(arr6);
  assert(arr6.toString() == [1, 2].toString());
}

function test7() {
  var arr7 = [1, 1];
  flag(arr7);
  assert(arr7.toString() == [1, 1].toString());
}

function test8() {
  var arr8 = [2, 2];
  flag(arr8);
  assert(arr8.toString() == [2, 2].toString());
}

function test9() {
  var arr9 = [2];
  flag(arr9);
  assert(arr9.toString() == [2].toString());
}

function test10() {
  var arr10 = [2, 2, 2, 1, 1, 0, 0];
  flag(arr10);
  assert(arr10.toString() == [0, 0, 1, 1, 2, 2, 2].toString());
}

function test11() {
  var arr11 = [];
  flag(arr11);
  assert(arr11.toString() == [].toString());
}

function testNull() {
  console.log(arguments.callee.name);
  var arr = null;
  flag(arr);
  assert(arr == null);
  // ???
}

// How about null array and one element array?
// also [2, 2, 2, 1, 1, 0, 0] <- how about this?
// null array or empty array? 
// pass in null? pass it....
// what is the time complexity? O(n)

test1();
test2();
test3();
test4();
test5();
test6();
test7();
test8();
test9();
test10();
test11();
testNull();