var object = {
  name: 'Holly',
  edad: 35,
  papel: 'productor'
}

function convertObjectToList(object) {
  arr = [];
  for (var key in object){
    arr.push([key,object[key]]);
    
  }
  return arr;
}