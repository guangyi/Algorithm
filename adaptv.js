Markup all phone numbers of this format in a <phone> tag in 10k+ html files in our website. The files can be in any subdirectory.

from

<>(XXX) XXX-XXXX</>

to

<phone>(XXX) XXX-XXXX</phone>
document.querySelectorAll(‘body *)


reExpress = ‘/([0-9]*3)[0-9]*3-[0-9]*4’
files = open(‘folder/address) 
for file in files:
    fileContent = open(file)
    for line in fileContent:
        index = re.match(reExpress, line)
        if index >-1:
       	 file.write(line[: index] + ‘<phone>’ + line[index + 1: index + 14] + line[index + 14: ])
close file

print binary search tree order in lexographical order
in order tree traversal
     b
a       c abc
def traversal(self, root):
    if root == None: return
    self.traversal(root.left)
    print root.val
    self.traversal(root.right)

Array.prototype.map = function( arr, callback) {
    var newArr = [];
    for (var i  = 0; i < arr.length; i++){
        var temp = callback(arr[i]);
        newArr.push(temp);
    }
    return newArr;
}
    map([1,2,3], function(x) { return x* x; });
[1,4,9]


some_exp_fn(); // this takes a long time


ratelimit_exp_fn() // this is called any number of times, but internally calls some_exp_fn at most once every 60s.

function ratelimit_exp_fn() {
            var prevTime;
	var time2 = getTime();
	if (time2 - prevTime > 60) {
		result = some_exp_fn();
		prevTime = time2;
	return result
 }
 ratelimit_exp_fn(fn3, fn4)
 ratelimit_exp_fn(fn3)
 ratelimit_exp_fn

ratelimit(fn) {
	}

ratelimited_exp_fn1 = ratelimit(exp_fn);

ratelimited_exp_fn2 = ratelimit(exp_fn2);

function ratelimit(fn) {
var prevTime = 0;
	return function() {
            var time2 = getTime();
	if (time2 - prevTime > 60) {
		result = fn();
		prevTime = time2;
	return result
 	}

}

gerrit
