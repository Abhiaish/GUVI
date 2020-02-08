var expected = {foo: 6, bar: 5};
var actual = {foo: 5, bar: 6};
testCase ="passed";
function assertObjectsEqual(actual,expected,testCase){
    actual1=JSON.stringify(actual)
    expected1=JSON.stringify(expected)
    console.log(expected1);
    console.log(actual1);
    if(expected1 == actual1){
        return testCase;
    } else{
        return testCase="failed";
    }

}