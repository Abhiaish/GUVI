function transformFirstAndLast(arr) {
 var obj={}
 length=arr.length;
    lastElement=arr[length-1];
    key=arr[0];
    value=lastElement;
    obj[key]=value;
    return obj;
    
}
console.log(transformFirstAndLast([4,5,6,2]));