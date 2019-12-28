
//json dict to count repeating elements
let arr = ['Apple', 'Banana', 'Apple', 'Durian', 'Durian', 'Durian'].reduce((arr, val) => arr.set(val, 1 + (arr.get(val) || 0)), new Map());

console.log(arr);
    