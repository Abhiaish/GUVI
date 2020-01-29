const search = document.getElementById('search');
const matchList = document.getElementById('match-list');

//search states.json and filter it
const searchStates = async searchText => {
    const res = await fetch('../data/states.json');
    var states = await res.json();
    //console.log(states);
   

  //get match to current text input
  //console.log(typeof(states));
  let matches = states.filter(state => {
    const regex = new RegExp(`^${searchText}`,'gi');
    return state.name.match(regex) || state.abbr.match(regex);
  });
  //console.log(matches);
  if(searchText.length === 0){
      matches =[];
      matchList.innerHTML='';
  }
  outputHtml(matches);
};

//show results in HTML
const outputHtml = matches =>{
    if(matches.length>0){
        const html = matches.map(match => `<div class="card card-body mb-1">
        <h4> ${match.name} (${match.abbr})
        <span class = "text-primary"> ${match.capital}</span></h4>
        <small>Lat:${match.lat}/Long:${match.long}</small>
        </div>
        `
        )
        .join('');

        matchList.innerHTML = html;  
    }
       
    
}
search.addEventListener('input',()=>searchStates(search.value));