// SICP p. 356

// floating-point approximate equality
var EPSILON = 1.0e-15;
function epsEq(x, y) {
  return Math.abs(x - y) < EPSILON;
}

// ex. 3.34 p. 367
function squarer(a, b) {
  function processNewValue() {
    if (hasValue(b)) {
      if (getValue(b) >= 0) {
        setValue(a, Math.sqrt(getValue(b)), me);
      } else {
        throw new Error("cannot take square root of negative number");
      }
    } else if (hasValue(a)) {
      setValue(b, getValue(a) * getValue(a), me);
    }
  }
  function processForgetValue() {
    forgetValue(a, me);
    forgetValue(b, me);
    processNewValue();
  }
  function me(request) {
    switch (request) {
    case "I-have-a-value":
      processNewValue();
      break;
    case "I-lost-my-value":
      processForgetValue();
      break;
    default:
      throw new Error("unknown request: squarer " + request);
    }
  }
  connect(a, me);
  connect(b, me);
  return me;
}

// (adder a1 a2 sum)
function adder(a1, a2, sum) {
  function processNewValue() {
    if (hasValue(a1) && hasValue(a2)) {
      setValue(sum, getValue(a1) + getValue(a2), me);
    } else if (hasValue(a1) && hasValue(sum)) {
      setValue(a2, getValue(sum) - getValue(a1), me);
    } else if (hasValue(a2) && hasValue(sum)) {
      setValue(a1, getValue(sum) - getValue(a2), me);
    }
  }
  function processForgetValue() {
    forgetValue(sum, me);
    forgetValue(a1, me);
    forgetValue(a2, me);
    processNewValue();
  }
  function me(request) {
    switch (request) {
    case "I-have-a-value":
      processNewValue();
      break;
    case "I-lost-my-value":
      processForgetValue();
      break;
    default:
      throw new Error("unknown request: adder " + request);
    }
  }
  connect(a1, me);
  connect(a2, me);
  connect(sum, me);
  return me;
}

// (multiplier m1 m2 product)
function multiplier(m1, m2, product) {
  function processNewValue() {
    if ((hasValue(m1) && getValue(m1) === 0) ||
        (hasValue(m2) && getValue(m2) === 0)) {
      setValue(product, 0, me);
    } else if (hasValue(m1) && hasValue(m2)) {
      setValue(product, getValue(m1) * getValue(m2), me);
    } else if (hasValue(product) && hasValue(m1)) {
      setValue(m2, getValue(product) / getValue(m1), me);
    } else if (hasValue(product) && hasValue(m2)) {
      setValue(m1, getValue(product) / getValue(m2), me);
    }
  }
  function processForgetValue() {
    forgetValue(product, me);
    forgetValue(m1, me);
    forgetValue(m2, me);
    processNewValue();
  }
  function me(request) {
    switch (request) {
    case "I-have-a-value":
      processNewValue();
      break;
    case "I-lost-my-value":
      processForgetValue();
      break;
    default:
      throw new Error("unknown request: multiplier " + request);
    }
  }
  connect(m1, me);
  connect(m2, me);
  connect(product, me);
  return me;
}

// (constant value connector)
function constant(value, connector) {
  function me(request) {
    throw new Error("unknown request: constant " + request);
  }
  connect(connector, me);
  setValue(connector, value, me);
  return me;
}

// (probe name connector)
function probe(name, connector) {
  function printProbe(value) {
    console.log("Probe: " + name + " = " + value);
  }
  function processNewValue() {
    printProbe(getValue(connector));
  }
  function processForgetValue() {
    printProbe("?");
  }
  function me(request) {
    switch (request) {
    case "I-have-a-value":
      processNewValue();
      break;
    case "I-lost-my-value":
      processForgetValue();
      break;
    default:
      throw new Error("unknown request: probe " + request);
    }
  }
  connect(connector, me);
  return me;
}

// (inform-about-value constraint), (inform-about-no-value constraint)
function informAboutValue(constraint) {
  constraint("I-have-a-value");
}
function informAboutNoValue(constraint) {
  constraint("I-lost-my-value");
}

