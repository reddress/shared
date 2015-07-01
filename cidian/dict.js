
/*
function findLine(lineNumber) {
  return words[lineNumber];
}

document.getElementById("getLineNumber").addEventListener("click", function() {
  document.getElementById("word").innerHTML = findLine(parseInt(
    document.getElementById("lineNumber").value, 10));
});
*/

/* SAMPLE ENTRY
"一團糟 一团糟 [yi1 tuan2 zao1] /chaos/bungle/complete mess/"
*/

// build fuzzy GR map
var fuzzyGRDict = {};

for (var wordIndex = 0, wordlistLen = words.length; wordIndex < wordlistLen; wordIndex++) {
  var pyPhrase = words[wordIndex].match(/\[.*?\]/)[0];
  pyPhrase = pyPhrase.replace(/[0-9\[\]]/g, "");

  pySyllables = pyPhrase.split(" ");
  
  var grPhrase = "";
  for (var j = 0, pyPhraseLen = pySyllables.length; j < pyPhraseLen; j++) {
    grPhrase += py2gr(pySyllables[j] + "1") + " ";
  }
  grPhrase = grPhrase.trim();
  
  if (!fuzzyGRDict[grPhrase]) {
    fuzzyGRDict[grPhrase] = [wordIndex];
  } else {
    fuzzyGRDict[grPhrase].push(wordIndex);
  }
}

function pyPhrase2gr(pyPhrase) {
  var grPhrase = "";
  var pySyllables = pyPhrase.split(" ");
  for (var i = 0, len = pySyllables.length; i < len; i++) {
    grPhrase += py2gr(pySyllables[i]) + " ";
  }
  return grPhrase;
}

function htmlifyWord(word) {
  var parts = word.split(" ");
  var trad = parts[0];
  var py = word.match(/\[.*?\]/)[0];
  py = py.slice(1, py.length - 1);
  
  result = '<span class="hint--top" data-hint="' + trad + '">' +
    trad + "</span> " + pyPhrase2gr(py) +
    parts.slice(2).join(" ") + "<br>";
  return result;
}

function findDefinition(definition) {
  var resultBlock = "";
  var searchTerm = definition.toLowerCase().trim();
  for (var i = 0, len = words.length; i < len; i++) {
    if (words[i].toLowerCase().indexOf(searchTerm) !== -1) {
      resultBlock += htmlifyWord(words[i]);
    }
  }
  return resultBlock;
}

function findByFuzzyGR(fuzzyGR) {
  var grSyllables = fuzzyGR.split(" ");
  var grToneless = "";
  // convert to pinyin, strip tones, then add tone 1, and reconvert to GR
  for (var i = 0, grSyllablesLen = grSyllables.length; i < grSyllablesLen; i++) {
    grToneless += py2gr(gr2py(grSyllables[i]).replace(/[0-9]/g, "") + "1") + " ";
  }

  try {
    var wordIndices = fuzzyGRDict[grToneless.trim()];

    var resultBlock = "";
    
    for (var i = 0, wordlistLen = wordIndices.length; i < wordlistLen; i++) {
      resultBlock += htmlifyWord(words[wordIndices[i]]);
    }
  } catch (e) {
    var resultBlock = "Cannot convert GR or no words found.";
  }
  
  return resultBlock;
}

document.getElementById("getDefinition").addEventListener("click", function() {
  document.getElementById("word").innerHTML = findDefinition(document.getElementById("definition").value);
  document.getElementById("definition").value = "";
  document.getElementById("definition").focus();
});

document.getElementById("getGR").addEventListener("click", function() {
  document.getElementById("word").innerHTML = findByFuzzyGR(document.getElementById("gr").value);
  document.getElementById("gr").value = "";
  document.getElementById("gr").focus();
});
