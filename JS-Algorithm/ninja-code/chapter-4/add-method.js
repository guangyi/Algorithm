function addMethod(object, name, fn) {
  var old = object[name]; 
  console.log(old);                       //#1
  object[name] = function(){
  	console.log(arguments);
    if (fn.length == arguments.length) {
    	console.log('here1');           //#2
      return fn.apply(this, arguments)           //#2
    }
    	
    else if (typeof old == 'function') {
    	console.log(fn.length, arguments.length);
    	return old.apply(this, arguments);         
    }          //#3
          //#3
  };
}

