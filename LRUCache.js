
function LRUCache(capacity) {
  this.capacity = capacity;
  this.put = function(key, value) {
    if (Object.keys(cache).length >= this.capacity && !(key in cache)) {
      var elemNeedToRemove = head;
      updateHead();
      delete cache[elemNeedToRemove];
    }
    if (!(key in cache)) {
      cache[key] = {value: value};
      if (head == null)  head = key;
      updateTail(key);
    }
    else {
      cache[key].value = value;
      updateOrderInCache(key);
      updateTail(key);
    }
  }
  this.get = function(key) {
    if (key in cache) {
      updateOrderInCache(key);
      updateTail(key);
      return cache[key].value;
    }
    return; 
  }
  this.remove = function(key) {
    if (key in cache) {
      removeKey(key);
    }
  }
  this.toString = function() {
    var key  = head;
    var result = '';
    while (key != null) {
      var ending = cache[key].next == null ? '' : ' << ';
      result += (key + ':' + cache[key].value + ending);
      key = cache[key].next;
    }
    return result || '[empty]';
  }
  
  var cache = new Object();
  var head = null;
  var tail = null;
  function updateTail(key) {
    if (tail != null) {
      cache[tail].next = key;
      cache[key].prev = tail;
      cache[key].next = null;
    }
    tail = key;
  };
  function updateHead() {
    if (head == null)  head = key;
    else {
      var nextKey = cache[head].next;
      if (nextKey) cache[nextKey].prev = null;
      head = nextKey;
    }
  };
  function updateOrderInCache(key) {
    if (cache[key].prev != null) {
      var prevKey = cache[key].prev;
      var nextKey = cache[key].next;
      cache[prevKey].next = nextKey;
      if (nextKey) cache[nextKey].prev = prevKey;
    }
    else {
      updateHead();
    }
  }
  function removeKey(key) {
    updateOrderInCache(key);
    if (cache[key].next == null) tail = cache[key].prev;
    delete cache[key];
  }

}

function assert(isTrue) {
  if (isTrue) console.log('assert pass!!! ');
  else console.log('Oops, not pass... ');
}

// Tests related

function test1() {
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  assert(lru.capacity == 3);
}

function test2() {
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 29);
  lru.put('john', 26);
  lru.put('angela', 24);
  assert(lru.toString() == 'adam:29 << john:26 << angela:24');
}

function test3() {
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 29);
  lru.put('john', 26);
  lru.put('angela', 24);
  lru.put('zhisheng', 88);
  assert(lru.toString() == 'john:26 << angela:24 << zhisheng:88');
}

function test4() {
  // test LRUCache.put function --> update value.
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 29);
  lru.put('john', 26);
  lru.put('angela', 24);
  lru.put('john', 78);
  assert(lru.toString() == 'adam:29 << angela:24 << john:78');
}

function test5() {
  // test LRUCache.get function.
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 29);
  lru.put('john', 26);
  lru.put('angela', 24);
  assert(lru.toString() == 'adam:29 << john:26 << angela:24');
  assert(lru.get('adam') == 29);
  assert(lru.toString() == 'john:26 << angela:24 << adam:29');
}

function test6() {
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 29);
  lru.put('john', 26);
  lru.put('angela', 24);
  assert(lru.toString() == 'adam:29 << john:26 << angela:24');
  lru.put('zhouzhou', 3);
  lru.put('john', 567);
  assert(lru.get('adam') == undefined);
  assert(lru.toString() == 'angela:24 << zhouzhou:3 << john:567');
}

function test7() {
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 34);
  lru.put('dan', 89);
  assert(lru.get('adam') == 34);
  assert(lru.toString() == 'dan:89 << adam:34');
}

function test8() {
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 34);
  lru.put('dan', 89);
  lru.remove('adam');
  assert(lru.toString() == 'dan:89');
  lru.remove('dan');
  assert(lru.toString() == '[empty]');
  
}

  // 1. remove first
  // 2. remove last
  // 3. remove the middle ones
function test9() {
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 29);
  lru.put('john', 26);
  lru.put('angela', 24);
  lru.remove('adam');
  assert(lru.toString() == 'john:26 << angela:24');
}

function test10() {
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 29);
  lru.put('john', 26);
  lru.put('angela', 24);
  lru.remove('john');
  assert(lru.toString() == 'adam:29 << angela:24');
}

function test11() {
  console.log(arguments.callee.name);
  var lru = new LRUCache(3);
  lru.put('adam', 29);
  lru.put('john', 26);
  lru.put('angela', 24);
  lru.remove('angela');
  assert(lru.toString() == 'adam:29 << john:26');
}

test1();console.log('');
test2();console.log('');
test3();console.log('');
test4();console.log('');
test5();console.log('');
test6();console.log('');
test7();console.log('');
test8();console.log('');
test9();console.log('');
test10();console.log('');
test11();console.log('');








// var c = new LRUCache(3);
// c.put('adam', 29);
// c.put('john', 26);
// c.put('angela', 24);
// c.toString();        // -> "adam:29 < john:26 < angela:24"
// c.get('john');       // -> 26
// // Now 'john' is the most recently used entry, since we just requested it
// c.toString();        // -> "adam:29 < angela:24 < john:26"
// c.put('zorro', 141); // -> {key:adam, value:29}
// // Because we only have room for 3 entries, put-ing 'zorro' purged 'adam'
// c.toString();        // -> "angela:24 < john:26 < zorro:141"



/* 
Your previous C++ content is preserved below:

#include <iostream>
using namespace std;

// To execute C++, please define "int main()"

class LRUCache {
  
  (id)initWithCapacity:(int)capacity;
  
  (void)addObject:(id)object; // when it's full, you need to remove the least recently used object.
      
  (id)getObjectForKey:(string)key; // update the frequency
  
  (void)removeObject:(id)object;

  (int)size; // 2
  
  (int)capacity; // 100

}


int main() {
  for (int i = 0; i < 5; i++) {
    cout << "hello world\n";
  }
  return 0;
}


/* 
Your previous JavaScript content is preserved below:

// Interview question:
// How to implement a LRU cache.


// LRU is least recently used.
// FIFO, LIFO, LRU.

class
 */