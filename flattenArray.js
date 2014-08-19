function flatten(array) {
  var result = [];
  flattenHelper(array, result);
  console.log(result);
}

function flattenHelper(array, result) {
  array.forEach(function(item) {
    if (Object.prototype.toString.call(item) == '[object Array]') {
      flattenHelper(item, result);
    }
    else result.push(item);
  });
}

function test1() {
  var arr = [{a: 'a'}, 'b', ['c', 'd'], ['e', ['f']], 'g'];
  flatten(arr);
}

test1();


// Answer:
function flatten_array(arr) {
    var out = [];
    for (var i = 0; i < arr.length; i++) {
        var cur = arr[i];
        if (isArray(cur)) {
            out = out.concat(flatten_array(cur));
        } else {
            out.push(cur);
        }
    }
    return out;
}

function isArray(elem) {
    return Array.isArray(elem); // ES6 only, easy to polyfill
    return Object.prototype.toString.call(elem) === '[object Array]'; //best
    return elem instanceof Array; //acceptable, but susceptible to cross-frame issues
}


// Iterative
function flatten_array_iteratively(arr) {
    var out = [];
    while (arr.length) {
        var last = arr.pop();
        if (isArray(last)) {
            arr = arr.concat(last);
        } else {
            out.push(last);
        }
    }
    out.reverse();
    return out;
}
