//objtolist
var object = {name: "ISRO", age: 35, role: "Scientist"};
var keys=[];
var array=[];
var values=[];
for(let i in object){
    values[i]=object[i];
    }

console.log(values);