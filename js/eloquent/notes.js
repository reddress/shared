// recursive findSolution to adding 5 or multiplying by 3

function findSolution(target) {
  function find(start, history) {
    if (start === target) {
      return history;
    } else if (start > target) {
      return null;
    } else {
      return find(start + 5, "(" + history + " + 5)") ||
        find(start * 3, "(" + history + " * 3)");
    }
  }
  return find(1, "1");
}

