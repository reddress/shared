"use strict";

function Rabbit(color) {
  this.color = color;
}

var Dog = function(breed) {
  this.breed = breed;
}

function speak(line) {
  console.log("the " + this.type + " rabbit says " + line + "");
}
