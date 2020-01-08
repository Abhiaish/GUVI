//Equal assert
var expected = { prop1: { a: "fun", b: "test" }, prop2: [1, 2, 3, 4] };
var actual = { prop2: [1, 2, 3, 4], prop1: { a: "fun", b: "test" } };
function assertObjectsEqual(actual, expected) {
    var expected1 = JSON.stringify(expected);
    var actual1 = JSON.stringify(actual);
    if (expected1 == actual1) {
        return true;
    }
    else {
        return false;
    }
}
console.log(assertObjectsEqual(actual, expected));