// (make-connector)
function makeConnector() {
  var value = false;
  var informant = false;
  var constraints = [];

  function setMyValue(newval, setter) {
    if (!hasValue(me)) {
      value = newval;
      informant = setter;
      forEachExcept(setter, informAboutValue, constraints);
    } else if (!epsEq(value, newval)) {  // else if (value !== newval) {  
      throw new Error("Contradiction: " + value + " is not equal to " + newval);
    } else {
      // console.log("Ignored.");
    }
  }

  function forgetMyValue(retractor) {
    if (retractor === informant) {
      informant = false;
      forEachExcept(retractor, informAboutNoValue, constraints);
    } else {
      // console.log("Ignored.");
    }
  }

  function connect(newConstraint) {
    if (constraints.indexOf(newConstraint) === -1) {
      constraints.push(newConstraint);
    }
    if (hasValue(me)) {
      informAboutValue(newConstraint);
    }
    // console.log('Done connecting.');
  }
  
  function me(request) {
    switch (request) {
    case "hasValue":
      if (informant) {
        return true;
      } else {
        return false;
      }
    case "value":
      return value;
    case "setValue":
      return setMyValue;
    case "forget":
      return forgetMyValue;
    case "connect":
      return connect;
    default:
      throw new Error("unknown operation on connector " + request);
    }
  }
  
  return me;
}

// (for-each-except exception procedure list)

function forEachExcept(exception, procedure, list) {
  function loop(items) {
    if (items.length === 0) {
      // console.log("forEachExcept done.");
    } else if (items[0] === exception) {
      // console.log("excluding exception: " + exception);
      loop(items.slice(1));
    } else {
      procedure(items[0]);
      loop(items.slice(1));
    }
  }
  loop(list);
}

// (has-value? connector) ... (connect connector new-constraint)

function hasValue(connector) {
  return connector("hasValue");
}

function getValue(connector) {
  return connector("value");
}

function setValue(connector, newValue, informant) {
  connector("setValue")(newValue, informant);
}

function forgetValue(connector, retractor) {
  connector("forget")(retractor);
}

function connect(connector, newConstraint) {
  connector("connect")(newConstraint);
}

// test the multiplier
var k = makeConnector();
var x = makeConnector();
var y = makeConnector();
constant(7, k);
multiplier(k, x, y);
probe('result', y);
setValue(x, 4, 'user');
setValue(x, 7, 'user');
forgetValue(x, 'user');

// Celsius to Fahrenheit
var C = makeConnector();
var F = makeConnector();
function celsiusToFahrenheitConverter(c, f) {
  var u = makeConnector();
  var v = makeConnector();
  var w = makeConnector();
  var x = makeConnector();
  var y = makeConnector();
  multiplier(c, w, u);
  multiplier(v, x, u);
  adder(v, y, f);
  constant(9, w);
  constant(5, x);
  constant(32, y);
}
celsiusToFahrenheitConverter(C, F);
probe("Celsius temp.", C);
probe("Fahrenheit temp.", F);
setValue(C, 25, 'user');
forgetValue(C, 'user');
setValue(F, 350, 'user');
forgetValue(F, 'user');

// area of a circle
function areaOfCircle(r, a) {
  var w = makeConnector();
  var x = makeConnector();
  squarer(r, w);
  multiplier(w, x, a);
  constant(3.1415, x);
}
var r = makeConnector();
var a = makeConnector();
areaOfCircle(r, a);
probe("radius", r);
probe("area", a);
setValue(r, 3, 'user');
forgetValue(r, 'user');
setValue(a, 22, 'user');
forgetValue(a, 'user');

// square root
var x = makeConnector();
var sqrt_x = makeConnector();
squarer(sqrt_x, x);
probe("the square root of x", sqrt_x);
probe("x", x);
setValue(x, 3, 'user');
forgetValue(x, 'user');
setValue(sqrt_x, 9, 'user');
forgetValue(sqrt_x, 'user');

// ex. 3.33 p. 366
function average(a, b, avg) {
  var u = makeConnector();
  var v = makeConnector();
  adder(a, b, v);
  multiplier(avg, u, v);
  constant(2, u);
}
var a = makeConnector();
var b = makeConnector();
var avg = makeConnector();
average(a, b, avg);
probe("average", avg);
setValue(a, 10, 'user');
setValue(b, 22, 'user');
forgetValue(b, 'user');

// contradiction
var u = makeConnector();
var v = makeConnector();
var a = makeConnector();
var b = makeConnector();
var x = makeConnector();
adder(u, v, x);
adder(a, b, x);
probe("a", a);
setValue(u, 1, 'user');
setValue(v, 2, 'user');
setValue(a, 10, 'user');
setValue(b, 20, 'user');
