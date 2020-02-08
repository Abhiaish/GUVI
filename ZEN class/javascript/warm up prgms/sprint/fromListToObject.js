function fromListToObject(arr){
var a={}
for (i=0;i<arr.length;i++){
    a[arr[i][0]] = arr[i][1]
}
    return a;
}