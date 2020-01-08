function transformEmployeeData(employeeData) {
var newList = [];
  
    for(var i = 0; i< employeeData.length; i++) {
      var workerData = {};
      for(var x = 0; x< employeeData[i].length; x++) {
        workerData[employeeData[i][x][0]] = employeeData[i][x][1];
      }
    return workerData;
  
  }
}
  console.log(transformEmployeeData([[['firstName', 'Vasanth'], ['lastName', 'Raja'], ['age', 24], ['role', 'JSWizard']], [['firstName', 'Sri'], ['lastName', 'Devi'], ['age', 28], ['role', 'Coder']]]));