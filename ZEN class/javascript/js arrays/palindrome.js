 function palindromes(a){
var palinrome = [];
var notpalinrome = [];
var len = a.length;
for (var i = 0; i < len; i++) {
  len2 = a[i].length;
  var mid = Math.floor(len2/2);
  for (var j = 0; j < mid; j++) {
    if (a[i][j] !== a[i][len2-1-j]) {
      notpalinrome.push(a[i]);
      break
    }else {
      palinrome.push(a[i]);
      break
    }
  }
}
console.log(palinrome);
console.log(notpalinrome);

}