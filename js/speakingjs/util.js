function getDefiningObject(obj, propKey) {
  obj = Object(obj)
  while (obj && !{}.hasOwnProperty.call(obj, propKey)) {
    obj = Object.getPrototypeOf(obj);
  }
  return obj;
}

