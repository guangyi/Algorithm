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
    var obj = Object(this);
    if (arguments.length == 4) {
        for (var i = 0; i < 4; i++) {
            obj[child + i + 1] = arguments[i];
    }
    else this.val = x;    
｝
var node1 = new QuadTreeNode();
var node2 = new QuadTreeNode(false);
node1.child1 = node2;

var node1 = new QuadTreeNode(false);
var node2 = new QuadTreeNode(true);
// etc
var root = new QuadTreeNode(node1, node2, node3, node4);

function intersect(a, b) {
   if a.child[i] and b.child[i] == leave: a and b
   if 
}


