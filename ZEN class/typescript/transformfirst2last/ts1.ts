function transformFirstAndLast(array){
    let obj={}
    let length1=array.length;
    let lastElement=array[length1-1];
    let key=array[0];
    let value=lastElement;
    obj[key]=value;
    return obj;
}
console.log(transformFirstAndLast(["GUVI", "I", "am", "Geek"]));
