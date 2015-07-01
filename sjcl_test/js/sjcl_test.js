"use strict";

var encrypted = sjcl.encrypt("ThePassword", "Hello SJCL");

console.log(encrypted);

var decrypted = sjcl.decrypt("ThePassword", encrypted);

console.log(decrypted);
