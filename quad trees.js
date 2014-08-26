quad trees

+---------------+
|               |
|               |
|               |
|               |
|               |
|               |
|               |
+---------------+

+-------+-------+
|       |       |
|       |       |
|       |       |
+-------+-------+
|       |       |
|       |       |
|       |       |
+-------+-------+

+-------+---+---+
|       |   |   |
|       +---+---+
|       |   |   |
+---+---+---+---+
|   |   |       |
+---+---+       |
|   |   |       |
+---+---+-------+

A:
+-------+-------+ T: true
|       |       | F: false
|   T   |   T   |
|       |       |
+-------+-------+
|       |       |
|   F   |   F   |
|       |       |
+-------+-------+

B:
+-------+---+---+
|       | F | F |
|   T   +---+---+
|       | T | T |
+---+---+---+---+
| F | T |       |
+---+---+   F   |
| F | T |       |
+---+---+-------+

C: = A and B
+-------+-------+
|       | F | F |
|   T   +---+---+
|       | T | T |
+-------+---+---+
|       |       |
|   F   |   F   |
|       |       |
+-------+-------+

[T,[F,F,T,T], [F,T,F,T],F]
function QuadTreeNode(x) ｛

    // this.topLeft;
    // this.topRight;
    // this.bottomLeft;
    // this.bottomRight;
    // this.val;
    this.copy = function() {
    	if (this.hasOwnProperty('val')) {
    		return new QuadTreeNode(this.val);
    	}
    	else {
    		var topLeft     = this.topLeft.copy();
			var topRight    = this.topRight.copy();
			var bottomLeft  = this.bottomLeft.copy();
			var bottomRight = this.bottomRight.copy();
			return new QuadTreeNode(topLeft, topRight, bottomLeft, bottomRight);
    	}
    };

    if (arguments.length == 4) {
    	this.topLeft     = arguments[0];
    	this.topRight    = arguments[1];
    	this.bottomLeft  = arguments[2];
    	this.bottomRight = arguments[3];
    }
    else 
    	this.val = x;    
｝
var node1 = new QuadTreeNode();
var node2 = new QuadTreeNode(false);
node1.child1 = node2;

var node1 = new QuadTreeNode(false);
var node2 = new QuadTreeNode(true);
// etc
var root = new QuadTreeNode(node1, node2, node3, node4);

function intersect(a, b) {
	if (a.hasOwnProperty('val') && b.hasOwnProperty('val')) {
		return new QuadTreeNode(a.val && b.val);
	} 
	else if (a.hasOwnProperty('val') || b.hasOwnProperty('val')) {
		var leafNode = a.hasOwnProperty('val') ? a : b;
		var rootNode = a.hasOwnProperty('val') ? b : a;
		if (leafNode.val == true) {
			return rootNode.copy();
		}
		else return new QuadTreeNode(false);
	}
	else {
		var topLeft     = intersect(a.topLeft, b.topLeft);
		var topRight    = intersect(a.topRight, b.topRight);
		var bottomLeft  = intersect(a.bottomLeft, b.bottomLeft);
		var bottomRight = intersect(a.bottomRight, b.bottomRight);
		return new QuadTreeNode(topLeft, topRight, bottomLeft, bottomRight);
	}
}


/*
function intersectWrapper(a, b, c) {
	if (a.hasOwnProperty('val') && b.hasOwnProperty('val')) {

	}
	for (var i = 0; i < 4; i++) {
		var childOfA = a['child' + i.toString()];
		var childOfB = b['child' + i.toString()];
		if (childOfA.hasOwnProperty('val') &&
		    childOfB.hasOwnProperty('val')) {
			c['child' + i.toString()].val = childOfA && childOfB;
		}
		else if (childOfA.hasOwnProperty('val') && !childOfB.hasOwnProperty('val')) {
			if (childOfA.val == false) {
				c['child' + i.toString()].val = false;
			}
			else c['child' + i.toString()] = childOfB;
		}
		else if (!childOfA.hasOwnProperty('val') && childOfB.hasOwnProperty('val')) {
			if (childOfB.val == false) {
				c['child' + i.toString()].val = false;
			}
			else c['child' + i.toString()] = childOfA;
		}
		else {
			intersectWrapper(childOfA, childOfB, c);
		}
	}
	return c;
}
*/


