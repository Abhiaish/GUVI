function fromListtoObject(array){
    var a={}
    for(let i=0;i<array.length;i++){
        a[array[i][0]]=array[i][1];
    }
    return a;
}
console.log(fromListtoObject([['make', 'Ford'], ['model', 'Mustang'], ['year', 1964]]))