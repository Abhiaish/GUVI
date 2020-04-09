function Odd(array){
  var arr = [];
  for (let i = 0; i < array.length; i++){
    if (array[i] % 2 !== 0){
      arr.push(array[i]);
    }
  }
  return arr;
    
}
var a = [1,2,3,4,5,6,7]
console.log(Odd(a));