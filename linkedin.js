// This is good :)

function Foo(){}
         Foo.prototype.a = "something";

// but this is bad.

function Foo(){}
Foo.prototype = {

  // some code in here....

};

// but this is also bad too....

function Foo(){}

var someRefObj = {};          // this is an object

Foo.prototype = someRefObj;      // but this is also bad, why?

var someInstance = new Foo();
someInstance.constructor        // what does this point to?  
                                // Function Object(){.....}