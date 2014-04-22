// SICP p. 356

// floating-point approximate equality
var EPSILON = 1.0e-15;
function epsEq(x, y) {
  return Math.abs(x - y) < EPSILON;
}

// sample usage
var c = makeConnector();
c("setValue")(9, "user");
c("value");
c("forget")("user");

// test the multiplier
var k = makeConnector();
var x = makeConnector();
var y = makeConnector();
constant(7, k);
multiplier(k, x, y);
probe('result', y);
setValue(x, 10, 'user');

// bugs
// forgetValue(x, 'user') does not actually erase old value
// probe not printing on new value changes, only informant = false, but is
// this way in original too

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
      throw new Error("Contradiction: " + value + " not equal to " + newval);
    } else {
      console.log("Ignored.");
    }
  }

  function forgetMyValue(retractor) {
    if (retractor === informant) {
      informant = false;
      forEachExcept(retractor, informAboutNoValue, constraints);
    } else {
      console.log("Ignored.");
    }
  }

  function connect(newConstraint) {
    if (constraints.indexOf(newConstraint) === -1) {
      constraints.push(newConstraint);
    }
    if (hasValue(me)) {
      informAboutValue(newConstraint);
    }
    console.log('Done connecting.');
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
      console.log("forEachExcept done.");
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
