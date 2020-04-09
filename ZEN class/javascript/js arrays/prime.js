function Prime(array) {
  
    var arr = [];
    for(var i = 2; i <= array; i++) {
        var count = 0;
        for (var j=1;j<=i;j++) {
            if(i%j == 0){
                count=count+1;
            }
        }
        if(count===2){
            arr.push(i);
        }
      }   
    console.log(arr);
    }
