// joel on software test yourself

function accumulate(combiner, nullValue, l) {
  if (l.length === 0) {
    return nullValue;
  }
  var first = l.shift();
  return combiner(first, accumulate(combiner, nullValue, l));
}

sumOfSquares([1,2,3,4,5]);  // 55
