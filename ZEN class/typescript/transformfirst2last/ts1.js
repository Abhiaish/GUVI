function transformFirstAndLast(array) {
    var obj = {};
    var length1 = array.length;
    var lastElement = array[length1 - 1];
    var key = array[0];
    var value = lastElement;
    obj[key] = value;
    return obj;
}
console.log(transformFirstAndLast(["GUVI", "I", "am", "Geek"]));
