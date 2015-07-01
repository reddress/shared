var ciphertext = CryptoJS.AES.encrypt("Hello AES", "ThePassword").ciphertext.toString(CryptoJS.enc.Base64);

console.log(ciphertext);

var CJSciphertext = CryptoJS.enc.Base64.parse(ciphertext);

console.log(CryptoJS.AES.decrypt(CJSciphertext, "ThePassword").toString(CryptoJS.enc.Utf8));
