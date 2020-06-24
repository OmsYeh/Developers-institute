//1
let legal_age = checkDriverAge();
function checkDriverAge(){
  let user_age = prompt('What is your age?');
  if (Number(user_age) < 18){
      alert("Sorry, you are too yound to drive this car. Powering off");
  } else if (Number(user_age) > 18){
      alert("Powering On. Enjoy the ride!");
  } else if (Number(user_age) === 18){
      alert("Congratulations on your first year of driving. Enjoy the ride!");
  } return;
}
//2
let legal_age = checkDriverAge();
function checkDriverAge(Number){
  if (Number < 18){
      alert("Sorry, you are too yound to drive this car. Powering off");
  } else if (Number > 18){
      alert("Powering On. Enjoy the ride!");
  } else if (Number === 18){
      alert("Congratulations on your first year of driving. Enjoy the ride!");
  } return;
}
checkDriverAge()  //<-----place age here
console.log(legal_age);
